import qrcode
import os

# Folder to save QR images
QR_FOLDER = os.path.join("static", "qrcodes")
os.makedirs(QR_FOLDER, exist_ok=True)

def generate_qr_code(box_id):
    """
    Generate a QR code that links to a summary page for the given box.
    Returns the relative path to the image.
    """
    # URL could point to a summary endpoint (if hosted)
    qr_text = f"http://127.0.0.1:5000/summary/{box_id}"

    img = qrcode.make(qr_text)
    qr_path = os.path.join(QR_FOLDER, f"qr_{box_id}.png")
    img.save(qr_path)

    # Return relative URL to the frontend
    return f"/static/qrcodes/qr_{box_id}.png"
