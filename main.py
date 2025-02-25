import requests
import schedule
import time
import random

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1344045495055683644/IF13aML6QZ2qiQCsXtOSmtGbxmPFxt0FPuQXknzDH6C4Io04mja7nsRkRAyO5I8BxpOW'
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
        # Faz a requisição à API da Steam
        params = {
            'appids': app_id,
            'cc': 'br',  # Código do país (Brasil)
            'l': 'pt',   # Idioma (Português)
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
    # Payload do webhook
    data = {
        "embeds": [embed]
    }

    # Cabeçalhos
    headers = {
        "Content-Type": "application/json"
    }

    # Envia o webhook
    response = requests.post(DISCORD_WEBHOOK_URL, json=data, headers=headers)

    # Verifica a resposta
    if response.status_code == 204:
        print("Mensagem enviada com sucesso para o Discord!")
    else:
        print(f"Erro ao enviar mensagem para o Discord: {response.status_code}")
        print(f"Resposta do Discord: {response.text}")  # Mostra a resposta do Discord para depuração

def check_and_send_deal():
    global app_list
    if not app_list:
        print("Carregando lista de apps...")
        get_app_list()
        if not app_list:
            print("Nenhum jogo encontrado na lista de apps.")
            return

    # Seleciona um jogo aleatoriamente
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

        # Cria um embed para o jogo
        embed = {
            "title": f"{EMOJIS['game']} {name}",
            "url": game_url,
            "description": f"{EMOJIS['money']} **Preço Original:** {original_price}\n"
                           f"{EMOJIS['discount']} **Preço com Desconto:** {discount_price}\n"
                           f"🎉 **Desconto:** {discount_percent}%",
            "color": 0x00ff00,  # Cor verde
            "thumbnail": {"url": game_details.get('header_image', 'https://cdn.akamai.steamstatic.com/store/home/store_home_share.jpg')}  # Imagem do jogo
        }

        # Envia o embed para o Discord
        send_discord_webhook(embed)
    else:
        print("Nenhum detalhe encontrado para o jogo selecionado.")

# Carrega a lista de apps ao iniciar o script
get_app_list()

# Agendar a execução a cada 5 minutos
schedule.every(1).minutes.do(check_and_send_deal)

# Loop para manter o script rodando
while True:
    schedule.run_pending()
    time.sleep(1)