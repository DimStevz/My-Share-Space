import qrcode

# Ask the user for the text to be embedded in the QR code
text = input("Enter the text to be embedded in the QR code: ")

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls error correction (L = ~7% of the code can be restored)
    box_size=10,  # size of the boxes in the QR code
    border=4,  # thickness of the border
)
qr.add_data(text)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill="black", back_color="white")

# Ask the user for the file name
file_name = input("Enter the file name for the QR code image (without extension): ")

# Construct the full path
img_path = f"C:/Users/Dimas/Desktop/All code/Phyton/Nyoba2Gajelas/qrcode/{file_name}.png"

# Save the image
img.save(img_path)

img_path