from codecarbon import EmissionsTracker

class CarbonTracker:
    def __init__(self):
        self.tracker = EmissionsTracker(output_dir=".", save_to_file=True)

    def start(self):
        self.tracker.start()

    def stop(self):
        emissions = self.tracker.stop()
        return emissions
