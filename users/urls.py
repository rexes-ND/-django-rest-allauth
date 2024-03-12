from django.urls import path
from django.views.generic import TemplateView

from dj_rest_auth.views import (
    LoginView,
    UserDetailsView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordChangeView,
)
from dj_rest_auth.registration.views import (
    RegisterView,
    VerifyEmailView,
    ResendEmailVerificationView,
)

from .views import email_confirm_redirect, password_reset_confirm_redirect

urlpatterns = [
    # User details API
    path(
        "",
        UserDetailsView.as_view(),
        name="rest_user_details",
    ),
    # Register API
    path(
        "register/",
        RegisterView.as_view(),
        name="rest_register",
    ),
    path(
        "verify-email/",
        VerifyEmailView.as_view(),
        name="rest_verify_email",
    ),
    path(
        "resend-email/",
        ResendEmailVerificationView.as_view(),
        name="rest_resend_email",
    ),
    path(
        "login/",
        LoginView.as_view(),
        name="rest_login",
    ),
    # NOTE: Sends email with link using
    # reverse("password_reset_confirm")
    path(
        "password-reset/",
        PasswordResetView.as_view(),
        name="rest_password_reset",
    ),
    # Redirect to client side (Reset)
    path(
        "password-reset-confirm/<str:uid>/<str:token>/",
        password_reset_confirm_redirect,
        name="password_reset_confirm",
    ),
    #
    path(
        "password-reset-confirm/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    # Redirect to client side (Verify)
    path(
        "account-confirm-email/<str:key>/",
        email_confirm_redirect,
        name="account_confirm_email",
    ),
    # NOTE: Register API sends email with link using
    # reverse("account_email_verification_sent")
    path(
        "account-confirm-email/",
        TemplateView.as_view(),
        name="account_email_verification_sent",
    ),
    path(
        "password-change/",
        PasswordChangeView.as_view(),
        name="rest_password_change",
    ),
]
