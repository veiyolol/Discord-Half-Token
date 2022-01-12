import base64

halftoken = base64.b64encode(input("UserID: ").encode()).decode()

print(f"{halftoken}.{'x'*6}.{'x'*27}")
