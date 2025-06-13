from wifi_qrcode_generator.generator import wifi_qrcode
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

# Wi-Fi credentials
ssid = "MOVISTAR-WIFI6-9390"
password = os.getenv("WIFI_PASSWORD")
security = "WPA"  # Use "WPA" instead of "WPA2-PSK"

# Generate the QR code
qr = wifi_qrcode(ssid, hidden=False, authentication_type=security, password=password)

# Save the image
qr_path = os.path.join(os.getcwd(), "wifi_qr.png")
qr.make_image().save(qr_path)

# Open and display the image
img = Image.open(qr_path)
img.show()