import qrcode
from PIL import Image

name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ")
info = input("Enter any extra info or website: ")

data = f"""
Name: {name}
Phone: {phone}
Email: {email}
Info: {info}
"""

qr = qrcode.make(data)
qr.save("my_qr_code.png")

# Open the QR image automatically
img = Image.open("my_qr_code.png")
img.show()

print("QR Code generated and displayed successfully!")
