class MissionHandler:
    def show_missions(self, count):
        try:
            count = int(count)
        except ValueError:
            print("Invalid mission. Please enter a number")
            return

        if count < 0:
            print("Mission Count cannot be negative.")
            return

        print("\n-----MISSION PROGRESS-----")
        for i in range(1, count + 1):
            print(f"Mission {i} completed")