from tkinter import * 
mywindow = Tk() 
mywindow.geometry("650x550")
mywindow.title("solicitud de cheque")
mywindow.resizable(False,False)
mywindow.config(background = "#FEF7DC")
main_title = Label(text="solicitud de cheque", font=("Cambria",13), bg="#D6D2C4", fg="black", width="550", height="2")
main_title.pack()

def send_data():
    nombre_info = username.get()
    cantidad_letras_info = cantidad_letras.get()
    concepto_info = concepto.get()
    age_info = str(age.get())
    print(username_info,"\t", password_info,"\t", fullname_info,"\t", age_info)


nombre_label = Label(text="Nombre: ", bg="#FFEEDD")
nombre_label.place(x=22, y=70)
cantidad_letras_label = Label(text="Cantidad en letras: ", bg="#FFEEDD")
cantidad_letras_label.place(x=22, y=100)
concepto_label = Label(text="En concepto de : ", bg="#FFEEDD")
concepto_label.place(x=25, y=130)
nombre_cuenta_label = Label(text="Nombre de la cuenta ", bg="#FFEEDD")
nombre_cuenta_label.place(x=22, y=180)
num_cuenta_label = Label(text="No. de la cuenta ", bg="#FFEEDD")
num_cuenta_label.place(x=200, y=180)
debito_label = Label(text="Débito ", bg="#FFEEDD")
debito_label.place(x=360, y=180)
credito_label = Label(text="Crédito", bg="#FFEEDD")
credito_label.place(x=520, y=180)

nombre = StringVar()
cantidad_letras = StringVar()
concepto = StringVar()
nombre_cuenta = StringVar()


nombre_entry = Entry(textvariable=nombre, width="40")
cantidad_letras_entry = Entry(textvariable=cantidad_letras, width="40")
concepto_entry = Entry(textvariable=concepto, width="40")

nombre_entry.place(x=80, y=70)
cantidad_letras_entry.place(x=130, y=100)
concepto_entry.place(x=130, y=130)

# Submit Button
submit_btn = Button(mywindow,text = "Submit Info", width = "10", height = "2", command = send_data, bg = "#F5C6AA")
submit_btn.place(x = 22, y = 320)

