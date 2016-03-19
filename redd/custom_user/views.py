from django.contrib.auth.tokens import default_token_generator
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.http import HttpResponse

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .forms import CustomUserRegistrationForm
from .serializers import UserSerializer
from .models import CustomUser


@csrf_protect
def register(request,
             is_admin_site=False,
             template_name='registration/registration_form.html',
             email_template_name='registration/registration_email.html',
             subject_template_name='registration/registration_subject.txt',
             registration_form=CustomUserRegistrationForm,
             token_generator=default_token_generator,
             post_registration_redirect=None,
             from_email=None,
             current_app=None,
             extra_context=None,
             ):

    if post_registration_redirect is None:
        post_registration_redirect = reverse('password_reset_done')
    else:
        post_registration_redirect = resolve_url(post_registration_redirect)
    if request.method == "POST":
        form = registration_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'email_receiver': 'sister_operations@sister.tv',
            }
            if is_admin_site:
                opts = dict(opts, domain_override=request.get_host())
            form.save(**opts)
            return HttpResponseRedirect(post_registration_redirect)
    else:
        form = registration_form()
    context = {
        'form': form,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context, current_app=current_app)


def registration_done(
        request,
        template_name='registration/registration_done.html',
        current_app=None,
        extra_context=None
):
    context = {}
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Lists all the info for the given user"""
        user = self.kwargs['pk']
        return CustomUser.objects.filter(email=user)


class UsersList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CustomUser.objects.all()


# class ObtainToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.DATA)
#         if serializer.is_valid():
#             token, created = Token.objects.get_or_create(user=serializer.object['user'])
#             print '{} just attempted to retrieve a token'.format(serializer.object['user'])
#             return Response({'token': token.key})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
