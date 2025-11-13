from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import Profile_View_Set

app_name = "api"

router = DefaultRouter()
router.register(r"Profiles" , Profile_View_Set , basename="profile")

urlpatterns = [
    path("" , include(router.urls))
]