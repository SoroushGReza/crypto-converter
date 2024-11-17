from django.urls import path
from .views import CryptoPriceView, ConvertCryptoView, CryptoListView

urlpatterns = [
    path("price/<str:symbol>/", CryptoPriceView.as_view(), name="crypto-price"),
    path("convert/<str:symbol>/", ConvertCryptoView.as_view(), name="convert-crypto"),
    path("cryptos/", CryptoListView.as_view(), name="crypto-list"),
]
