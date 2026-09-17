from signal_simulator import SignalSimulator


def main():
    simulator = SignalSimulator()

    congestion_levels = [
        "Low",
        "Medium",
        "High"
    ]

    for level in congestion_levels:
        result = simulator.get_signal_status(level)

        print(f"Congestion: {result['congestion']}")
        print(f"Green time: {result['green_time']} seconds")
        print(f"Status: {result['status']}")
        print("-" * 40)


if __name__ == "__main__":
    main()