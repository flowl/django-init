
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView

from apps.Application import settings
from apps.Application.views import HtmlView

# from apps.OtherApp.urls import urlpatterns as other_app_urlpatterns


# If you don't want to use different language prefixes, remove the `i18n_patterns()` call

urlpatterns = [] + i18n_patterns(
    path('', HtmlView.as_view(template_name='sites/index.html',
                              extra_context={'public_port': settings.env('PUBLIC_PORT'),
                                             'app_port': settings.env('APP_PORT')}),
         name='start'),
    path('hello-world/',
         TemplateView.as_view(template_name='sites/hello_world.html', extra_context={'greet_name': 'world'}),
         name='hello_world'),

    path('i18n/', include('django.conf.urls.i18n')),

    path('account/', HtmlView.as_view(), name='account'),
    path('account/login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('admin/', admin.site.urls),
)

# urlpatterns += other_apps_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
