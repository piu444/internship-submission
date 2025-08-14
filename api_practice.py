import requests
# def request():
#     url = "https://api.freeapi.app/api/v1/public/randomusers"
#     requests.get(url)
#     response = requests.get(url)
#     data= response.json()
    
#     if data["success"] and "data" in data:
#         users = data["data"]
#         print(f"✅ {len(users)} users retrieved successfully.")
#         return users
#     else:

#         raise Exception("❌ Failed to retrieve users or no data found.")
    
    
# def main():
#     try:
#         users = request()
#         for user in users:
#             print(f"Name: {user['name']}, Email: {user['email']}")
#     except Exception as e:
#         print(e)
        
# if __name__ == "__main__":
#     main()   



import requests

def random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"    
    response = requests.get(url)
    data = response.json()

    # For debugging - to understand the structure
    # print(data)

    if data["success"] and "data" in data:
        joke_data = data["data"]

        # Safely retrieve the joke content
        content = joke_data.get("content")  # This is usually the main joke text
        return content
    else:
        raise Exception("❌ Failed to retrieve jokes or no data found.")

def main():
    try:
        content = random_jokes()
        print(f"✅ Joke retrieved successfully:\n{content}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
