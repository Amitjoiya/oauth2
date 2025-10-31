# weather-cli.py
import requests, sys

city = " ".join(sys.argv[1:]) or "Delhi"
url = f"https://wttr.in/{city}?format=3"
try:
    print(requests.get(url, timeout=5).text)
except Exception as e:
    print("Error:", e)
