from django.db import IntegrityError

from rest_framework import serializers
from dj_rest_auth.registration.serializers import (
    RegisterSerializer as RestRegisterSerializer,
)


# https://github.com/iMerica/dj-rest-auth/issues/552
class RegisterSerializer(RestRegisterSerializer):
    # def validate_email(self, email):
    #     email = get_adapter().clean_email(email)
    #     if email and EmailAddress.objects.filter(email__iexact=email).exists():
    #         raise serializers.ValidationError(
    #             "A user is already registered with this e-mail address.",
    #         )
    #     return email

    # Cleanest implementation in my opinion
    def save(self, request):
        try:
            return super().save(request)
        except IntegrityError as e:
            if "email" in str(e):
                raise serializers.ValidationError(
                    "A user is already registered with this e-mail address.",
                )
            else:
                # Coming from somewhere else, then propagate
                raise
