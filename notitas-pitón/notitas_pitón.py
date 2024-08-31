import tkinter as tk
from tkinter import messagebox

##Guardar datos
def save():
    names = tbname.get()
    Lnames = tbLname.get()
    age = tbage.get()
    height = tbheight.get()
    phone = tbphone.get()
    gender = ""
    if varGender.get() == 1:
        gender = "Hombre"
    elif varGender.get() == 2:
        gender = "Mujer"
    data = "Nombre: " + names + "\nApellidos: " + Lnames + "\nEdad: " + age + "\nAltura: " + height + "\nTelefono: " + phone + "\nSexo: " + gender
    with open("datasapitón.txt", "a") as file:
        file.write(data + "\n\n")
    messagebox.showinfo("Datos " + "Datos guardados: \n\n", data)
##Borrar datos
def clear():
    tbname.delete(0, tk.END)
    tbLname.delete(0, tk.END)
    tbage.delete(0, tk.END)
    tbheight.delete(0, tk.END)
    tbphone.delete(0, tk.END)
    varGender.set(0)

def delete_fun():
    clear()

##Crear Ventana
window = tk.Tk()
window.geometry("520x500")
window.title("Formulario")
##Crear variable de RadioButton
varGender = tk.IntVar()

##Crear campos de entrada y etiquetas (el diseño de la ventana) (tb= TextBox, Lb= Label)
lbName = tk.Label(window, text= "Nombre: ")
lbName.pack()
tbname = tk.Entry()
tbname.pack()
lbLName = tk.Label(window, text= "Apellido: ")
lbLName.pack()
tbLname = tk.Entry()
tbLname.pack()
lbAge= tk.Label(window, text= "Edad: ")
lbAge.pack()
tbage = tk.Entry()
tbage.pack()
lbHeight = tk.Label(window, text= "Altura: ")
lbHeight.pack()
tbheight = tk.Entry()
tbheight.pack()
lbPhone = tk.Label(window, text= "Telefono: ")
lbPhone.pack()
tbphone = tk.Entry()
tbphone.pack()
##CheckBox
lbGender = tk.Label(window, text= "Sexo")
lbGender.pack()
rbMale = tk.Radiobutton(window, text= "Hombre", variable = varGender, value=1)
rbMale.pack()
rbFemale = tk.Radiobutton(window, text = "Mujer", variable = varGender, value = 2)
rbFemale.pack()

##Botones
btDelete = tk.Button(window, text = "Borrar", command = delete_fun)
btDelete.pack()
btGuardar = tk.Button(window, text = "Guardar", command = save)
btGuardar.pack()
##ejecución de ventana
window.mainloop()