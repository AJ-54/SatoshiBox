import requests
from django.shortcuts import get_object_or_404
from .models import Product
from django.conf import settings


base_url = "https://www.blockonomics.co/api"
headers = {"Authorization": "Bearer " + settings.BLOCKONOMICS_KEY}
conversion = {"BTC": lambda currency: f"{base_url}/price?currency={currency}"}


def exchanged_rate(amount, crypto, currency) -> float:
    url = conversion[crypto](currency)
    r = requests.get(url)
    response = r.json()
    return round(pow(10, 8) * amount / response["price"])

def exchanged_rate_to_usd(amount, crypto, currency) -> float:
    url = conversion[crypto](currency)
    r = requests.get(url)
    response = r.json()
    return round (amount * response["price"], 2)


def create_payment(product, crypto):
    url = f"{base_url}/new_address"
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    address = response.json()["address"]
    price = exchanged_rate(product.price, crypto, product.currency)/pow(10, 8)

    return address, price
