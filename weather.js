const getWeather = async () => {
    const city = document.getElementById("city-input").value;
    const url = `http://127.0.0.1:5000/weather?city=${city}`;
    const response = await fetch(url);
    const data = await response.json();

    if (response.ok) {
        // Display the weather data on your webpage
        document.getElementById("weather-description").textContent = `Weather: ${data.weather_message}`;
        document.getElementById("weather-temperature").textContent = `Temperature: ${data.temperature}°C`;
        document.getElementById("weather-humidity").textContent = `Humidity: ${data.humidity}%`;
        document.getElementById("weather-wind").textContent = `Wind Speed: ${data.wind_speed} m/s`;
    } else {
        // Handle error
        alert(data.error);
    }
};
 