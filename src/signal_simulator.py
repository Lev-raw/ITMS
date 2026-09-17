class SignalSimulator:
    def __init__(self):
        """
        Initialize default signal timings.
        """

        self.timings = {
            "Low": 20,
            "Medium": 40,
            "High": 60
        }

    def calculate_green_time(self, congestion_level):
        """
        Calculate green signal duration based on congestion.
        """

        return self.timings.get(congestion_level, 20)

    def get_signal_status(self, congestion_level):
        """
        Return signal information for the current congestion level.
        """

        green_time = self.calculate_green_time(congestion_level)

        return {
            "congestion": congestion_level,
            "green_time": green_time,
            "status": f"Green signal recommended for {green_time} seconds"
        }