from tkinter import * 
mywindow = Tk() 
mywindow.geometry("650x550")
mywindow.title("solicitud de cheque")
mywindow.resizable(False,False)
mywindow.config(background = "#FEF7DC")
main_title = Label(text="SOLICITUD DE CHEQUE", font=("Cambria",13), fg="black", width="550", height="2")
main_title.pack()

#creamos la imgen
imagen =PhotoImage(file="compulab.png")
lblimagen=Label(mywindow,image=imagen).place(x=10,y=-3, width="100", height="50")


def send_data():
	nombre_data = nombre.get()
	fecha_data = fecha.get()
	cantidad_letras_data = cantidad_letras.get()
	concepto_data = concepto.get()
	nombre_cuenta_data = nombre_cuenta.get()
	num_cuenta_data = str(num_cuenta.get())
	debito_data = str(debito.get())
	credito_data = str(credito.get())
	banco_data = banco.get()
	solicitado_data = solicitado.get()
	autorizado_data = autorizado.get()
	confeccionado_data = confeccionado.get()
	dinero_data = str(dinero.get())
	banco_data = banco.get()
	print(nombre_data,"\t", cantidad_letras_data,"\t", fecha_data,"\t", concepto_data,"\t", dinero_data,"\t",banco_data,"\t",debito_data,"\t",credito_data,"\t",solicitado_data,"\t",autorizado_data,"\t",confeccionado_data)

	newfile = open("solicitud de cheque.txt","a")
	newfile.write(nombre_data)
	newfile.write("\t")
	newfile.write(cantidad_letras_data)
	newfile.write("\t")
	newfile.write(dinero_data)
	newfile.write("\t")
	newfile.write(concepto_data)
	newfile.write("\t")
	newfile.write(fecha_data)
	newfile.write("\t")
	newfile.write(banco_data)
	newfile.write("\t")
	newfile.write(debito_data)
	newfile.write("\t")
	newfile.write(credito_data)
	newfile.write("\t")
	newfile.write(solicitado_data)
	newfile.write("\t")
	newfile.write(autorizado_data)
	newfile.write("\t")
	newfile.write(confeccionado_data)
	newfile.write("\n")
	newfile.close()

	nombre_entry.delete(0, END)	
	fecha_entry.delete(0, END)
	cantidad_letras_entry.delete(0, END)
	concepto_entry.delete(0, END)
	dinero_entry.delete(0, END)
	nombre_cuenta_entry.delete(0,END)
	num_cuenta_entry.delete(0,END)
	banco_entry.delete(0, END)
	debito_entry.delete(0, END)
	credito_entry.delete(0, END)
	solicitado_entry.delete(0, END)
	autorizado_entry.delete(0, END)
	confeccionado_entry.delete(0, END)


nombre_label = Label(text="Nombre: ", bg="#FFEEDD")
nombre_label.place(x=40, y=70)

fecha_label = Label(text="Fecha: ", bg="#FFEEDD")
fecha_label.place(x=250, y=70)

cantidad_letras_label = Label(text="Cantidad en letras: ", bg="#FFEEDD")
cantidad_letras_label.place(x=22, y=100)

dinero_label = Label(text="$. ", bg="#FFEEDD")
dinero_label.place(x=500, y=100)

concepto_label = Label(text="En concepto de : ", bg="#FFEEDD")
concepto_label.place(x=25, y=130)

nombre_cuenta_label = Label(text="Nombre de la cuenta ", bg="#FFEEDD")
nombre_cuenta_label.place(x=22, y=180)

num_cuenta_label = Label(text="No. de la cuenta ", bg="#FFEEDD")
num_cuenta_label.place(x=200, y=180)

debito_label = Label(text="Debito ", bg="#FFEEDD")
debito_label.place(x=360, y=180)

credito_label = Label(text="Credito", bg="#FFEEDD")
credito_label.place(x=500, y=180)

banco_label = Label(text="Banco: ", bg="#FFEEDD")
banco_label.place(x=40, y=340)

solicitado_label = Label(text="Solicitado por: ", bg="#FFEEDD")
solicitado_label.place(x=40, y=365)

autorizado_label = Label(text="Autorizado por: ", bg="#FFEEDD")
autorizado_label.place(x=40, y=390)

confeccionado_label = Label(text="Confeccionado por: ", bg="#FFEEDD")
confeccionado_label.place(x=40, y=415)



nombre = StringVar()
fecha = StringVar()
cantidad_letras = StringVar()
concepto = StringVar()
nombre_cuenta = StringVar()
num_cuenta = StringVar()
debito = StringVar()
credito = StringVar()
dinero = StringVar()
banco = StringVar()
solicitado = StringVar()
autorizado = StringVar()
confeccionado = StringVar()

nombre_entry = Entry(textvariable=nombre, width="20")
fecha_entry = Entry(textvariable=fecha, width="20")
cantidad_letras_entry = Entry(textvariable=cantidad_letras, width="40")
concepto_entry = Entry(textvariable=concepto, width="40")
nombre_cuenta_entry= Entry(textvariable=nombre_cuenta, width="20")
num_cuenta_entry= Entry(textvariable=num_cuenta, width="20")
debito_entry= Entry(textvariable=debito, width="20")
credito_entry= Entry(textvariable=credito, width="20")
dinero_entry = Entry(textvariable=dinero, width="10")
banco_entry = Entry(textvariable=banco, width="20")
solicitado_entry = Entry(textvariable=solicitado, width="20")
autorizado_entry = Entry(textvariable=autorizado, width="20")
confeccionado_entry = Entry(textvariable=confeccionado, width="20")


nombre_entry.place(x=95, y=70)
fecha_entry.place(x=295, y=70)
cantidad_letras_entry.place(x=130, y=100)
concepto_entry.place(x=130, y=130)
nombre_cuenta_entry.place(x=22, y=200)
num_cuenta_entry.place(x=190, y=200)
debito_entry.place(x=460, y=200)
credito_entry.place(x=330, y=200)
dinero_entry.place(x=520, y=100)
banco_entry.place(x=95, y=342)
solicitado_entry.place(x=125, y=365)
autorizado_entry.place(x=135, y=390)
confeccionado_entry.place(x=150, y=415)


# Submit Button
submit_btn = Button(mywindow,text = "Subir", width = "10", height = "2", command = send_data, bg = "#F5C6AA")
submit_btn.place(x = 22, y = 490)

mywindow.mainloop()



