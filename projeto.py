

import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "pt_br"
    }
    response = requests.get(base_url, params=params)
    return response.json()

def show_weather():
    city = city_entry.get()
    api_key = "dcff7686f26776979302c03866346d58"
    weather_data = get_weather(city, api_key)

    if weather_data["cod"] == 200:
        main_weather = weather_data["main"]
        weather_description = weather_data["weather"][0]["description"]

        result_text = (
            f"Temperatura: {main_weather['temp']}°C\n"\
            f"Pressão: {main_weather['pressure']} hPa\n"\
            f"Umidade: {main_weather['humidity']}%\n"\
            f"Descrição: {weather_description}"
        )
    elif weather_data["cod"] == "404":
        result_text = "Cidade não encontrada!"
    else:
        result_text = f"Erro: {weather_data['message']}"

    result_label.config(text=result_text)

app = tk.Tk()
app.title("Previsão do Tempo")
app.geometry("800x400")  # Aumenta o tamanho da janela

font = ("Verdana", 20)  # Define a fonte e o tamanho da letra

tk.Label(app, text="Digite o nome da cidade:", font=font).pack(pady=5)
city_entry = tk.Entry(app, font=font)
city_entry.pack(pady=6)

tk.Button(app, text="Obter Previsão", command=show_weather, font=font).pack(pady=5)

result_label = tk.Label(app, text="", wraplength=300, font=font)  # Adiciona o rótulo para exibir os resultados
result_label.pack(pady=10)

app.mainloop()

