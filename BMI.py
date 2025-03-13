from tkinter import *
from tkinter import messagebox as mbox


win = Tk()
win.title("BIM")
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry('%dx%d-1+0' % (width, height))
win.resizable(0, 0)
win.config(bg='#8072f8')
win.iconbitmap('icon.ico')


def BMI_calc():
    global BIM
    BHeight = float(var2.get())
    BWeight = float(var1.get())
    BIM = str('%.2f' % (BWeight / (BHeight * BHeight)))
    lablBMIResult.config(text=BIM)
    x = float(BIM)
    if x < 19:
        Underweight.config(bg='red', relief='sunken')  # ----Underweight
        normal.config(bg='#6ce95b', relief='flat')
        Overweight.config(bg='#6ce95b', relief='flat')
        Obesity_Level_I.config(bg='#6ce95b', relief='flat')
        Obesity_Level_II.config(bg='#6ce95b', relief='flat')
        Obesity_Level_III.config(bg='#6ce95b', relief='flat')
    elif x < 25:
        Underweight.config(bg='#6ce95b', relief='flat')  # ----Normal
        normal.config(bg='#ccff00', relief='sunken')
        Overweight.config(bg='#6ce95b', relief='flat')
        Obesity_Level_I.config(bg='#6ce95b', relief='flat')
        Obesity_Level_II.config(bg='#6ce95b', relief='flat')
        Obesity_Level_III.config(bg='#6ce95b', relief='flat')
    elif x < 30:
        Underweight.config(bg='#6ce95b', relief='flat')  # ----Overweight
        Overweight.config(bg='#ffd000', relief='sunken')
        normal.config(bg='#6ce95b', relief='flat')
        Obesity_Level_I.config(bg='#6ce95b', relief='flat')
        Obesity_Level_II.config(bg='#6ce95b', relief='flat')
        Obesity_Level_III.config(bg='#6ce95b', relief='flat')
    elif x < 35:
        Underweight.config(bg='#6ce95b', relief='flat')  # ----obesity-level 1
        Obesity_Level_I.config(bg='orange', relief='sunken')
        Overweight.config(bg='#6ce95b', relief='flat')
        normal.config(bg='#6ce95b', relief='flat')
        Obesity_Level_II.config(bg='#6ce95b', relief='flat')
        Obesity_Level_III.config(bg='#6ce95b', relief='flat')
    elif x < 40:
        Underweight.config(bg='#6ce95b', relief='flat')  # ----obesity-level 2
        Obesity_Level_II.config(bg='#ff3c00', relief='sunken')
        Obesity_Level_I.config(bg='#6ce95b', relief='flat')
        Overweight.config(bg='#6ce95b', relief='flat')
        normal.config(bg='#6ce95b', relief='flat')
        Obesity_Level_III.config(bg='#6ce95b', relief='flat')
    elif x < 900:
        Underweight.config(bg='#6ce95b', relief='flat')  # ----obesity-level 3
        Obesity_Level_III.config(bg='red', relief='sunken')
        Obesity_Level_II.config(bg='#6ce95b', relief='flat')
        Obesity_Level_I.config(bg='#6ce95b', relief='flat')
        Overweight.config(bg='#6ce95b', relief='flat')
        normal.config(bg='#6ce95b', relief='flat')


def Clear():
    lablBMIResult.config(text='')
    var1.set(0)
    var2.set(0.0)

    Underweight.config(bg='#6ce95b', relief='flat')
    Obesity_Level_III.config(bg='#6ce95b', relief='flat')
    Obesity_Level_II.config(bg='#6ce95b', relief='flat')
    Obesity_Level_I.config(bg='#6ce95b', relief='flat')
    Overweight.config(bg='#6ce95b', relief='flat')
    normal.config(bg='#6ce95b', relief='flat')


def about():
    mbox.showinfo('About this app', "Body mass index is calculated by dividing height squared\nby weight regardless "
                                    "of race or age, adjust the "
                                    "scale to your height and the weight in the text box then\ncalculate\n\nCompany "
                                    "Name: Esoteric Apps\n\nApplication Name: Body Mass Index "
                                    "Calculator\n\nReport Errors at: PempheroHajap10@Gmail.com\n\nVersion 1.8")


