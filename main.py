from gui import *
import logic

def main():
    window = Tk()
    window.title("Calculator")
    window.geometry("700x300")
    window.resizable(False, False)
    gui = Gui(window)
    logic.Logic(gui)
    window.mainloop()


if __name__ == "__main__":
    main()