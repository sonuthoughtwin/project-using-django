from django.urls import path
from .import views
from .views import SturegCreat
urlpatterns=[
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("reg",SturegCreat.as_view()),
]