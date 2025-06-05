from tkinter import *
import PIL.Image
import PIL.ImageTk

window = Tk()
window.title('Anvil Cheater 2.0 by ravenousdox')

window.configure(bg='black')
window.geometry('500x500')

#im = PIL.Image.open("file1.png")
#photo = PIL.ImageTk.PhotoImage(im)

#label = Label(window, image=photo).grid(row=0, column=0)
#label.image = photo  # keep a reference!


Label(window, text='What would you like to do?', bg='black', fg='red', font='none 12 bold').grid(row=0, column=0)
Button(window, text='Perform Smith', width=14).grid(row=1, pady=5)
Button(window, text='Modify Item', width=14).grid(row=2, pady=5)
Button(window, text='Create Item', width=14).grid(row=3, pady=5)
Button(window, text='Regenerate Items', width=14).grid(row=4, pady=5)
Button(window, text='Reload Items', width=14).grid(row=5, pady=5)
Button(window, text='Initialize Items', width=14).grid(row=6, pady=5)
Button(window, text='Exit Program', width=14).grid(row=7, pady=5)

window.mainloop()
