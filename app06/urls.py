from django.contrib import admin
from django.urls import path, include
from . import views
game_list = views.GameViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
game_detail = views.GameViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('games', views.GameViewSet)

from rest_framework.documentation import include_docs_urls
urlpatterns = [
    # path('games/', views.GameList.as_view(), name='game-list'),
    # path('games/<int:pk>/', views.GameDetail.as_view(), name='game-detail'),
    path('', include(router.urls)),
    path('parser/', views.ParserView.as_view(), name='parser')
]
