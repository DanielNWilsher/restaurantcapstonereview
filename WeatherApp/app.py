from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    weather_data = fetch_weather_data(city)
    if weather_data:
        return render_template('result.html', weather=weather_data, city=city)
    else:
        return render_template('index.html', error="City not found")

def fetch_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
