import requests
from rich import print
from rich.console import Console

params = {
    
}

r = requests.get("https://api.opensea.io/api/v1/assets")

print(r.json())