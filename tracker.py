from codecarbon import EmissionsTracker

class CarbonTracker:
    def __init__(self):
        self.tracker = None

    def start(self):
        self.tracker = EmissionsTracker(
            output_dir=".", 
            save_to_file=False,  # Disable file saving for web app
            measure_power_secs=1,
            log_level="ERROR"
        )
        self.tracker.start()

    def stop(self):
        if self.tracker:
            emissions = self.tracker.stop()
            # CodeCarbon returns the emissions value directly
            return emissions if emissions is not None else 0.0
        return 0.0