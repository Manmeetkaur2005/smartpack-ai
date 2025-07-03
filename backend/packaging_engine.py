# packaging_engine.py
def suggest_box(items):
    total_volume = 0
    for item in items:
        try:
            vol = item["length"] * item["width"] * item["height"]
            total_volume += vol
        except Exception as e:
            raise ValueError("Invalid item dimensions") from e

    # Box size logic
    if total_volume <= 1000:
        box_type = "Small"
    elif total_volume <= 5000:
        box_type = "Medium"
    else:
        box_type = "Large"

    # Efficiency (arbitrary formula for now)
    efficiency = round(90 - (total_volume % 50) / 10, 2)

    # CO₂ savings mock logic
    co2_saved = int(total_volume / 10)

    return {
        "box_type": box_type,
        "efficiency": efficiency,
        "co2_saved": co2_saved
    }
