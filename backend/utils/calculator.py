def calculate_volume(length, width, height):
    """Returns volume in cubic cm"""
    return round(length * width * height, 2)

def calculate_efficiency(used_volume, box_volume):
    """Returns how efficiently a box is filled"""
    if box_volume == 0:
        return 0
    return round((used_volume / box_volume) * 100, 2)

def calculate_co2_saved(original_volume, optimized_volume):
    """Returns estimated CO₂ saved based on space saved (mock logic)"""
    saved_volume = original_volume - optimized_volume
    if saved_volume <= 0:
        return 0
    return round(saved_volume * 0.015, 2)  # Example: 0.015g CO₂ saved per cm³ saved
