from django.urls import path

from res_api import views

urlpatterns = [
    path('nickapi/', views.NickApiView.as_view()),
]
