from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()

class AccountsView(LoginRequiredMixin, TemplateView):
    pass

#auth pages
auth_pages_confirm_email_view = AccountsView.as_view(template_name="auth/confirm-email.html")
auth_pages_confirm_email_2_view = AccountsView.as_view(template_name="auth/confirm-email-2.html")

auth_pages_login_2_view = AccountsView.as_view(template_name="auth/login-2.html")
auth_pages_logout_view = AccountsView.as_view(template_name="auth/logout.html")
auth_pages_logout_2_view = AccountsView.as_view(template_name="auth/logout-2.html")

auth_pages_lock_screen_view = AccountsView.as_view(template_name="auth/lock-screen.html")
auth_pages_lock_screen_2_view = AccountsView.as_view(template_name="auth/lock-screen-2.html")


auth_pages_recoverpw_view = AccountsView.as_view(template_name="auth/recoverpw.html")
auth_pages_recoverpw_2_view = AccountsView.as_view(template_name="auth/recoverpw-2.html")
auth_pages_register_2_view = AccountsView.as_view(template_name="auth/register-2.html")

auth_pages_signin_signup_view = AccountsView.as_view(template_name="auth/signin-signup.html")
auth_pages_signin_signup_2_view = AccountsView.as_view(template_name="auth/signin-signup-2.html")

