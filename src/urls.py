from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from allauth.account.views import login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', login),
    path('backend/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
