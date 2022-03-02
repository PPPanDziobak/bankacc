from django.urls import include, path
from rest_framework import routers
from .views import (
    AccountCreateView,
    AccountDetailView,
    ChangePinView,
    HomeView,
    LoginView,
    TransferHistoryView,
    TransferView
)
from .viewsets import AccountViewset, CardViewset, TransferViewset


router = routers.DefaultRouter()
router.register(r'account', AccountViewset)
router.register(r'card', CardViewset)
router.register(r'transfer', TransferViewset)

app_name = 'bankaccount'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('create-account/', AccountCreateView.as_view(), name='create-account'),
    path('<int:id>/', AccountDetailView.as_view(), name='account-details'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('card/', ChangePinView.as_view(), name='card'),
    path('my-account/transfer-history', TransferHistoryView.as_view(), name='transfer-history'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
