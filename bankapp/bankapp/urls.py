# from rest_framework import routers
from django.contrib import admin
from django.urls import include, path

# from .viewsets import AccountViewset, CardViewset, TransferViewset
#
#
# router = routers.DefaultRouter()
# router.register(r'account', AccountViewset)
# router.register(r'card', CardViewset)
# router.register(r'transfer', TransferViewset)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('bankaccount.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
