from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiapp import views, model_views

router = DefaultRouter()
router.register('studentapi', views.StudentViewSet, basename='student')

router1 = DefaultRouter()
router1.register('studentapi', model_views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('mbv/', include(router1.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
