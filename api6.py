import requests

def get_weather():
    city = input("Enter the name of the city: ")
    API_KEY = "e525ccb2f799821191278add6deba06a"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  

        data = response.json()

        print(f"\n Weather in {city}:")
        print(f" Temperature: {data['main']['temp']}K")
        print(f"Weather: {data['weather'][0]['description']}")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(" City not found. Please check the spelling.")
        else:
            print(f" HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f" Request error: {req_err}")
    except KeyError:
        print(" Error in parsing the response data.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_weather()

    
    


