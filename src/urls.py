from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from allauth.account.views import login

urlpatterns = [
    path('', login),
    path('backend/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
]
