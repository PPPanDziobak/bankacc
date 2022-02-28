from django import forms
from django.forms import CharField
import random

from .models import Account, Transfer


def generate_numbers():
    number = random.randint(100000, 999999)
    return str(number)


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.PasswordInput()


class CreateAccountForm(forms.ModelForm):
    # account_number = CharField(widget=generate_numbers(), required=True)
    # credit_card = CharField(widget=generate_numbers(), required=True)

    class Meta:
        model = Account
        exclude = ('balance', )


class TransferForm(forms.ModelForm):

    class Meta:
        model = Transfer
        exclude = ('balance_before_transfer', 'balance_after_transfer', 'transaction_counter')


