# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from solo.models import SingletonModel


class DynamicEmailConfiguration(SingletonModel):
    host = models.CharField(
        blank=True, null=True,
        max_length=256, verbose_name="Email Host")

    port = models.SmallIntegerField(
        blank=True, null=True,
        verbose_name="Email Port")

    from_email = models.CharField(
        blank=True, null=True,
        max_length=256, verbose_name="Default From Email")

    username = models.CharField(
        blank=True, null=True,
        max_length=256, verbose_name="Email Authentication Username")

    password = models.CharField(
        blank=True, null=True,
        max_length=256, verbose_name="Email Authentication Password")

    use_tls = models.BooleanField(
        default=False, verbose_name="Use TLS")

    use_ssl = models.BooleanField(
        default=False, verbose_name="Use SSL")

    fail_silently = models.BooleanField(
        default=False, verbose_name="Fail Silently")

    timeout = models.SmallIntegerField(
        blank=True, null=True,
        verbose_name="Email Send Timeout (seconds)")

    def clean(self):
        if self.use_ssl and self.use_tls:
            raise ValidationError(
                "\"Use TLS\" and \"Use SSL\" are mutually exclusive, "
                  "so only set one of those settings to True.")
        settings.DEFAULT_FROM_EMAIL = self.from_email

    def __str__(self):
        return "Email Configuration"

    class Meta:
        verbose_name = "Email Configuration"


__all__ = ['DynamicEmailConfiguration']
