from django.db import models


class CreditCard(models.Model):
    card_number = models.CharField(u'Numer karty', max_length=10)
    expiration_date = models.DateField(u'Data ważności')
    cvc_number = models.CharField(u'Numer CVC', max_length=3)


# class Account(models.Model):
#     account_number = models.CharField(u'Numer konta', max_length=12)
#     balance = models.IntegerField(u'Stan konta')
#     credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)


class Account(models.Model):
    firstname = models.CharField(u'Imię', max_length=50, blank=True)
    lastname = models.CharField(u'Nazwisko', max_length=50, blank=True)
    email = models.EmailField(u'Email', max_length=50, blank=True)
    phone = models.CharField(u'Telefon', max_length=12, blank=True)
    address = models.CharField(u'Adres', max_length=250, blank=True)
    city = models.CharField(u'Miasto', max_length=250, blank=True)
    country = models.CharField(u'Kraj', max_length=250, blank=True)
    date_of_birth = models.DateField(u'Data urodzenia', auto_now_add=True, blank=True)
    account_number = models.CharField(u'Numer konta', max_length=12, blank=False)
    balance = models.IntegerField(u'Stan konta')
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)


class Transfer(models.Model):
    transfer_receiver_firstname = models.CharField(u'Imię odbiorcy', max_length=50)
    transfer_receiver_lastname = models.CharField(u'Nazwisko odbiorcy', max_length=50)
    transfer_receiver_account_number = models.CharField(u'Nr konta odbiorcy', max_length=50)
    transfer_amount = models.IntegerField(u'Kwota transakcji', default=0.01)
    transfer_date = models.DateField('Data przelewu', auto_now_add=True, blank=True)
    balance_before_transfer = models.IntegerField('Stan przed transakcją')
    balance_after_transfer = models.IntegerField('Stan po transakcji')
    transaction_counter = models.IntegerField(u'Licznik transakcji', default=0)


class CardPayment(models.Model):
    payment_amount = models.IntegerField('Kwota transakcji', default=0.00)
    payment_date = models.DateField('Data transakcji', auto_now_add=True, blank=True)
    payments_counter = models.IntegerField(u'Licznik transakcji', default=0)





