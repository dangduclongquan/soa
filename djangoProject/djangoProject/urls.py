"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
# Customer Information
    # C
    path('customer-information/create/', views.CustomerCreateAPIView.as_view()),

    # R
    path('customer-information/<int:pk>/', views.CustomerInformationAPIView.as_view()),
    path('customer-information/all/', views.CustomerAllAPIView.as_view()),

    # U
    path('customer-information/<int:pk>/update/', views.CustomerUpdateAPIView.as_view()),

    # Transaction History
    path('customer-information/<int:pk>/transaction-history/', views.TransactionHistoryAPIView.as_view()),

# Loan
    # C
    path('loan/create/', views.LoanCreateAPIView.as_view()),

    # R
    path('loan/<int:pk>/', views.LoanAPIView.as_view()),
    path('loan/all/', views.LoanAllAPIView.as_view()),

    # U
    path('loan/<int:pk>/update/', views.LoanUpdateAPIView.as_view()),

# Verify
    path('verify/', include('verifyCustomerInformation.urls')),

# Bank
    path('bank/', include('bank.urls')),

# Calculate
    path('calculate/', include('calculateMaximumLoan.urls')),

# Result
    path('result/', include('result.urls'))
]
