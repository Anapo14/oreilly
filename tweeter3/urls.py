"""
tweeter3 URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from tweeter import views
#from tweeter.views import UserViewSet, TweetViewSet, SignUp, current_user

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tweets', views.TweetViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/current/', views.current_user, name='current'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #configure a new url mapping for frontend.
    # path('', include('frontend.urls'))
]
