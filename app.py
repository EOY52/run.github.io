import requests

app = Flask(__name__)
BOT_TOKEN = '5330818384:AAEOOXnCIYmA90Q0AWv6AW1yBO50OMRgsyw'  # Замените на токен вашего бота

@app.route(f'/bot{BOT_TOKEN}', methods=['POST'])
def handle_webhook():
    if request.method == 'POST':
        data = request.json
        message = data['message']
        chat_id = message['chat']['id']
        text = message.get('text', '')

        if text == '/start':
            send_message(chat_id, 'Welcome to Clicker Game! Click the coin to gain points!')

        return '', 200

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/setwebhook')
def set_webhook():
    WEBHOOK_URL = 'http://aniks.fun/'  # Замените на URL вашего веб-приложения
    response = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}')
    return response.json(), 200

if __name__ == '__main__':
    app.run(debug=True)