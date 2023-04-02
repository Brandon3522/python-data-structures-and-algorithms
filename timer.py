import tkinter as tk
from datetime import timedelta

def start_timer():
    global time
    # Get the number of minutes from the spinbox
    minutes = int(spinbox.get())

    # Calculate the number of seconds
    time = minutes * 60
    time_label.config(text=str(time))

    # Start the countdown
    countdown()

def countdown():
    global time
    # Update the time remaining
    time -= 1
    time_label.config(text=str(time))

    if time > 0:
        # Schedule another countdown after 1000ms (1 second)
        time_label.after(1000, countdown)
    else:
        # Stop the countdown and change the label text
        time_label.config(text="Time's up!")

# Create a new Tkinter window
root = tk.Tk()
root.title("Timer")

# Create a label to display the time remaining
time_label = tk.Label(root, font=("Helvetica", 24))
time_label.pack()

# Create a spinbox to select the number of minutes
spinbox = tk.Spinbox(root, from_=1, to=60)
spinbox.pack()

# Create a button to start the timer
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

# Run the Tkinter event loop
root.mainloop()
