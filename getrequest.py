import requests

url = "https://api.api-ninjas.com/v1/passwordgenerator?length=16r"

headers = {
    "X-Api-Key": "ywT0cjINTPWXfaXYF0h8FA==rULJGQLhnCjjDpPw" 
}

params = {
    "length": 20,  # Adjust length as needed
    "exclude_numbers": False,
    "exclude_special_chars": False
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    password = data.get('password')
    print(f"Generated Password: {password}")
else:
    print(f"Error: {response.status_code}")