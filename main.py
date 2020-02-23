import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 600,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Find Sports Teams')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter Latitude:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 75, window=label2)

label3 = tk.Label(root, text='Enter Longitude:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 125, window=label3)


entry1 = tk.Entry (root)
entry2 = tk.Entry (root)
canvas1.create_window(200, 100, window=entry1)
canvas1.create_window(200, 150, window=entry2)


def list_city():
	city_list = ["  ", "Vancouver", "Tornto"]
	variable = tk.StringVar(root)
	variable.set(city_list[0]) # default value

	w = tk.OptionMenu(root, variable, *city_list, command=callback)
	w.place(x = 200, y =250)
	w.pack()

def callback(selection):
	print(selection)

def getSquareRoot ():
    
    x1 = entry1.get()
    x2 = entry2.get()
    
    label4 = tk.Label(root, text= 'Sports Teams Within Radius of' + x1 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 200, window=label4)
    
    label5 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 260, window=label5)

# Main method
def main():

	button1 = tk.Button(text='Get Info', command=list_city, bg='brown', fg='black', font=('helvetica', 9, 'bold'))
	canvas1.create_window(200, 180, window=button1)
	root.mainloop()

# Main program       
if __name__=="__main__":
    main()
    
