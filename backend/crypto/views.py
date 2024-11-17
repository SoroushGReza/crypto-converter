import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer


class CryptoPriceView(APIView):
    def get(self, request, *args, **kwargs):
        coin = self.kwargs.get("symbol").lower()
        url_price = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        try:
            response_price = requests.get(url_price).json()
            price_usd = response_price[coin]["usd"]
            return Response(
                {"symbol": coin, "price_usd": price_usd}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ConvertCryptoView(APIView):
    def get(self, request, *args, **kwargs):
        coin = self.kwargs.get("symbol").upper()
        amount = request.query_params.get("amount", "1").replace(
            ",", "."
        )  # Replace ',' with '.'

        # Validate ammount
        try:
            amount = float(amount)
        except ValueError:
            return Response(
                {"error": "Invalid amount. Please use numbers like 2.5 or 2,5."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Fetch `coingecko_id` for symbol from database
            crypto = Cryptocurrency.objects.get(symbol=coin)
            coingecko_id = crypto.coingecko_id

            # Fetch crypto price
            url_price = f"https://api.coingecko.com/api/v3/simple/price?ids={coingecko_id}&vs_currencies=usd"
            response_price = requests.get(url_price).json()

            if coingecko_id not in response_price:
                return Response(
                    {"error": "Invalid cryptocurrency or data not available."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            price_usd = response_price[coingecko_id]["usd"]

            # Fetch exchange rate
            url_rate = "https://api.exchangerate-api.com/v4/latest/USD"
            response_rate = requests.get(url_rate).json()

            if "rates" not in response_rate:
                return Response(
                    {"error": "Failed to fetch exchange rates."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            rates = response_rate["rates"]

            # Perform conversion
            usd_value = amount * price_usd
            eur_value = usd_value * rates.get("EUR", 1)
            sek_value = usd_value * rates.get("SEK", 1)

            return Response(
                {
                    "crypto": coin,
                    "amount": amount,
                    "usd": round(usd_value, 2),
                    "eur": round(eur_value, 2),
                    "sek": round(sek_value, 2),
                },
                status=status.HTTP_200_OK,
            )
        except Cryptocurrency.DoesNotExist:
            return Response(
                {"error": f"No cryptocurrency found for symbol {coin}."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CryptoListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            cryptos = Cryptocurrency.objects.all()
            serializer = CryptocurrencySerializer(cryptos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
