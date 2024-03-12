from django.conf import settings
from django.http import HttpResponseRedirect


def email_confirm_redirect(_request, key):
    return HttpResponseRedirect(f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/")


def password_reset_confirm_redirect(_request, uid, token):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{uid}/{token}/"
    )
