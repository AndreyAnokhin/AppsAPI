from django.urls import path

from .views import AppsView, SingleAppView


app_name = "apps_api"

urlpatterns = [
    path('', AppsView.as_view()),
    path('<str:title>', SingleAppView.as_view()),
]
