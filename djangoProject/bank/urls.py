from django.urls import path, include
from . import views

urlpatterns = [
    # C
    path('create/', views.BankCreateAPIView.as_view()),

    # R
    path('<int:pk>/', views.BankAPIView.as_view()),
    path('all/', views.BankAllAPIView.as_view())
]