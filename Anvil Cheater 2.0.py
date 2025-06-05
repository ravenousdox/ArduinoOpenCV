from tkinter import *

def click():
    entered_text = textentry.get()
    output.delete(0.0, END)

window = Tk()
window.title('Anvil Cheater 2.0 by ravenousdox')
Label(window, bg='black').grid(row=0, column=0, sticky=E)
window.configure(background='black')
Label(window, text="Enter word: ", bg='black', fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=W)
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)
Label(window, text="\nTest:", bg='black', fg='white', font='none 12 bold').grid(row=4, column=0, sticky=W)
output = Text(window, width=75, height=6, wrap=WORD, background='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)

image = Image.open(r'C:\Users\RIG1\Desktop\file1.png')
photo_image = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo_image)
label.pack()

window.mainloop()
