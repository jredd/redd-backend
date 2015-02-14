from __future__ import absolute_import

from django.views.decorators.debug import sensitive_post_parameters
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.sites.models import get_current_site
from django.contrib.admin.options import IS_POPUP_VAR
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import get_object_or_404
from django.contrib.admin.util import unquote
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.contrib import messages
from django.template import loader
from django.contrib import admin

from . import models
from . import forms

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())


def make_active(modeladmin, request, queryset,
                use_https=False,
                from_email=None,
                subject_template_name='registration/registration_activation_subject.txt',
                email_template_name='registration/registration_activation_email.html',
                ):
    queryset.update(is_active=True)

    for obj in queryset:
        # check to see if the user name and last name exists
        # if not just set the user name to the email
        from django.core.mail import send_mail
        if obj.first_name or obj.last_name:
            user = '{} {}'.format(obj.first_name, obj.last_name)
        else:
            user = obj.email
        email_receiver = obj.email
        current_site = get_current_site(request)
        site_name = current_site.name
        domain = current_site.domain
        c = {
            'email': email_receiver,
            'domain': domain,
            'site_name': site_name,
            'user': user,
            'protocol': 'https' if use_https else 'http',
            }
        subject = loader.render_to_string(subject_template_name, c)
        email = loader.render_to_string(email_template_name, c)

        send_mail(subject, email, from_email, [email_receiver])


def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = forms.CustomUserChangeForm
    add_form = forms.CustomUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')
    ordering = ('email',)
    actions = [make_active, make_inactive]

    def get_urls(self):
        from django.conf.urls import patterns
        return patterns('',
                        (r'^(.+)/password/$',
                         self.admin_site.admin_view(self.user_change_password))) + super(CustomUserAdmin,
                                                                                         self).get_urls()
    @sensitive_post_parameters_m
    def user_change_password(self, request, id, form_url=''):

        id = unquote(id)

        if not self.has_change_permission(request):
            raise PermissionDenied
        user = get_object_or_404(self.get_queryset(request), pk=id)

        if request.method == 'POST':
            form = self.change_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                change_message = self.construct_change_message(request, form, None)
                self.log_change(request, user, change_message)
                msg = ugettext('Password changed successfully.')
                messages.success(request, msg)
                return HttpResponseRedirect('..')
        else:
            form = self.change_password_form(user)

        fieldsets = [(None, {'fields': list(form.base_fields)})]
        adminForm = admin.helpers.AdminForm(form, fieldsets, {})

        context = {
            'title': _('Change password: %s') % escape(user.get_username()),
            'adminForm': adminForm,
            'form_url': form_url,
            'form': form,
            'is_popup': IS_POPUP_VAR in request.REQUEST,
            'add': True,
            'change': False,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_absolute_url': False,
            'opts': self.model._meta,
            'original': user,
            'save_as': False,
            'show_save': True,
        }
        return TemplateResponse(request,
            self.change_user_password_template or
            'admin/auth/user/change_password.html',
            context, current_app=self.admin_site.name)

admin.site.register(models.CustomUser, CustomUserAdmin)
# admin.site.register(Dealer, DealerAdmin)
