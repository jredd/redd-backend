from __future__ import absolute_import

from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.template import loader

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    def clean_username(self):
        pass

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserRegistrationForm(CustomUserCreationForm):

    def save(self, commit=True, domain_override=None,
             subject_template_name='registration/registration_subject.txt',
             email_template_name='registration/registration_email.html',
             use_https=False,
             token_generator=default_token_generator,
             from_email=None,
             request=None,
             email_receiver=None,
             ):
        email = self.cleaned_data["email"]
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()

        # Email notification setup
        from django.core.mail import send_mail
        UserModel = get_user_model()
        active_users = UserModel._default_manager.filter(
            email__iexact=email, is_active=False)
        for user in active_users:
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            c = {
                'email': email_receiver,
                'domain': domain,
                'site_name': site_name,
                'user': user,
                'protocol': 'https' if use_https else 'http',
            }
            subject = loader.render_to_string(subject_template_name, c)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            email = loader.render_to_string(email_template_name, c)
            send_mail(subject, email, from_email, [email_receiver])
        return user


class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'is_active', 'is_staff', 'first_name', 'last_name', 'date_joined')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

    def save(self, commit=True, domain_override='sister.tv',
             subject_template_name='registration/registration_activation_subject.txt',
             email_template_name='registration/registration_activation_email.html',
             use_https=False,
             token_generator=default_token_generator,
             from_email=None,
             email_receiver=None,
             ):
        user = super(UserChangeForm, self).save(commit=False)
        email_receiver = user.email
        print Site.objects.get_current()
        if commit:
            user.save()
        if not domain_override:
            current_site = Site.objects.get_current()
            site_name = current_site.name
            domain = Site.objects.get_current()
        else:
            site_name = domain = Site.objects.get_current()
        # only sends an email notification if the user's previous
        # is_active state was false and if the new state is true
        if not self.initial['is_active'] and user.is_active:
            # Email notification setup
            from django.core.mail import send_mail
            c = {
                'email': email_receiver,
                'domain': domain,
                'site_name': site_name,
                'user': user,
                'protocol': 'https' if use_https else 'http',
            }
            subject = loader.render_to_string(subject_template_name, c)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            email = loader.render_to_string(email_template_name, c)
            send_mail(subject, email, from_email, [email_receiver])

        return user
