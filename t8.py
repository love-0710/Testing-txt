import time
import pyautogui
import json
import tkinter as tk

class TinyTaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TinyTask Clone")

        # UI Elements
        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Recording", command=self.stop_recording)
        self.stop_button.pack()

        self.play_button = tk.Button(root, text="Play Recording", command=self.play_recording)
        self.play_button.pack()

        self.recorded_actions = []  # List to store recorded actions
        self.is_recording = False

    def start_recording(self):
        self.is_recording = True
        self.recorded_actions = []  # Clear previous recordings
        self.record_actions()

    def stop_recording(self):
        self.is_recording = False
        print("Recording stopped!")

    def record_actions(self):
        while self.is_recording:
            # Record Mouse Position
            x, y = pyautogui.position()
            self.recorded_actions.append({'type': 'move', 'x': x, 'y': y, 'timestamp': time.time()})

            # Record Mouse Clicks
            if pyautogui.mouseInfo() is not None:
                button = pyautogui.mouseInfo().button
                action_type = 'press'  # Could add release logic here too
                self.recorded_actions.append({'type': 'click', 'x': x, 'y': y, 'button': button, 'action': action_type, 'timestamp': time.time()})

            # Record Keyboard Input (use pyautogui type function to type out keys)
            # For example, press keys, add a mechanism to capture keypresses
            
            time.sleep(0.1)  # Delay for better recording experience

    def play_recording(self):
        start_time = self.recorded_actions[0]['timestamp']
        for action in self.recorded_actions:
            timestamp = action['timestamp']
            delay = timestamp - start_time
            time.sleep(delay)

            if action['type'] == 'move':
                pyautogui.moveTo(action['x'], action['y'])
            elif action['type'] == 'click':
                pyautogui.click(action['x'], action['y'])

        print("Playback finished!")

    def save_recording(self):
        with open("recording.json", "w") as f:
            json.dump(self.recorded_actions, f)

    def load_recording(self):
        with open("recording.json", "r") as f:
            self.recorded_actions = json.load(f)


# Set up the main window
root = tk.Tk()
app = TinyTaskApp(root)
root.mainloop()