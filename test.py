import base64

# URL to be encoded
url = "info@erik-skopp.de"

# Encoding the URL to base64
encoded_url = base64.b64encode(url.encode()).decode()
print(encoded_url)