var1 = DoubleVar()
var2 = DoubleVar()
main = Frame(win, bg='#8072f8', pady=15)
main.pack()
Tops = Frame(main, width=width, height=100, bd=8, relief="raised", bg='#00ffa2')
Tops.pack(side='top')
f1 = Frame(main, width=600, height=600, bd=8, relief='raised', bg='#00ffa2')
f1.pack(side='left')
f2 = Frame(main, width=300, height=600, bd=8, relief='raised', bg='#6ce95b')
f2.pack(side='right')

f1a = Frame(f1, width=600, height=200, bd=20, relief="raised", bg='#6ce95b')
f1a.pack(side='top')
f1b = Frame(f1, width=600, height=400, bd=20, relief="raised", bg='#6ce95b')
f1b.pack(side='top')

Title = Label(Tops, text="         +     Body Mass Index Calculator    +        ", padx=16, pady=16, bd=16,
              fg='red', bg='#7ae0ca', font=('agency fb', 50, 'bold'), relief="raised", width=32, height=1)
Title.pack()

lblWeight = Label(f1a, text="Select Weight in kilograms", font=('arial', 20, 'bold'), bg='#6ce95b', bd=20)
lblWeight.grid(row=0, column=0)

Bodyweight = Scale(f1a, variable=var1, from_=1, to=315, length=880, tickinterval=14, orient=HORIZONTAL)
Bodyweight.grid(row=1, column=0)

lblblHeight = Label(f1b, text="Enter Height In Meters", bg='#6ce95b', font=('tahoma', 20, 'bold'), bd=20)
lblblHeight.grid(row=0, column=0)

txtHeight = Entry(f1b, textvariable=var2, font=('arial', 16, 'bold'), bd=16, width=22, justify='center')
txtHeight.grid(row=1, column=0)

lablBMIResult = Label(f1b, padx=16, pady=16, bd=16,
                      bg='#00ffa2', font=('arial', 30, 'bold'), relief="sunken", width=34, height=1)
lablBMIResult.grid(row=2, column=0)

Table = Label(f2, font=('arial', 20, 'bold'), text="BMI Table (Meaning)", pady=11, bg='#6ce95b').grid(row=0, column=0)
# ----------------------------------------------------Labels-----------------------------------------------------------

Underweight = Label(f2, text="Underweight         <  19 ", pady=5, bg='#6ce95b', font=('arial', 12, 'bold'))
Underweight.grid(row=1)
normal = Label(f2, text="Normal Weight      19-24", pady=5, bg='#6ce95b', font=('arial', 12, 'bold'))
normal.grid(row=2)
Overweight = Label(f2, text="Overweight            25-29", pady=5, bg='#6ce95b', font=('arial', 12, 'bold'))
Overweight.grid(row=3)

Obesity_Level_I = Label(f2, text="Obesity Level I      30-34", pady=5, bg='#6ce95b', font=('arial', 12, 'bold'))
Obesity_Level_I.grid(row=4)
Obesity_Level_II = Label(f2, text="Obesity Level II     35-39", pady=5, bg='#6ce95b', font=('arial', 12, 'bold'))
Obesity_Level_II.grid(row=5)
Obesity_Level_III = Label(f2, text="  Obesity Level III       >   40", pady=5, bg='#6ce95b', font=('arial', 12, 'bold'))
Obesity_Level_III.grid(row=6)

calculate_Button = Button(f2, text="Calculate", font=('arial', 25, 'bold'), bd=5, bg='#9395ff', width=15, height=3,
                          command=BMI_calc)
calculate_Button.grid(row=7)

clear_Button = Button(f2, text="Reset", font=('arial', 25, 'bold'), bd=5, bg='#9395ff', width=15, height=1,
                      command=Clear)
clear_Button.grid(row=8)

about_btn = Button(win, text='about', width=10, height=3, bg='#6ce95b', bd=5, font=('Arial', 16), command=about)
about_btn.place(x=1200, y=50)
version = Label(win, text='version: 1.8', font=('arial', 15, 'bold'), bg='#ff452b')
version.place(x=1230, y=700)
win.mainloop()
