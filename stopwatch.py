import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.running = False
# to start the watch
    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            print("Stopwatch started...")
        else:
            print("Stopwatch is already running.")
# to stop the watch

    def stop(self):
        if self.running:
            self.end_time = time.time()
            self.running = False
            print("Stopwatch stopped.")
        else:
            print("Stopwatch is not running.")
# reset watch here
    def reset(self):
        self.start_time = None
        self.end_time = None
        self.running = False
        print("Stopwatch reset.")

    def elapsed_time(self):
        if self.running:
            elapsed = time.time() - self.start_time
            return elapsed
        elif self.start_time and self.end_time:
            elapsed = self.end_time - self.start_time
            return elapsed
        else:
            return 0


    def display_time(self):
        elapsed = self.elapsed_time()
        minutes, seconds = divmod(elapsed, 60)
        hours, minutes = divmod(minutes, 60)
        print(f"Elapsed Time: {int(hours):02}:{int(minutes):02}:{int(seconds):02}")


if __name__ == "__main__":
    stopwatch = Stopwatch()
    while True:
        print("Commands: start, stop, reset, time, exit")
        command = input("Enter command: ").strip().lower()
        if command == "start":
            stopwatch.start()
        elif command == "stop":
            stopwatch.stop()
        elif command == "reset":
            stopwatch.reset()
        elif command == "time":
            stopwatch.display_time()
        elif command == "exit":
            break
        else:
            print("Invalid command.")









