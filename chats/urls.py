from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('api/v1/room', views.RoomViewsSets)
router.register('api/v1/message', views.MessageViewsSets)

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessage/<str:room>/', views.getMessages, name='getMessages')
]
urlpatterns += router.urls
