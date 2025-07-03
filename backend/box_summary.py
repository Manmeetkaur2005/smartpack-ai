from flask import Blueprint, render_template_string

summary_bp = Blueprint("summary", __name__)

@summary_bp.route("/summary/<int:box_id>")
def show_summary(box_id):
    # You can fetch actual box details from the database using box_id
    # For now, this is a mock summary:
    summary_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Box Summary</title>
        <style>
            body {{ font-family: Arial; background: #f4f4f4; padding: 20px; }}
            .box {{ background: white; padding: 20px; border-radius: 8px; max-width: 500px; margin: auto; }}
            h1 {{ color: #1e40af; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>📦 Box Summary</h1>
            <p><strong>Box ID:</strong> {box_id}</p>
            <p><strong>Contents:</strong> Sample items packed using SmartPack AI</p>
            <p><strong>Efficiency:</strong> 87%</p>
            <p><strong>CO₂ Saved:</strong> 124g</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(summary_html)
