import urllib.parse

password = '175@#Mt8'
encoded_password = urllib.parse.quote(password)
print(encoded_password)