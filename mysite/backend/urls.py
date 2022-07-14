from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('test', views.TestViewSet)
router.register('question', views.QuestionViewSet)
router.register('answer', views.AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('guardar-certificacion/', views.guardar_certificacion),
    path('get-certificacion/', views.get_certificacion),
    path('revision-certificacion/', views.revision_certificacion),
]