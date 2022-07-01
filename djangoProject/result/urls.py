from django.urls import path, include
from . import views

urlpatterns = [
    # C
    path('', views.ResultCreateAPIView.as_view()),

    # R
    path('<int:pk>/', views.ResultAPIView.as_view()),
    path('all/', views.ResultAllAPIView.as_view()),

]
