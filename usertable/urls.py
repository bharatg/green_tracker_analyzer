from django.urls import path
from django.conf.urls import url, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'habits', views.HabitViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^user/$', views.user_list),
    url(r'^habit/$', views.habit_list),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^habit/(?P<pk>[0-9]+)/$', views.habit_detail),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('weekly/', views.weekly, name='weekly')
]
