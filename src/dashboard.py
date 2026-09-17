import cv2


def draw_dashboard(
    frame,
    vehicle_count,
    congestion_level,
    green_time,
    fps,
    processed_frames
):
    """
    Draw the ITMS dashboard on the video frame.
    """

    panel_width = 390
    panel_height = 235

    # Create a dark transparent panel
    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (10, 10),
        (panel_width, panel_height),
        (20, 20, 20),
        -1
    )

    cv2.addWeighted(
        overlay,
        0.75,
        frame,
        0.25,
        0,
        frame
    )

    # Dashboard title
    cv2.putText(
        frame,
        "ITMS Dashboard",
        (25, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # Vehicle count
    cv2.putText(
        frame,
        f"Vehicles: {vehicle_count}",
        (25, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    # Congestion color
    if congestion_level == "Low":
        congestion_color = (0, 255, 0)

    elif congestion_level == "Medium":
        congestion_color = (0, 165, 255)

    else:
        congestion_color = (0, 0, 255)

    # Congestion level
    cv2.putText(
        frame,
        f"Congestion: {congestion_level}",
        (25, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        congestion_color,
        2
    )

    # Recommended green time
    cv2.putText(
        frame,
        f"Green Time: {green_time} sec",
        (25, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # FPS
    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (25, 195),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Processed frames
    cv2.putText(
        frame,
        f"Frames: {processed_frames}",
        (210, 195),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    return frame