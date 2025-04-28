import time
import json
import threading
from pynput.mouse import Controller, Listener as MouseListener
from pynput.keyboard import Controller as KeyboardController, Listener as KeyboardListener
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

        self.mouse_controller = Controller()
        self.keyboard_controller = KeyboardController()
        self.is_recording = False

    def start_recording(self):
        self.is_recording = True
        self.recorded_actions = []  # Clear previous recordings
        # Start Mouse and Keyboard Listeners in separate threads
        self.mouse_listener = MouseListener(on_move=self.on_move, on_click=self.on_click)
        self.keyboard_listener = KeyboardListener(on_press=self.on_press, on_release=self.on_release)

        self.mouse_listener.start()
        self.keyboard_listener.start()

    def stop_recording(self):
        self.is_recording = False
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        print("Recording stopped!")

    def on_move(self, x, y):
        if self.is_recording:
            timestamp = time.time()
            self.recorded_actions.append({'type': 'move', 'timestamp': timestamp, 'x': x, 'y': y})

    def on_click(self, x, y, button, pressed):
        if self.is_recording:
            timestamp = time.time()
            action_type = 'press' if pressed else 'release'
            self.recorded_actions.append({'type': 'click', 'timestamp': timestamp, 'x': x, 'y': y, 'button': button.name, 'action': action_type})

    def on_press(self, key):
        if self.is_recording:
            timestamp = time.time()
            self.recorded_actions.append({'type': 'key_press', 'timestamp': timestamp, 'key': str(key)})

    def on_release(self, key):
        if self.is_recording:
            timestamp = time.time()
            self.recorded_actions.append({'type': 'key_release', 'timestamp': timestamp, 'key': str(key)})

    def play_recording(self):
        for action in self.recorded_actions:
            timestamp = action['timestamp']
            delay = timestamp - (self.recorded_actions[0]['timestamp'] if self.recorded_actions else 0)
            time.sleep(delay)

            if action['type'] == 'move':
                self.mouse_controller.position = (action['x'], action['y'])
            elif action['type'] == 'click':
                if action['action'] == 'press':
                    self.mouse_controller.press(action['button'])
                else:
                    self.mouse_controller.release(action['button'])
            elif action['type'] == 'key_press':
                self.keyboard_controller.press(action['key'])
            elif action['type'] == 'key_release':
                self.keyboard_controller.release(action['key'])

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