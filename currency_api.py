import requests

def convert_currency(amount, from_currency, to_currency):
    try:
        # Normalize currency codes
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        # API endpoint
        url = "https://api.frankfurter.app/latest"
        params = {
            "amount": amount,
            "from": from_currency,
            "to": to_currency
        }

        response = requests.get(url, params=params)
        print(f"[CurrencyAPI] URL: {response.url}")

        if response.status_code != 200:
            return f"❌ API error: {response.status_code}"

        data = response.json()
        print(f"[CurrencyAPI] Response JSON: {data}")

        # Check if 'rates' and target currency exist
        if "rates" not in data or to_currency not in data["rates"]:
            return f"❌ Conversion from '{from_currency}' to '{to_currency}' not supported."

        result = data["rates"][to_currency]
        return f"{amount} {from_currency} = {result:.2f} {to_currency}"

    except Exception as e:
        return f"⚠️ Currency conversion failed: {str(e)}"
