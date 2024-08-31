from django.urls import path, include

from rest_framework.routers import DefaultRouter

from res_api import views


router = DefaultRouter()
router.register('nick-viewset', views.NickViewSet, basename='nick-viewset')

urlpatterns = [
    path('nickapi/', views.NickApiView.as_view()),
    path('', include(router.urls))
]
