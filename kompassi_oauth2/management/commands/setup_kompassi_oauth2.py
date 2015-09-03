# encoding: utf-8

from django.core.management import call_command
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    args = ''
    help = 'Setup Kompassi OAuth2'

    def handle(self, *args, **options):
        group, unused = Group.objects.get_or_create(name=settings.KOMPASSI_EDITOR_GROUP)

        content_permissions = Permission.objects.filter(
            content_type__app_label='content',
            content_type__model__in=['page', 'redirect', 'blogpost', 'blogcomment'],
        )

        group.permissions.add(*content_permissions)

        ads_permissions = Permission.objects.filter(
            content_type__app_label='ads',
            content_type__model__in=['banner', 'bannerclick'],
        )

        group.permissions.add(*ads_permissions)
