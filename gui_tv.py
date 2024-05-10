import tkinter as tk

# TV Remote GUI - title is TV Remote
class TVRemoteGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TV Remote")

        # GUI frame
        self.channel_frame = tk.Frame(self.master)
        self.channel_frame.pack(padx=10, pady=10)

        # GUI 'TV' - this is the black square the tv channels appear
        self.channel_canvas = tk.Canvas(self.channel_frame, width=100, height=100)
        self.channel_canvas.pack(padx=10, pady=10)
        self.channel_rectangle = self.channel_canvas.create_rectangle(0, 0, 100, 100, fill="black")
        self.channel_text = self.channel_canvas.create_text(50, 50, text="CNN", fill="red", font=("Arial", 14, "bold"))

        # GUI frame
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(padx=10, pady=10)

        # Power button, starts off as not activated
        self.power_state = False
        self.button_power = tk.Button(self.button_frame, text="Power", width=10)
        self.button_power.grid(row=0, column=0, padx=5, pady=5)

        # Blank spae between button
        Spacer1 = tk.Label(self.button_frame, text="")
        Spacer1.grid(row=1, column=0)

        # Volume up button
        self.button_volume_up = tk.Button(self.button_frame, text="Vol +", width=10)
        self.button_volume_up.grid(row=2, column=0, padx=5, pady=5)

        # Blank spae between button
        Spacer2 = tk.Label(self.button_frame, text="")
        Spacer2.grid(row=3, column=0)

        # Volume down button
        self.button_volume_down = tk.Button(self.button_frame, text="Vol -", width=10)
        self.button_volume_down.grid(row=4, column=0, padx=5, pady=5)

        # Blank spae between button
        Spacer3 = tk.Label(self.button_frame, text="")
        Spacer3.grid(row=5, column=0)

        # Channel up button
        self.button_channel_up = tk.Button(self.button_frame, text="Ch +", width=10)
        self.button_channel_up.grid(row=6, column=0, padx=5, pady=5)

        # Blank spae between button
        Spacer4 = tk.Label(self.button_frame, text="")
        Spacer4.grid(row=7, column=0)

        # Channel down button
        self.button_channel_down = tk.Button(self.button_frame, text="Ch -", width=10)
        self.button_channel_down.grid(row=8, column=0, padx=5, pady=5)

        # Blank spae between button
        Spacer5 = tk.Label(self.button_frame, text="")
        Spacer5.grid(row=9, column=0)

        # Makes mute button
        self.button_mute = tk.Button(self.button_frame, text="Mute", width=10)
        self.button_mute.grid(row=10, column=0, padx=5, pady=5)

        # Volume Slider
        self.volume_slider = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL)
        self.volume_slider.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Volume Slider set and returns when muted again
        self.volume_slider.set(50)
        self.previous_volume = 50