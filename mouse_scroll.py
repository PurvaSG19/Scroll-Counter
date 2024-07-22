import tkinter as tk
from pynput import mouse

class ScrollTracker:
    def __init__(self, root):
        self.root = root
        self.total_scroll = 0 # initialize count = 0 

        # Create label to display the scroll count
        self.label = tk.Label(root, text=f"Total Scroll: {self.total_scroll}", font=("Roboto", 16))
        self.label.pack(padx=10,pady=10)


        # Set up the window in the corner of the screen
        self.root.overrideredirect(True) # remove the window decorations
        self.root.geometry("+10+10")  # Position at (10, 10)
        self.root.attributes("-topmost", True)  # Keep window on top of other tabs
        

        # Start the mouse listener
        self.start_listener()

    def on_scroll(self, x, y, dx, dy):
        self.total_scroll += abs(dy)
        self.label.config(text=f"Total Scroll: {self.total_scroll}")

    def start_listener(self):
        self.listener = mouse.Listener(on_scroll=self.on_scroll)
        self.listener.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollTracker(root)
    root.mainloop()
