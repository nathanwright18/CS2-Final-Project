import gui
import math

class Logic:
    def __init__(self, gui: gui.Gui) -> None:
        """
        Function initializing class.
        :param gui: Variable to call functions from gui file.
        :param input_value: Saves value for current input that the user is currently entering.
        :param output_value: Saves value from input if any calculations need to be made with more than one numerical input for accurate output when final calculation is made.
        :param input_values: Saves input for the method of calculation including add, subtract, multiply and divide.
        """
        self.gui = gui
        self.input_value: str = ""
        self.output_value: int = 0
        self.input_values: list = []
        self.gui.base_submit_button.config(command=self.base_height_submit)
        self.gui.equal_button.config(command=self.equal)
        self.gui.button_one.config(command=self.mode)
        self.gui.button_two.config(command=self.mode)
        self.gui.button_three.config(command=self.mode)
        self.gui.button_four.config(command=self.mode)
        self.gui.clear_button.config(command=self.clear)
        self.gui.mode_button.config(command=self.mode)
        self.gui.trig_button.config(command=self.trig)
        self.gui.divide_button.config(command=self.divide)
        self.gui.multiply_button.config(command=self.multiply)
        self.gui.subtract_button.config(command=self.subtract)
        self.gui.add_button.config(command=self.add)
        self.gui.negative_button.config(command=self.negative)
        self.gui.decimal_button.config(command=self.decimal)
        self.gui.equal_button.config(command=self.equal)
        self.gui.nine_button.config(command=self.nine)
        self.gui.eight_button.config(command=self.eight)
        self.gui.seven_button.config(command=self.seven)
        self.gui.six_button.config(command=self.six)
        self.gui.five_button.config(command=self.five)
        self.gui.four_button.config(command=self.four)
        self.gui.three_button.config(command=self.three)
        self.gui.two_button.config(command=self.two)
        self.gui.one_button.config(command=self.one)
        self.gui.zero_button.config(command=self.zero)
        self.gui.sin_button.config(command=self.trig)
        self.gui.cos_button.config(command=self.trig)
        self.gui.tan_button.config(command=self.trig)
    def base_height_submit(self):
        """
        Function outputs extra functions with correctly inputted values.
        """
        try:
            first_input: float = float(self.gui.base_input.get())
            output_list: list = []
            if self.gui.radio_answer.get() == 1 or self.gui.radio_answer.get() == 2:
                if self.gui.radio_answer.get() == 1:
                    output_list.append(first_input)
                    output: float = math.pi * first_input
                    self.gui.text.config(text=f"Area: {output:.4f}")
                elif self.gui.radio_answer.get() == 2:
                    output = first_input ** 2
                    self.gui.text.config(text=f"Area: {output:.4f}")       
            else:
                second_input = float(self.gui.height_input.get())
                if self.gui.radio_answer.get() == 3:
                    output = first_input * second_input
                    self.gui.text.config(text=f"Area: {output:.4f}")
                elif self.gui.radio_answer.get() == 4:
                    output = 0.5 * first_input * second_input
                    self.gui.text.config(text=f"Area: {output:.4f}")
                elif self.gui.radio_answer.get() == 5:
                    output = math.asin(first_input / second_input)
                    self.gui.text.config(text=f"Sin: {output:.4f}")
                elif self.gui.radio_answer.get() == 6:
                    output = math.acos(first_input / second_input)
                    self.gui.text.config(text=f"Cos: {output:.4f}")
                elif self.gui.radio_answer.get() == 7:
                    output = math.atan(first_input / second_input)
                    self.gui.text.config(text=f"Tan: {output:.4f}")
        except ZeroDivisionError:
            self.gui.text.config(text="Division by 0 not allowed.")
        except ValueError:
            self.gui.text.config(text="Enter valid values for entries")
    def equal(self):
        """
        Function outputs normal numerical operations from users input through provided buttons.
        """
        try:
            if self.gui.radio_answer.get() == -1:
                if self.input_values[0] == "+":
                    self.output_value = float(self.output_value) + float(self.input_value)
                    self.gui.text.config(text=f"{self.output_value:.4f}")
                    self.input_value = ""
                    self.input_values = []
                    return self.output_value
                elif self.input_values[0] == "-":
                    self.output_value = float(self.output_value) - float(self.input_value)
                    self.gui.text.config(text=f"{self.output_value:.4f}")
                    self.input_value = ""
                    self.input_values = []
                    return self.output_value
                elif self.input_values[0] == "*":
                    self.output_value = float(self.output_value) * float(self.input_value)
                    self.gui.text.config(text=f"{self.output_value:.4f}")
                    self.input_value = ""
                    self.input_values = []
                    return self.output_value
                elif self.input_values[0] == "/":
                    try:
                        self.output_value = float(self.output_value) / float(self.input_value)
                        self.gui.text.config(text=f"{self.output_value:.4f}")
                        self.input_value = ""
                        self.input_values = []
                    except ZeroDivisionError:
                        self.gui.text.config(text="Division by 0 not allowed.")
                    return self.output_value
                else:
                    self.gui.text.config(text="Choose a valid method")
        except IndexError:
            self.gui.text.config(text="Choose a valid operation.")
    def clear(self):
        """
        Function resets the calculator.
        """
        self.gui.radio_answer.set(-1)
        self.gui.text.config(text="0")
        self.gui.frame_two.pack_forget()
        self.gui.frame_eight.pack_forget()
        self.gui.frame_nine.pack_forget()
        self.input_values = []
        self.output_value = 0
        self.input_value = ""
    def trig(self):
        """
        Function give user the option to pick between the three trig options and provides input options for the functionality.
        """
        self.gui.frame_two.pack_forget()
        self.gui.frame_eight.pack_forget()
        self.gui.frame_nine.pack()
        status = self.gui.radio_answer.get()
        if status == 5:
            self.gui.base_label.config(text="Opposite")
            self.gui.height_label.config(text="Hypotenuse")
            self.gui.height_label.pack(side="left")
            self.gui.height_input.pack(side="left")
            self.gui.frame_eight.pack()
        elif status == 6:
            self.gui.base_label.config(text="Adjacent")
            self.gui.height_label.config(text="Hypotenuse")
            self.gui.height_label.pack(side="left")
            self.gui.height_input.pack(side="left")
            self.gui.frame_eight.pack()
        elif status == 7:
            self.gui.base_label.config(text="Opposite")
            self.gui.height_label.config(text="Adjacent")
            self.gui.height_label.pack(side="left")
            self.gui.height_input.pack(side="left")
            self.gui.frame_eight.pack()
    def mode(self):
        """
        Function allows user to choose and calculate the area of four provided shapes.
        """
        self.gui.frame_nine.pack_forget()
        self.gui.frame_eight.pack_forget()
        self.gui.frame_two.pack()
        status = self.gui.radio_answer.get()
        if status == 1:
            self.gui.base_label.config(text="Radius")
            self.gui.height_label.pack_forget()
            self.gui.height_input.pack_forget()
            self.gui.frame_eight.pack()
        elif status == 2:
            self.gui.base_label.config(text="Side")
            self.gui.height_label.pack_forget()
            self.gui.height_input.pack_forget()
            self.gui.frame_eight.pack()
        elif status == 3:
            self.gui.base_label.config(text="Length")
            self.gui.height_label.config(text="Width")
            self.gui.height_label.pack(side="left")
            self.gui.height_input.pack(side="left")
            self.gui.frame_eight.pack()
        elif status == 4:
            self.gui.base_label.config(text="Base")
            self.gui.height_label.config(text="Height")
            self.gui.height_label.pack(side="left")
            self.gui.height_input.pack(side="left")
            self.gui.frame_eight.pack()
    def divide(self):   
        """
        Function allows user to divide given input with next provided input.
        """
        if self.gui.radio_answer.get() == -1:
            self.gui.text.config(text=f"{self.gui.text.cget("text")}/")
            if self.output_value != 0 and self.input_value != "":
                self.output_value = self.output_value / self.input_value
            elif self.output_value != 0 and self.input_value == "":
                self.input_value = ""
            else:
                self.output_value = float(self.input_value)
            self.input_value = ""
            try:
                if len(self.input_values) > 0:
                    self.input_values[0] = "/"
                else:
                    self.input_values.append("/")
            except IndexError:
                self.gui.text.config(text="Choose a valid operation.")
            return self.output_value
    def multiply(self):        
        """
        Function allows user to multiply given input with next provided input.
        """
        if self.gui.radio_answer.get() == -1:
            self.gui.text.config(text=f"{self.gui.text.cget("text")}*")
            if self.output_value != 0 and self.input_value != "":
                self.output_value = self.output_value * self.input_value
            elif self.output_value != 0 and self.input_value == "":
                self.input_value = ""
            else:
                self.output_value = float(self.input_value)
            self.input_value = ""
            try:    
                if len(self.input_values) > 0:
                    self.input_values[0] = "*"
                else:
                    self.input_values.append("*")
            except IndexError:
                self.gui.text.config(text="Choose a valid operation.")
            return self.output_value
    def subtract(self):
        """
        Function allows user to subtract given input with next provided input.
        """
        if self.gui.radio_answer.get() == -1:
            self.gui.text.config(text=f"{self.gui.text.cget("text")}-")
            if self.output_value != 0 and self.input_value != "":
                self.output_value = self.output_value - self.input_value
            elif self.output_value != 0 and self.input_value == "":
                self.input_value = ""
            else:
                self.output_value = float(self.input_value)
            self.input_value = ""
            try:
                if len(self.input_values) > 0:
                    self.input_values[0] = "-"
                else:
                    self.input_values.append("-")
            except IndexError:
                self.gui.text.config(text="Choose a valid operation.")
            return self.output_value
    def add(self):
        """
        Function allows user to divide given input with next provided input.
        """
        if self.gui.radio_answer.get() == -1:
            self.gui.text.config(text=f"{self.gui.text.cget("text")}+")
            if self.output_value != 0 and self.input_value != "":
                self.output_value = float(self.output_value) + float(self.input_value)
            elif self.output_value != 0 and self.input_value == "":
                self.input_value = ""
            else:
                self.output_value = float(self.input_value)
            self.input_value = ""
            try:
                if len(self.input_values) > 1:
                    self.input_values[0] = "+"
                else:
                    self.input_values.append("+")
            except IndexError:
                self.gui.text.config(text="Choose a valid operation.")
            return self.output_value
    def negative(self):
        """
        Function changes the value to negative or positive based on previous input value provided.
        """
        if self.gui.radio_answer.get() == -1:
            if float(self.input_value) < 0:
                self.gui.text.config(text=f"{0 - self.input_value}")
            else:
                self.gui.text.config(text=f"-{self.input_value}")
            self.input_value = 0 - float(self.input_value)
            return self.input_value
    def decimal(self):
        """
        Function changes digit to float when input value is a digit.
        """
        if self.gui.radio_answer.get() == -1:
            if self.input_value.isdigit():
                self.input_value = self.input_value + "."
                previous_input = self.gui.text.cget("text")
                self.gui.text.config(text=f"{previous_input}.")
                return self.input_value
    def nine(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "9"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}9")
            return self.input_value
    def eight(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "8"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}8")
            return self.input_value
    def seven(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "7"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}7")
            return self.input_value
    def six(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "6"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}6")
            return self.input_value
    def five(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "5"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}5")
            return self.input_value
    def four(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "4"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}4")
            return self.input_value
    def three(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "3"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}3")
            return self.input_value
    def two(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "2"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}2")
            return self.input_value
    def one(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "1"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}1")
            return self.input_value
    def zero(self):
        """
        Function adds the numerical value to previously entered input.
        """
        if self.gui.radio_answer.get() == -1:
            self.input_value = str(self.input_value) + "0"
            self.gui.text.config(text=f"{self.gui.text.cget("text")}0")
            return self.input_value