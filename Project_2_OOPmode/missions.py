class MissionHandler:
    def show_missions(self, count):
        print("\n-----MISSION PROGRESS-----")
        for i in range(1, count + 1):
            print(f"Mission {i} completed")