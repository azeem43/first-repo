from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookingView, basename='booking')
urlpatterns = router.urls

urlpatterns = [
    path('',views.index,name='index'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('',include(router.urls))
    
]
