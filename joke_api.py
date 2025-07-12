import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("error"):
            return "😅 Oops! I couldn't fetch a joke right now."

        # Handle single or two-part jokes
        if data.get("type") == "single":
            return f"😂 {data.get('joke')}"
        elif data.get("type") == "twopart":
            return f"😂 {data.get('setup')}\n👉 {data.get('delivery')}"
        else:
            return "🤔 Got a joke, but it's in an unexpected format!"

    except requests.exceptions.Timeout:
        return "⚠️ Joke service timed out. Try again later."
    except Exception:
        return "😢 Sorry, joke service is currently unavailable."
