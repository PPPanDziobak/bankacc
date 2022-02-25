from django.db import models


class CreditCard(models.Model):
    card_number = models.CharField(u'Numer karty')
    expiration_date = models.DateField(u'Data ważności')
    cvc_number = models.CharField(u'Numer CVC', max_length=3)


class Account(models.Model):
    account_number = models.CharField(u'Numer konta')
    balance = models.IntegerField(u'Stan konta')
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)


class AccountOwner(models.Model):
    firstname = models.CharField(u'Imię', max_length=50)
    lastnamename = models.CharField(u'Nazwisko', max_length=50)
    addess = models.CharField(u'Adres', max_length=250)
    city = models.CharField(u'Miasto', max_length=250)
    country = models.CharField(u'Kraj', max_length=250)
    date_of_birth = models.DateField(u'Data urodzenia', auto_now_add=True, blank=True)
    account_number = models.ForeignKey(Account, on_delete=models.CASCADE)


class TransactionHistory(models.Model):
    transfer_receiver_firstname = models.CharField(u'Imię odbiorcy', max_length=50)
    transfer_receiver_lastname = models.CharField(u'Nazwisko odbiorcy', max_length=50)
    transfer_receiver_account_number = models.CharField(u'Nr konta odbiorcy', max_length=50)
    transfer_amount = models.IntegerField(u'Kwota transakcji', default=0.01)
    transfer = models.DateField('Data przelewu', auto_now_add=True, blank=True)
    balance_before_transfer = models.IntegerField('Stan przed transakcją')
    balance_after_transfer = models.IntegerField('Stan po transakcji')
    transaction_counter = models.IntegerField(u'Licznik transakcji', default=0)




