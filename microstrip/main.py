import math
import tkinter as tk

root = tk.Tk()

# setting the windows size
root.geometry("600x400")
# transmission line details
class Transmission_line:
    def __init__(self, dielectric, width, height, length, frequency):
        self.dielectric = dielectric
        self.width = width
        self.height = height
        self.category = bool((self.width/self.height)>1)
        self.ratio = self.width / self.height
        self.electrical_length = length/frequency*0.0254

    def calculate(self):
        impedance = 0
        if self.category ==0:
            eff = 0.5*(self.dielectric+1+(self.dielectric-1)*(1/math.sqrt(1+12/self.ratio))+0.04*(1-self.ratio**2))
            impedance = 60 * math.log((8/self.ratio)+(self.ratio/4))/math.sqrt(eff)
        if self.category ==1:
            eff =0.5*(self.dielectric+1+((self.dielectric-1)/math.sqrt(1/12/self.ratio)))
            impedance = 120*math.pi/(math.sqrt(eff)*(self.ratio+1.393+2*math.log(self.ratio+1.444)/3))
        # getting the phase velocity easily
        phase_velocity = 3*10**8/math.sqrt(self.dielectric)
        electrical_length = self.electrical_length/(phase_velocity/(10**5))
        impedance_text = ("The characteristic impedance is " + str(impedance) +" ohms.")
        phase_velocity_text = ("The phase velocity is "+str(phase_velocity)+" m/s.")
        length_text = ("The electrical length is "+str(electrical_length)+" m.")
        output1 = tk.Label(root,text=impedance_text)
        output1.grid(row=7,column=0)
        output2 = tk.Label(root, text=phase_velocity_text)
        output2.grid(row=8, column=0)
        output3 = tk.Label(root, text=length_text)
        output3.grid(row=9, column=0)
        return 0


# declaring string variable for storing name and password bc tk is stupid
width_var = tk.StringVar()
dia_var = tk.StringVar()
height_var = tk.StringVar()
length_var = tk.StringVar()
frequency_var = tk.StringVar()


def setup_line():
    width = float(width_var.get())
    dielectric = float(dia_var.get())
    height = float(height_var.get())
    length = float(length_var.get())
    frequency = float(frequency_var.get())
    line = Transmission_line(dielectric, width, height, length, frequency)
    line.calculate()

width_text = tk.Label(root, text='Width(in)')
width = tk.Entry(root, textvariable=width_var)

dialec_text = tk.Label(root, text='Dielectric Constant (relative to free space)')
dialec = tk.Entry(root, textvariable=dia_var)

height_text = tk.Label(root, text='Height(in)')
height = tk.Entry(root, textvariable=height_var)

length_text = tk.Label(root, text='Length(in)')
length = tk.Entry(root, textvariable=length_var)

frequency_text = tk.Label(root, text='Frequency (MHz)')
frequency = tk.Entry(root, textvariable=frequency_var)

calc = tk.Button(root, text='Calculate', command=setup_line)


# placing the label and entry in
# the required position using grid
# method
dialec_text.grid(row=0,column=0)
dialec.grid(row=0, column=1)
width_text.grid(row=1,column=0)
width.grid(row=1, column=1)
height_text.grid(row=2,column=0)
height.grid(row=2, column=1)
length_text.grid(row=3,column=0)
length.grid(row=3, column=1)
frequency_text.grid(row=4,column=0)
frequency.grid(row=4, column=1)
calc.grid(row=6, column=1)
# performing an infinite loop
# for the window to display
root.mainloop()
