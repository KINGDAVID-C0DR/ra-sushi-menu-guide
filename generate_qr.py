# Run: python -m pip install qrcode[pil]
# Then: python generate_qr.py
import qrcode
url=input("Enter the published HTTPS menu website URL: ").strip()
if not url.startswith("https://"):
    raise SystemExit("Please provide the final https:// website URL")
q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=14,border=4)
q.add_data(url);q.make(fit=True);q.make_image(fill_color="black",back_color="white").save("RA_Sushi_Menu_QR.png")
print("Created RA_Sushi_Menu_QR.png")
