import gui_tv

# Initializes TVRemote buttons
class Logic:
    def __init__(self, gui: gui_tv.TVRemoteGUI) -> None:
        self.gui = gui
        self.gui.button_power.config(command=self.toggle_power)
        self.gui.button_volume_up.config(command=self.volume_up)
        self.gui.button_volume_down.config(command=self.volume_down)
        self.gui.button_channel_up.config(command=self.channel_up)
        self.gui.button_channel_down.config(command=self.channel_down)
        self.gui.button_mute.config(command=self.mute_tv)

        # Power button - hides channel name so the TV is 'off'
    def toggle_power(self):
        if self.gui.power_state:
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, state="normal")
        else:
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, state="hidden")
        self.gui.power_state = not self.gui.power_state
        self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="CNN", fill="red", font=("Arial", 14, "bold"))
        self.gui.volume_slider.set(50)

        # Volume Slider
    def volume_up(self):
        current_volume = self.gui.volume_slider.get()
        if current_volume < 100:
            self.gui.volume_slider.set(current_volume + 1)

        # Volume down button
    def volume_down(self):
        current_volume = self.gui.volume_slider.get()
        if current_volume > 0:
            self.gui.volume_slider.set(current_volume - 1)

        # Channel up when button pressed
    def channel_up(self):
        current_text = self.gui.channel_canvas.itemcget(self.gui.channel_text, "text")
        if current_text == "CNN":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="Food Network", fill="blue", font=("Arial", 10, "bold"))
        if current_text == "Food Network":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="PBS", fill="green", font=("Arial", 14, "bold"))
        if current_text == "PBS":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="History Channel", fill="orange", font=("Arial", 9, "bold"))
        if current_text == "History Channel":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="Monkey TV", fill="mint cream", font=("Arial", 12, "bold"))
        if current_text == "Monkey TV":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="How Its Made", fill="hot pink", font=("Arial", 11, "bold"))
        if current_text == "How Its Made":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="Dance Off", fill="RoyalBlue", font=("Arial", 14, "bold"))
        if current_text == "Dance Off":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="Monke 2", fill="cyan", font=("Arial", 14, "bold"))
        if current_text == "Monke 2":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="CNN", fill="red", font=("Arial", 14, "bold"))

        # Channel down when button pressed
    def channel_down(self):
        current_text = self.gui.channel_canvas.itemcget(self.gui.channel_text, "text")
        if current_text == "CNN":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="Monke 2", fill="blue", font=("Arial", 12, "bold"))
        if current_text == "Monke 2":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="Dance Off", fill="green", font=("Arial", 11, "bold"))
        if current_text == "Dance Off":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="How Its Made", fill="orange", font=("Arial", 9, "bold"))
        if current_text == "How Its Made":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="Monkey TV", fill="mint cream", font=("Arial", 12, "bold"))
        if current_text == "Monkey TV":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="History Channel", fill="hot pink", font=("Arial", 9, "bold"))
        if current_text == "History Channel":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="PBS", fill="RoyalBlue", font=("Arial", 14, "bold"))
        if current_text == "PBS":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="Food Network", fill="cyan", font=("Arial", 10, "bold"))
        if current_text == "Food Network":
            self.gui.channel_canvas.itemconfigure(self.gui.channel_text, text="CNN", fill="red", font=("Arial", 14, "bold"))

        # Mute button - returns volume to last one set when pressed again
    def mute_tv(self):
        if self.gui.volume_slider.get() != 0:
            self.gui.previous_volume = self.gui.volume_slider.get()
            self.gui.volume_slider.set(0)
        else:
            self.gui.volume_slider.set(self.gui.previous_volume)