from __future__ import absolute_import

from django.contrib.sites.models import get_current_site
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.template import loader

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


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
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')
    ordering = ('email',)
    actions = [make_active, make_inactive]


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Dealer, DealerAdmin)
