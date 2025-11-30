from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "Snippets"
router = DefaultRouter()
router.register(r"snippets" , views.Snippet_ViewSet)
router.register(r"users" , views.User_ViewSet)

urlpatterns = [
    path("" , include(router.urls)),
]
