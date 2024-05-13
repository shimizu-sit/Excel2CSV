import tkinter

# Window
window = tkinter.Tk()
window.title("Excel2CSV")
window.geometry("600x600")

# Label
label = tkinter.Label(text='label pack')
label.pack()
label_2 = tkinter.Label(text='Label_2 place')
label_2.place(x=200, y=200)

window.mainloop()