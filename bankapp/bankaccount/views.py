from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
    View
)
from .models import Account, Transfer
from .forms import CreateAccountForm


class HomeView(View):

    template_name = 'bankaccount/home.html'

    def get(self, request):

        return render(request, self.template_name)


class AccountCreateView(View):

    template_name = 'bankaccount/create-account.html'

    def get(self, request, *args, **kwargs):
        form = CreateAccountForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateAccountForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class AccountDetailView(View):
    pass


class TransferHistoryView(View):
    pass


class TransferView(View):
    pass


class NextView(View):
    pass


class LoginView(View):
    pass


class AccountOperations(View):

    def deposit(self, amount):

        self.deposit += amount

    def withdraw(self, amount):

        self.deposit -= amount

    def card_payment(self, amount):

        self.deposit -= amount

    def get_account_balance(self, balance):

        account_balance = Account.objects.get(balance=balance)

        return account_balance

    def transfer(self, account_balance):

        context = {
            'transfer_to_data': {
                'firstname': Transfer.objects.get,
                'lastname': '',
                'amount': '',
            }

        }

        return context
