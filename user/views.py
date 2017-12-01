from django.contrib.auth import get_user_model, views
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic, View

from user.forms import SignupForm, SigninForm
from user.tokens import account_activation_token as account_activation


class SignIn(views.LoginView):
    template_name = 'signup.html'
    form_class = SigninForm
    extra_context = {'action': 'Sign In'}


class SignOut(views.LogoutView):
    next_page = '/'


class SignUp(generic.FormView):
    form_class = SignupForm
    template_name = 'signup.html'

    def _send_activation_email(self, form, user):
        current_site = get_current_site(self.request)
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation.make_token(user),
        })
        mail_subject = 'Activate your blog account.'
        recipient = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[recipient])
        email.send()

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        self._send_activation_email(form, user)
        return HttpResponse(
            'Please confirm your email address to complete the registration'
        )


class Activate(View):

    def get(self, _, uid_b64, token):
        user_model = get_user_model()
        try:
            uid = force_text(urlsafe_base64_decode(uid_b64))
            user = user_model.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
            user = None
        if user is not None and account_activation.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. '
                                'Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')
