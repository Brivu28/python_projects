import requests
import sqlite3
import time

# Replace with your actual API keys
WEATHER_API_KEY = 'your_actual_openweathermap_api_key'
NEWS_API_KEY = 'your_actual_newsapi_api_key'

# Database setup
def create_connection():
    conn = sqlite3.connect('weather_news.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY,
            city TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_search(city):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO searches (city) VALUES (?)', (city,))
    conn.commit()
    conn.close()

# Weather API integration
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# News API integration
def get_news():
    url = f'http://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['articles'][:5]  # Get top 5 headlines
    except requests.RequestException as e:
        print(f"Error fetching news data: {e}")
        return None

# Main application logic
def main():
    create_tables()
    while True:
        city = input("Enter city name for weather info (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        weather = get_weather(city)
        if weather:
            save_search(city)
            print(f"City: {weather['city']}")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Weather: {weather['description']}")
        else:
            print("Could not fetch weather data. Please try again.")
        
        print("\nTop News Headlines:")
        news = get_news()
        if news:
            for i, article in enumerate(news):
                print(f"{i+1}. {article['title']}")
                print(f"   {article['description']}")
                print(f"   {article['url']}")
        else:
            print("Could not fetch news data. Please try again.")

if __name__ == "__main__":
    main()
