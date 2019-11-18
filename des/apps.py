# -*- coding: utf-8

from django.apps import AppConfig
from django.conf import global_settings, settings


class DjangoDesConfig(AppConfig):
    name = 'des'
    verbose_name = 'Dynamic Email Settings'
    verbose_name_plural = verbose_name

    def ready(self):
        from des.models import DynamicEmailConfiguration

        c = DynamicEmailConfiguration.get_solo()
        if settings.DEFAULT_FROM_EMAIL == global_settings.DEFAULT_FROM_EMAIL:
            settings.DEFAULT_FROM_EMAIL = c.from_email
