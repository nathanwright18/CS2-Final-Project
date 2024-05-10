import tkinter as tk
from gui_tv import TVRemoteGUI
import logic_tv



# Initialize Tkinter gui to pop up and stay up
def main():
    root = tk.Tk()
    remote_gui = TVRemoteGUI(root)
    logic_tv.Logic(remote_gui)
    root.mainloop()

if __name__ == "__main__":
    main()