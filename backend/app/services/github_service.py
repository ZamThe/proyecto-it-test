import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_github_user(username: str):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 404:
            return {
                "error": "Usuario no encontrado"
            }

        elif response.status_code == 401:
            return {
                "error": "Token inválido o expirado"
            }

        else:
            return {
                "error": f"Error {response.status_code}",
                "details": response.text
            }

    except requests.exceptions.RequestException as e:
        return {
            "error": "No fue posible conectar con GitHub",
            "details": str(e)
        }