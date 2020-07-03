import warnings

from django.apps import AppConfig
from django.contrib import admin
from django.utils.translation import gettext as _
from django.utils.translation import gettext_noop as _n


class Config(AppConfig):
    name = 'Application'
    verbose_name = _n('django-init')

    def ready(self):
        # Disallow bulk delete
        # admin.site.disable_action('delete_selected')

        admin.AdminSite.site_header = _('django-init')
        admin.AdminSite.site_title = _('django-init')
        admin.AdminSite.index_title = _('django-init')

        # Filter EXIF warnings (too many corrupt files)
        # warnings.filterwarnings("ignore", "(Possibly )?corrupt EXIF data", UserWarning)
