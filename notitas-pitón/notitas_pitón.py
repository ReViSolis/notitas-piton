import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector as mysqlcausa #para conectar con MySQL

def insertarRegistro(names, Lnames, age, height, phone, gender):
    try:
        connnection = mysqlcausa.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "laluznu7S!",
                database = "avanzaprogra",
            )
        cursor = connnection.cursor()
        query = "insert into tabla (notname, lastName, age, height, phone, sexo) values (%s, %s, %s, %s, %s, %s)"
        values = (names, Lnames, age, height, phone, gender)
        cursor.execute(query, values)
        connnection.commit()
        cursor.close()
        connnection.close()
        messagebox.showinfo("Datos", "Se guardaó a la base de datos")
    except mysqlcausa.Error as err:
        messagebox.showerror("ERROR", f"error fatal, corregirrrrrr!!: {err}") ##aquí quedaste OOOOOOOOOOOOOOOOOOOOOOOOOO

##defes
def ValidInt(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def ValidDeci(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def Valid10(valor):
    return valor.isdigit() and len(valor) == 10

def ValidText(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))


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
#Validar dato
    if (ValidInt(age) and ValidDeci(height) and Valid10(phone) and ValidText(names) and ValidText(Lnames)):

#Ingrsar datos al database
        insertarRegistro(names, Lnames, age, height, phone, gender)

        data = "Nombre: " + names + "\nApellidos: " + Lnames + "\nEdad: " + age + "\nAltura: " + height + "\nTelefono: " + phone + "\nSexo: " + gender
        with open("datasapitón.txt", "a") as file:
            file.write(data + "\n\n")
        messagebox.showinfo("Datos " + "Datos guardados: \n\n", data)
#limpiar después de guardar
        clear()
    else:
        messagebox.showerror("ERROR", "ingrsar dato valido en los campos")

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