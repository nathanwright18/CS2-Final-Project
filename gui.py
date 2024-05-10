from tkinter import *

class Gui:
    def __init__(self, window) -> None:
        """
        Function initializing class.
        :param window: Initializes the entire frame for the calculator in the gui.
        :param frame_one: First section of values for functionality of calculator.
        :param text: Shows the input given by the user based on buttons or values given.
        :param radio_answer: Sets integer value to what the caclulator should be showing based on the mode selected by the user.
        :param frame_two: Section where user selects input options for mode calculations after mode button is selected.
        :param button_one: When selected allows user to see input option for circle calculations.
        :param button_two: When selected allows user to see input option for square calculations.
        :param button_three: When selected allows user to see input option for rectangle calculations.
        :param button_four: When selected allows user to see input option for triangle calculations.
        :param frame_three: Section that allows user to input both to choose to input trig, mode operations or basic calculator functionality.
        :param clear_button: User removes all previous information saved by calculator and resets to how it would be as turning on a calculator.
        :param mode_button: User clicks to choose between circle, square, rectangle and triangle calculations.
        :param trig_button: User clicks to choose between sin, cos and tan calculations.
        :param divide_button: User selects this to run this operations for previously entered numerical value along with next inputted value.
        :param frame_four: Section that allows user to input specific numerical values and operations.
        :param seven_button: User selects to include numerical value to previously entered input.
        :param eight_button: User selects to include numerical value to previously entered input.
        :param nine_button: User selects to include numerical value to previously entered input.
        :param multiply_button: User selects this to run this operations for previously entered numerical value along with next inputted value.
        :param frame_five: Section that allows user to input specific numerical values and operations.
        :param four_button: User selects to include numerical value to previously entered input.
        :param five_button: User selects to include numerical value to previously entered input.
        :param six_button: User selects to include numerical value to previously entered input.
        :param subtract_button: User selects this to run this operations for previously entered numerical value along with next inputted value.
        :param frame_six: Section that allows user to input specific numerical values and operations.
        :param one_button: User selects to include numerical value to previously entered input.
        :param two_button: User selects to include numerical value to previously entered input.
        :param three_button: User selects to include numerical value to previously entered input.
        :param add_button: User selects this to run this operations for previously entered numerical value along with next inputted value.
        :param frame_seven: Section that allows user to input specific numerical values and operations.
        :param negative_button: Changes absolute value of the input given by the user.
        :param zero_button: User selects to include numerical value to previously entered input.
        :param decimal_button: User selects to change integer to float value.
        :param equal_button: User selects to finalize mathematical operations for main calculations done by simple caclulator.
        :param frame_eight: Section where user selects trig method to calculate.
        :param base_label: Pops up with what the input is being used for.
        :param base_input: Input for variable that base_label is shown as.
        :param base_submit_button: Submits all calculations for extra functionality for the calculator under the mode and trig options.
        :param height_label: Pops up with what the input is being used for as the secondary entry.
        :param height_input: Input for variable that height_label is shown as.
        :param frame_nine: Section where user selects what trig function they want to use for their calculation.
        :param sin_button: Calculates radian value for sin function with the two lengths of the side of the triangle being calculated.
        :param cos_button: Calculates radian value for cos function with the two lengths of the side of the triangle being calculated.
        :param tan_button: Calculates radian value for tan function with the two lengths of the side of the triangle being calculated.
        """
        self.window = window
        # Output section
        self.frame_one = Frame(self.window)
        self.text = Label(self.frame_one, text="0")
        self.text.config(bg="white", justify=CENTER, state=DISABLED)
        self.text.pack(side="left")
        self.frame_one.pack()
        # Mode radiobutton options
        self.frame_two = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(-1)
        self.button_one = Radiobutton(self.frame_two, text="Circle", variable=self.radio_answer, value=1)
        self.button_two = Radiobutton(self.frame_two, text="Square", variable=self.radio_answer, value=2)
        self.button_three = Radiobutton(self.frame_two, text="Rectangle", variable=self.radio_answer, value=3)
        self.button_four = Radiobutton(self.frame_two, text="Triangle", variable=self.radio_answer, value=4)
        self.button_one.pack(side="left")
        self.button_two.pack(side="left")
        self.button_three.pack(side="left")
        self.button_four.pack(side="left")
        self.frame_two.pack_forget()
        # section one of calculator
        self.frame_three = Frame(self.window)
        self.clear_button = Button(self.frame_three, text="Clear")
        self.mode_button = Button(self.frame_three, text="Mode")
        self.trig_button = Button(self.frame_three, text="Trig")
        self.divide_button = Button(self.frame_three, text="/")
        self.clear_button.pack(side="left")
        self.mode_button.pack(side="left")
        self.trig_button.pack(side="left")
        self.divide_button.pack(side="left")
        self.frame_three.pack()
        # numbers part one
        self.frame_four = Frame(self.window)
        self.seven_button = Button(self.frame_four, text="7")
        self.eight_button = Button(self.frame_four, text="8")
        self.nine_button = Button(self.frame_four, text="9")
        self.multiply_button = Button(self.frame_four, text="*")
        self.seven_button.pack(side="left")
        self.eight_button.pack(side="left")
        self.nine_button.pack(side="left")
        self.multiply_button.pack()
        self.frame_four.pack()
        # numbers part two
        self.frame_five = Frame(self.window)
        self.four_button = Button(self.frame_five, text="4")
        self.five_button = Button(self.frame_five, text="5")
        self.six_button = Button(self.frame_five, text="6")
        self.subtract_button = Button(self.frame_five, text="-")
        self.four_button.pack(side="left")
        self.five_button.pack(side="left")
        self.six_button.pack(side="left")
        self.subtract_button.pack(side="left")
        self.frame_five.pack()
        # numbers part three
        self.frame_six = Frame(self.window)
        self.one_button = Button(self.frame_six, text="1")
        self.two_button = Button(self.frame_six, text="2")
        self.three_button = Button(self.frame_six, text="3")
        self.add_button = Button(self.frame_six, text="+")
        self.one_button.pack(side="left")
        self.two_button.pack(side="left")
        self.three_button.pack(side="left")
        self.add_button.pack()
        self.frame_six.pack()
        self.frame_seven = Frame(self.window)
        self.negative_button = Button(self.frame_seven, text="+/-")
        self.zero_button = Button(self.frame_seven, text="0")
        self.decimal_button = Button(self.frame_seven, text=".")
        self.equal_button = Button(self.frame_seven, text="=")
        self.negative_button.pack(side="left")
        self.zero_button.pack(side="left")
        self.decimal_button.pack(side="left")
        self.equal_button.pack()
        self.frame_seven.pack()
        self.frame_eight = Frame(self.window)
        self.base_label = Label(self.frame_eight)
        self.base_input = Entry(self.frame_eight)
        self.base_submit_button = Button(self.frame_eight, text="Submit")
        self.height_label = Label(self.frame_eight)
        self.height_input = Entry(self.frame_eight)
        self.base_label.pack(side="left")
        self.base_input.pack(side="left")
        self.base_submit_button.pack(side="left")
        self.height_label.pack_forget()
        self.height_input.pack_forget()
        self.frame_eight.pack_forget()
        self.frame_nine = Frame(self.window)
        self.sin_button = Radiobutton(self.frame_nine, text="Sin", variable=self.radio_answer, value=5)
        self.cos_button = Radiobutton(self.frame_nine, text="Cos", variable=self.radio_answer, value=6)
        self.tan_button = Radiobutton(self.frame_nine, text="Tan", variable=self.radio_answer, value=7)
        self.sin_button.pack(side="left")
        self.cos_button.pack(side="left")
        self.tan_button.pack(side="left")
        self.frame_nine.pack_forget()