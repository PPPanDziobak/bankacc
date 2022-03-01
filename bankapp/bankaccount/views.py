from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
    View
)
from .models import Account, Transfer
from .forms import CreateAccountForm, TransferForm


class HomeView(View):

    template_name = 'bankaccount/home.html'

    def get(self, request):

        return render(request, self.template_name)


class LoginView(View):
    template_name = 'bankaccount/login.html'

    def login_user(self, request):

        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('account-details')

            else:
                return redirect('login')
        else:
            return render(request, self.template_name)


class AccountCreateView(CreateView):

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


class AccountDetailView(DetailView):

    template_name = 'bankaccount/my-account.html'

    def get_object(self):
        balance = self.kwargs.get('balance')
        return get_object_or_404(Account, balance=balance)


class TransferHistoryView(View):
    template_name = 'bankaccount/transfer-history.html'
    queryset = Transfer.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwrgs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


class TransferView(View):
    template_name = 'bankaccount/transfer.html'

    def get(self, request, *args, **kwargs):

        form = TransferForm()
        context = {'form': form}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = TransferForm(request.POST)

        if form.is_valid():
            form.save()
            form = TransferForm()
        context = {'form': form}

        return render(request, self.template_name, context)



























class NextView(View):
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

