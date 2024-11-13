import tkinter as tk
import json
import subprocess
from tkinter import messagebox

class VNCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Embedded VNC Viewer")
        self.root.geometry("800x600")

        # Frame where the VNC client will be displayed
        self.vnc_frame = tk.Frame(self.root, width=700, height=500, bg="black")
        self.vnc_frame.place(x=50, y=50)

        # Start the VNC client in a subprocess within the frame
        self.start_vnc_client()

        # Overlay Frame to capture clicks on top of VNC viewer
        self.overlay_frame = tk.Frame(self.vnc_frame, width=700, height=500, bg="", highlightthickness=0)
        self.overlay_frame.place(x=0, y=0)

        # Bind click event to overlay frame
        self.overlay_frame.bind("<Button-1>", self.get_click_coordinates)

    def start_vnc_client(self):
        try:
            # Start a VNC client as an embedded subprocess (using TigerVNC)
            self.vnc_process = subprocess.Popen([
                "vncviewer",  # Use TigerVNC or your VNC client of choice
                "localhost:5901",  # Replace with your actual VNC server address
                "-geometry", "700x500"  # Match the frame's size for alignment
            ])
        except FileNotFoundError:
            messagebox.showerror("Error", "VNC viewer not found. Please install TigerVNC or adjust path.")

    def get_click_coordinates(self, event):
        # Get the click coordinates relative to the frame
        x = event.x
        y = event.y

        # Log the coordinates to JSON
        self.save_coordinates_to_json(x, y)

    def save_coordinates_to_json(self, x, y):
        # Append coordinates to JSON file
        coordinates = {"x": x, "y": y}
        try:
            with open("click_coordinates.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(coordinates)
        
        with open("click_coordinates.json", "w") as file:
            json.dump(data, file, indent=4)

    def on_closing(self):
        # Close VNC subprocess on exit
        if self.vnc_process:
            self.vnc_process.terminate()
        self.root.destroy()

# Main Application Setup
root = tk.Tk()
app = VNCApp(root)
root.protocol("WM_DELETE_WINDOW", app.on_closing)
root.mainloop()
