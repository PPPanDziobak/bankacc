from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet

from . serializers import AccountSerializer, CreditCardSerializer, TransferSerializer
from .models import Account, CreditCard, Transfer


class BaseViewSet(ViewSet):
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
        return Response(response)


class AccountViewset(BaseViewSet):
    queryset = Account.objects.all()
    serializer_cass = AccountSerializer


class CardViewset(BaseViewSet):
    queryset = CreditCard.objects.all()
    serializer_cass = AccountSerializer


class TransferViewset(BaseViewSet):
    queryset = Transfer.objects.all()
    serializer_cass = AccountSerializer
