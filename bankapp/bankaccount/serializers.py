from rest_framework import serializers

from .models import Account, CreditCard, Transfer


class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class TransferSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Transfer
        fields = '__all__'


class CreditCardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CreditCard
        fields = '__all__'
