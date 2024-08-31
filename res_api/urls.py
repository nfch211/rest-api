from django.urls import path, include

from rest_framework.routers import DefaultRouter

from res_api import views


router = DefaultRouter()
router.register('nick-viewset', views.NickViewSet, basename='nick-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('nickapi/', views.NickApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
