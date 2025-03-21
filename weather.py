from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = "d9825e08808cd390eb6b76991dc78a7b"

def get_weather(location):
    # URL to fetch weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]
        
        # Full weather details to be returned
        return {
            "location": location.capitalize(),
            "description": weather["description"],
            "temperature": main["temp"],
            "humidity": main["humidity"],
            "pressure": main["pressure"],
            "wind_speed": wind["speed"],
            "wind_deg": wind["deg"],
            "content": generate_content(weather["description"], main["temp"]),
        }
    else:
        return None

def generate_content(description, temperature):
    """Generate custom content based on the weather description and temperature."""
    if "clear" in description:
        return f"The weather is clear with a nice temperature of {temperature}°C. Perfect for outdoor activities!"
    elif "cloud" in description:
        return f"There are a few clouds in the sky with a pleasant {temperature}°C. It's a good day to relax."
    elif "rain" in description:
        return f"It's raining, and the temperature is {temperature}°C. Don't forget your umbrella!"
    elif "snow" in description:
        return f"Snow is falling, with a temperature of {temperature}°C. Perfect weather to enjoy some hot cocoa!"
    elif "storm" in description:
        return f"A storm is brewing with a temperature of {temperature}°C. Stay safe and indoors."
    else:
        return f"The weather is {description} with a temperature of {temperature}°C. Be prepared!"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location = request.form["location"]
        weather_data = get_weather(location)
        if weather_data:
            return render_template("index.html", weather=weather_data)
        else:
            return render_template("index.html", weather=None)

    return render_template("index.html", weather=None)

if __name__ == "__main__":
    app.run(debug=True)
