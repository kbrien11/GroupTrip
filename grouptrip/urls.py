from django.urls import path,include
from . import views

from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    path('register',views.createUser),
    path('login',views.login),
    path('sendMessage/<token>/<groupName>',views.sendMessage),
    path('viewMessages/<token>/<groupName>',views.viewMessages),
    path('users/<groupName>/<token>',views.getUsersPerGroup),
    path('checkActiveUser/<username>',views.checkActiveUser),
    path('logout/<username>',views.logout)
]