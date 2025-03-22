from PIL import Image
import qrcode
import random
input = input("Add your URL:")

# Create a QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Define the data to be encoded in the QR code
data = f"{input}"

# Add the data to the QR code object
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Open the logo or image file
logo = Image.open("logo2.png")

# Resize the logo or image if needed
logo = logo.resize((60, 60))

# Position the logo or image in the center of the QR code
img_w, img_h = img.size
logo_w, logo_h = logo.size
pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)

# Paste the logo or image onto the QR code
img.paste(logo, pos)
# Make random num for fime name
number = "".join(random.choice("0123456789")for e in range(6))
# Save the QR code image with logo or image
img.save(f"QRcode-IMG/QRCODE-ST-{number}.png")