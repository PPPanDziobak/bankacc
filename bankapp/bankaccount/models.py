from django.db import models

import random


class CreditCard(models.Model):
    card_number = models.CharField(u'Numer karty', max_length=10)
    expiration_date = models.DateField(u'Data ważności', auto_now_add=True)
    cvc_number = models.CharField(u'Numer CVC', max_length=3)
    payment_amount = models.IntegerField('Kwota transakcji', default=0.00)
    payment_date = models.DateField('Data transakcji', auto_now_add=True, blank=True)
    payments_counter = models.IntegerField(u'Licznik transakcji', default=0)
    pin_number = models.CharField(u'Kod pin', max_length=4, default=1234)

    def __str__(self):
        return self.card_number

    def get_card_number(self):
        card_number = random.randint(100000, 999999)
        return card_number

    def save(self, *args, **kwargs):
        self.account_number = self.get_card_number()
        super(CreditCard, self).save(*args, **kwargs)


class Account(models.Model):
    firstname = models.CharField(u'Imię', max_length=50, blank=True)
    lastname = models.CharField(u'Nazwisko', max_length=50, blank=True)
    email = models.EmailField(u'Email', max_length=50, blank=True)
    password = models.CharField(u'Hasło', max_length=12, blank=True)
    phone = models.CharField(u'Telefon', max_length=12, blank=True)
    address = models.CharField(u'Adres', max_length=250, blank=True)
    city = models.CharField(u'Miasto', max_length=250, blank=True)
    country = models.CharField(u'Kraj', max_length=250, blank=True)
    date_of_birth = models.DateField(u'Data urodzenia', auto_now_add=True, blank=True)
    account_number = models.CharField(u'Numer konta', max_length=12, blank=False)
    balance = models.IntegerField(u'Stan konta')
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number

    def get_account_number(self):
        account_number = random.randint(100000, 999999)
        return str(account_number)

    def save(self, *args, **kwargs):
        self.account_number = self.get_account_number()
        super(Account, self).save(*args, **kwargs)


class Transfer(models.Model):
    transfer_title = models.CharField(u'Tytuł przelewu', max_length=50, default='Przelew środków')
    transfer_receiver_firstname = models.CharField(u'Imię odbiorcy', max_length=50)
    transfer_receiver_lastname = models.CharField(u'Nazwisko odbiorcy', max_length=50)
    transfer_receiver_account_number = models.CharField(u'Nr konta odbiorcy', max_length=5)
    transfer_amount = models.IntegerField(u'Kwota transakcji', default=0.01)
    transfer_date = models.DateField('Data przelewu', auto_now_add=True, blank=True)
    balance_before_transfer = models.IntegerField('Stan przed transakcją')
    balance_after_transfer = models.IntegerField('Stan po transakcji')
    transaction_counter = models.IntegerField(u'Licznik transakcji', default=0)



