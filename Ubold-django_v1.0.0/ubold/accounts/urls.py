from django.urls import path

from .views import (

    auth_pages_confirm_email_view,
    auth_pages_confirm_email_2_view,
    auth_pages_login_2_view,
    auth_pages_logout_view,
    auth_pages_logout_2_view,
    auth_pages_lock_screen_view,
    auth_pages_lock_screen_2_view,
    auth_pages_recoverpw_view,
    auth_pages_recoverpw_2_view,
    auth_pages_register_2_view,
    auth_pages_signin_signup_view,
    auth_pages_signin_signup_2_view,

)


app_name = "accounts"
urlpatterns = [

    # pages
    path("confirm-mail", view=auth_pages_confirm_email_view, name="confirm-email"),
    path("confirm-mail-2", view=auth_pages_confirm_email_2_view, name="confirm-email-2"),
    path("login-2", view=auth_pages_login_2_view, name="login-2"),
    path("logout", view=auth_pages_logout_view, name="logout"),
    path("logout-2", view=auth_pages_logout_2_view, name="logout-2"),
    path("lock-screen", view=auth_pages_lock_screen_view, name="lock-screen"),
    path("lock-screen-2", view=auth_pages_lock_screen_2_view, name="lock-screen-2"),
    path("recoverpw", view=auth_pages_recoverpw_view, name="recoverpw"),
    path("recoverpw-2", view=auth_pages_recoverpw_2_view, name="recoverpw-2"),
    path("register-2", view=auth_pages_register_2_view, name="register-2"),
    path("signin-signup", view=auth_pages_signin_signup_view, name="signin-signup"),
    path("signin-signup-2", view=auth_pages_signin_signup_2_view, name="signin-signup-2"),
]
