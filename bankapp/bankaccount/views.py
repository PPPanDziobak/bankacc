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
from .forms import CreateAccountForm, LoginForm, TransferForm


class HomeView(View):

    template_name = 'bankaccount/home.html'

    def get(self, request):

        return render(request, self.template_name)


class LoginView(View):
    template_name = 'bankaccount/login.html'

    def get(self, request, **kwargs):
        form = LoginForm()
        context = {'form': form}

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        form = LoginForm()
        context = {'form': form}

        return render(request, self.template_name, context)

    def login_user(self, request, **kwargs):

        if request.method == 'POST':
            form = LoginForm()

            context = {'form': form}

            # email = request.POST['email']
            # password = request.POST['password']

            user = authenticate(request, context)

            if user is not None:
                login(request, user)
                return redirect('https://wp.pl')
                # return redirect('account-details')

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

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Account, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)


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

