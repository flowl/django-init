from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.Application import settings
from apps.Application.managers import CustomUserManager


class CustomUser(AbstractUser):
    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]
        app_label = 'Application'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    objects = CustomUserManager()

    # username = email
    # username = models.EmailField(verbose_name=_('Username'), unique=True, blank=False)

    email = models.EmailField(verbose_name=_('Email'), unique=True, blank=False)

    language = models.CharField(verbose_name=_('Language'), choices=settings.LANGUAGES, max_length=5, default='en',
                                null=False,
                                blank=False, help_text='Language preference')

    # privacy_accepted_at = models.DateTimeField(verbose_name=_('Privacy accepted at'), default=None,
    #                                           blank=False, null=True, help_text=_(
    #        'The timestamp of when the privacy terms were beeing accepted.'))

    displayname = models.CharField(verbose_name=_('Displayname'), max_length=128, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def display_group(obj):
        return ', '.join(str(g) for g in obj.groups.all())

    display_group.short_description = _('Groups')
