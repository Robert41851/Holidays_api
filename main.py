import requests
from dotenv import load_dotenv
import os

    
def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://calendarific.com/api/v2/holidays"
    params = {"api_key": api_key,"country": "ru", "year": 2025}
    response = requests.get(url,params=params)
    response.raise_for_status()
    holidays = response.json()["response"]["holidays"]
    months = [
        "января", 
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря"
    ]
    for holiday in holidays:
        name = holiday["name"]
        day = holiday["date"]["datetime"]["day"]
        month = holiday["date"]["datetime"]["month"]
        month = months[month-1]
        description = holiday["description"]
        print(f"""
дата: {day} {month}
название праздника: {name}
описание: {description}
""")


if __name__ == "main":
    main()
