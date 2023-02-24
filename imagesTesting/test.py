import requests

access_token = "EAARLFM5Skx0BAOx9sjuSyG7J4iRbP4aZAvRU1oXGmLGBMHD29iIZA1xo1EhOXe2gjPUI6dTASCewjMhJ7ZA1KQxZAz8NDpG8ez5jaGfSUdcx5twKFPa7XCZB9mhW63kG7Qo0NSVj64XzUytXVjVCksjQYDX4ge5jbIFbahcIi4lpiejQRsfCPCzHKZAD4f2yAiE3oseWZCKehQEH5WpNFqf"

recipient_id = "recipient_id"

message = "Hello World!"

url = f"https://graph.facebook.com/v7.0/{recipient_id}/messages?access_token={access_token}"

payload = {"message": message}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("Message sent successfully")
else:
    print("Failed to send message")