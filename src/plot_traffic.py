import csv
import matplotlib.pyplot as plt


def read_traffic_data(file_path):
    frames = []
    vehicle_counts = []
    unique_vehicle_counts = []

    with open(
        file_path,
        mode="r",
        newline="",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            frames.append(
                int(row["frame_number"])
            )

            vehicle_counts.append(
                int(row["visible_vehicle_count"])
            )

            unique_vehicle_counts.append(
                int(row["unique_vehicle_count"])
            )

    return (
        frames,
        vehicle_counts,
        unique_vehicle_counts
    )


def main():
    file_path = "outputs/traffic_log.csv"

    (
        frames,
        vehicle_counts,
        unique_vehicle_counts
    ) = read_traffic_data(file_path)

    if not frames:
        print("No traffic data found.")
        return

    plt.figure(figsize=(10, 5))

    plt.plot(
        frames,
        vehicle_counts,
        label="Visible Vehicles"
    )

    plt.plot(
        frames,
        unique_vehicle_counts,
        label="Unique Tracking IDs"
    )

    plt.xlabel("Frame Number")
    plt.ylabel("Vehicle Count")
    plt.title("Traffic Analysis Over Time")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        "outputs/traffic_analysis.png"
    )

    plt.show()

    print(
        "Graph saved to "
        "outputs/traffic_analysis.png"
    )


if __name__ == "__main__":
    main()