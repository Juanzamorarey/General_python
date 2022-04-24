from tkinter import*

def sumar():
    r.set(float(n1.get())+float(n2.get())) 
    borrar()
def restar():
    r.set(float(n1.get())-float(n2.get())) 
    borrar()
def dividir():
    r.set(float(n1.get())/float(n2.get())) 
    borrar()
def multiplicar():
    r.set(float(n1.get())*float(n2.get())) 
    borrar()

def borrar():
    n1.set("")
    n2.set("")

root= Tk()
root.config(bd=15)
root.resizable(0,0)

n1 = StringVar()
n2 = StringVar()
r = StringVar()


Label(root,text="Número 1").pack(side="left")
entry1 = Entry(root,justify="left",textvariable=n1).pack(side="left") 
Label(root,text="Número 2").pack(side="left")
entry2 = Entry(root,justify="left",textvariable=n2).pack(side="left") 
Label(root,text="Resultado").pack(side="left")
Label(root,text="").pack(side="left") 
resultado = Entry(root,justify="left",textvariable=r,state="disabled").pack(side="left") 

frame = Frame(root,width=80,height=80).pack(side = "right", anchor="n")

Button(frame, text="Sumar", command=sumar).pack(side="right",anchor="n")
Button(frame, text="Restar", command=restar).pack(side="right",anchor="n")
Button(frame, text="Multiplicar", command=multiplicar).pack(side="right",anchor="n")
Button(frame, text="Dividir", command=dividir).pack(side="right",anchor="n")


root.mainloop()