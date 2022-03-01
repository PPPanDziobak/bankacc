from django.urls import path
from .views import (
    AccountCreateView,
    AccountDetailView,
    HomeView,
    LoginView,
    TransferHistoryView,
    TransferView
)


app_name = 'bankaccount'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('create-account/', AccountCreateView.as_view(), name='create-account'),
    path('my-account/', AccountDetailView.as_view(), name='account-details'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('my-account/transfer-history', TransferHistoryView.as_view(), name='transfer-history'),
]
