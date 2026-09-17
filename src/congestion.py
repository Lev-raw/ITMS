def estimate_congestion(vehicle_count):
    """
    Estimate congestion based on the number of visible vehicles.

    These thresholds are simple MVP rules.
    They can be adjusted according to the video and camera angle.
    """

    if vehicle_count <= 3:
        return "Low"

    elif vehicle_count <= 7:
        return "Medium"

    else:
        return "High"