import requests
import schedule
import time
import random
import os

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
STEAM_API_URL = 'https://store.steampowered.com/api/appdetails'
STEAM_APP_LIST_URL = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'

EMOJIS = {
    "money": "💰",
    "discount": "🛒",
    "game": "🎮",
    "link": "🔗"
}

app_list = []

def get_app_list():
    global app_list
    try:
        response = requests.get(STEAM_APP_LIST_URL)
        if response.status_code == 200:
            data = response.json()
            app_list = data['applist']['apps']
            print(f"Lista de apps carregada com {len(app_list)} jogos.")
        else:
            print(f"Erro ao buscar lista de apps: {response.status_code}")
    except Exception as e:
        print(f"Erro ao buscar lista de apps: {e}")

def get_game_details(app_id):
    try:
        params = {
            'appids': app_id,
            'cc': 'br',
            'l': 'pt',
        }
        response = requests.get(STEAM_API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if data and str(app_id) in data and data[str(app_id)]['success']:
                return data[str(app_id)]['data']
        return None
    except Exception as e:
        print(f"Erro ao buscar detalhes do jogo {app_id}: {e}")
        return None

def send_discord_webhook(embed):
    data = {
        "embeds": [embed]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=data, headers=headers)
    if response.status_code == 204:
        print("Mensagem enviada com sucesso para o Discord!")
    else:
        print(f"Erro ao enviar mensagem para o Discord: {response.status_code}")
        print(f"Resposta do Discord: {response.text}")

def check_and_send_deal():
    global app_list
    if not app_list:
        print("Carregando lista de apps...")
        get_app_list()
        if not app_list:
            print("Nenhum jogo encontrado na lista de apps.")
            return

    random_game = random.choice(app_list)
    app_id = random_game['appid']
    print(f"Buscando detalhes do jogo {app_id}...")
    game_details = get_game_details(app_id)
    if game_details and 'price_overview' in game_details:
        price_overview = game_details['price_overview']
        name = game_details.get('name', 'Nome desconhecido')
        original_price = price_overview.get('initial_formatted', 'N/A')
        discount_price = price_overview.get('final_formatted', 'N/A')
        discount_percent = price_overview.get('discount_percent', 0)
        game_url = f"https://store.steampowered.com/app/{app_id}"

        embed = {
            "title": f"{EMOJIS['game']} {name}",
            "url": game_url,
            "description": f"{EMOJIS['money']} **Preço Original:** {original_price}\n"
                           f"{EMOJIS['discount']} **Preço com Desconto:** {discount_price}\n"
                           f"🎉 **Desconto:** {discount_percent}%",
            "color": 0x00ff00,
            "thumbnail": {"url": game_details.get('header_image', 'https://cdn.akamai.steamstatic.com/store/home/store_home_share.jpg')}
        }

        send_discord_webhook(embed)
    else:
        print("Nenhum detalhe encontrado para o jogo selecionado.")


get_app_list()

check_and_send_deal()

schedule.every(1).minutes.do(check_and_send_deal)

while True:
    schedule.run_pending()
    time.sleep(1)