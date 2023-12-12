from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = "snow")

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.3,anchor=CENTER)

label = Label(root, text = "Name in Ascii  : ",  bg="light yellow", fg="black")
label_encrypted = Label(root, text = "encrypted name  : ",  bg="light yellow", fg="black")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
        ascii = int(ord(letter))
        encrypted = ascii - 1 
        label_encrypted["text"] += str(chr(encrypted))
        
        
btn=Button(root, text="Show name is Ascii and encrypted", command=asciiConverter, bg="gold" , fg = 'black') 
btn.place(relx=0.5,rely=0.4, anchor=CENTER)             
label.place(relx=0.5,rely=0.5,anchor=CENTER)
label_encrypted.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()