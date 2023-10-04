from headerbase import *

type_base = [ '0' , '1' , '2' , '3' , '4' , '5' 
            , '6' , '7' , '8' , '9' , 'a' , 'b' 
            , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' 
            , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' 
            , 'o' , 'p' , 'q' , 'r' , 's' , 't'
            , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
#-------------------------------------------------------------------
def Salir():
    preg = MessageBox.askokcancel("Aviso", "¿desea salir del programa?")
    if (preg == True):
        exit()
#-------------------------------------------------------------------
def CalculoBase():
    panel_PuntoFlotante.place_forget()
    panel_CalculoBase.place(x=0,y=0)
    LimpiarCLR()    
#-------------------------------------------------------------------
def PuntoFlotante():
    panel_CalculoBase.place_forget()
    panel_PuntoFlotante.place(x=0,y=0)
    LimpiarCLR()    
#-------------------------------------------------------------------
def HabilitBaseIng():
    if (opcion_ingreso.get() == 3):
        entry_base_ingreso.config(state="normal", background="white")
    else:
        entry_base_ingreso.config(state="disabled", background="grey")
        base_n_ingreso.set("")
#-------------------------------------------------------------------
def HabilitBaseOut():
    if (opcion_resultado.get() == 3):
        entry_base_resultado.config(state="normal", background="white")
    else:
        entry_base_resultado.config(state="disabled", background="grey")
        base_n_resultado.set("")
#-------------------------------------------------------------------

def CalculoProceso():
    salida = True
       
    # verificar si el ingreso de valor es correcto con la base ingresada
    if ((len(ing_valor.get())) != 0):
        
        # verifica si tiene cantidad de 1 o 0 en un punto o coma (debe tener una coma o un punto)
        if ((((str(ing_valor.get())).count(',')) <= 1) or (((str(ing_valor.get())).count('.')) <= 1)):
            
            entero = StringVar()
            decima = StringVar()
            # verificar si tiene un solo punto o coma
            if ((((str(ing_valor.get())).count(',')) == 1) or (((str(ing_valor.get())).count('.')) == 1)):
                t = ' '
                if (((str(ing_valor.get())).count(',')) == 1):
                    t = ','                    
                if (((str(ing_valor.get())).count('.')) == 1):
                    t = '.'
                l1 = (str(ing_valor.get())).split(t)
                entero.set(l1[0])
                decima.set(l1[1])   
            else:    
                # si no tiene ni punto y coma entonces igualamos entero = ing_valor y decima = ""
                entero.set(ing_valor.get())
                decima.set("")
            baseIN = IdentificarBase(opcion_ingreso.get(), base_n_ingreso.get()) 
            baseOUT = IdentificarBase(opcion_resultado.get(), base_n_resultado.get()) 
            if (baseIN != -1):
                if (baseOUT != -1):
                    if (VerificarIngreso(type_base, entero.get(), baseIN)):
                        if (VerificarIngreso(type_base, decima.get(), baseIN)):
                            gvalor = float(Base_N_a_Decimal(type_base, entero.get(), decima.get(), baseIN))
                            l1 = (str(gvalor)).split('.')
                            entero.set(l1[0])
                            decima.set(l1[1])
                            out_valor.set(Decimal_a_Base_N(type_base, entero.get(), decima.get(), baseOUT))
                            
                        else:
                            MessageBox.showerror("Error", "El valor ingresado es incorrecto") 
                            salida = False        
                    else:
                        MessageBox.showerror("Error", "El valor ingresado es incorrecto") 
                        salida = False
                else:
                    MessageBox.showwarning("Aviso", "La base de resultado es erronea") 
                    salida = False
            else:
                MessageBox.showwarning("Aviso", "La base de ingreso es erronea")  
                salida = False
        else:
            MessageBox.showwarning("Aviso", "el ingreso es incorrecto")  
            salida = False    
    else:
        MessageBox.showwarning("Aviso", "ingrese un valor")  
        salida = False
        
    if (salida == False):
        LimpiarCLR()            
#---------------------------------------------------------------------------------------
def LimpiarCLR():
    ing_valor.set("")
    out_valor.set("")
    opcion_ingreso.set(0)
    opcion_resultado.set(0)
    entry_base_ingreso.config(state="disabled", background="grey")
    entry_base_resultado.config(state="disabled", background="grey")
    base_n_ingreso.set("")
    base_n_resultado.set("") 
#---------------------------------------------------------------------------------------
def CalculoFlotante():
    salida = True
       
    # verificar si el ingreso de valor es correcto con la base ingresada
    if ((len(ing_valor.get())) != 0):
        BaseIn = 0
 
        # verifica si las dos bases tienen una correcta realicion con el valor de ingreso
        BaseIn = VerifIngresoData(opcion_ingreso.get(), ing_valor.get())
        if (BaseIn == 1):
            if (opcion_ingreso.get() == opcion_resultado.get()):
                out_valor.set(ing_valor.get())
            else:
                if ((opcion_ingreso.get() == 0) and (opcion_resultado.get() != 0)):
                    if (opcion_resultado.get() == 1):
                        out_valor.set(Decimal_IEEE_754(ing_valor.get(), 127, 23))         
                    if (opcion_resultado.get() == 2):
                        out_valor.set(Decimal_IEEE_754(ing_valor.get(), 1023, 52))           
                    if (opcion_resultado.get() == 3):
                        out_valor.set(Decimal_IEEE_754(ing_valor.get(), 16383, 64))                                                        
                else:
                    if ((opcion_ingreso.get() == 1) and (opcion_resultado.get() != 1)):
                        if (opcion_resultado.get() == 0):
                            out_valor.set(IEEE_754_Decimal(ing_valor.get(), 8, 23))
                        if (opcion_resultado.get() == 2):
                            out_valor.set(Decimal_IEEE_754(IEEE_754_Decimal(ing_valor.get(), 8, 23), 1023, 52))
                        if (opcion_resultado.get() == 3):
                            out_valor.set(Decimal_IEEE_754(IEEE_754_Decimal(ing_valor.get(), 8, 23), 16383, 64))                            
                    else:
                        if ((opcion_ingreso.get() == 2) and (opcion_resultado.get() != 2)):
                            if (opcion_resultado.get() == 0):
                                out_valor.set(IEEE_754_Decimal(ing_valor.get(), 11, 52))
                            if (opcion_resultado.get() == 1):
                                out_valor.set(Decimal_IEEE_754(IEEE_754_Decimal(ing_valor.get(), 11, 52), 127, 23))                            
                            if (opcion_resultado.get() == 3):
                                out_valor.set(Decimal_IEEE_754(IEEE_754_Decimal(ing_valor.get(), 11, 52), 16383, 64))                                  
                        else:
                            if ((opcion_ingreso.get() == 3) and (opcion_resultado.get() != 3)):
                                if (opcion_resultado.get() == 0):
                                    out_valor.set(IEEE_754_Decimal(ing_valor.get(), 15, 64))
                                if (opcion_resultado.get() == 1):
                                    out_valor.set(Decimal_IEEE_754(IEEE_754_Decimal(ing_valor.get(), 15, 64), 127, 23))                            
                                if (opcion_resultado.get() == 2): 
                                    out_valor.set(Decimal_IEEE_754(IEEE_754_Decimal(ing_valor.get(), 15, 64), 1023, 52))                              
        else:
            MessageBox.showwarning("Aviso", "ingrese un valor correcto")  
            salida = False        
    else:
        MessageBox.showwarning("Aviso", "ingrese un valor")  
        salida = False
        
    if (salida == False):
        LimpiarCLR() 
#---------------------------------------------------------------------------------------
# ventana de inicio
root = Tk()
root.title("Calculo de base")
root.maxsize(width=1100, height=600)
root.minsize(width=1100, height=600)

opcion_ingreso = IntVar() # tipo de base especifica de entrada
opcion_resultado = IntVar() # tipo de base especifica de salida
base_n_ingreso = StringVar() # base especial de ingreso
base_n_resultado = StringVar() # base especial de salida
ing_valor = StringVar() # valor de ingreso
out_valor = StringVar() # valor de salida

menubar = Menu(root)

#-----------------------------------------------------------------------------------------------------
panel_CalculoBase = PanedWindow(root, background="#FFFFCC")
panel_CalculoBase.config(width=1100, height=600)
label_ingreso = Label(panel_CalculoBase, text="Ingrese un valor")
label_ingreso.config(font=("Verdana", 16, "italic"), background="#FFFFCC")
label_ingreso.place(x=10, y=40)
entry_ingreso = Entry(panel_CalculoBase)
entry_ingreso.config(font=("Arial", 16, "bold"), justify="right", foreground="red", textvariable=ing_valor)
entry_ingreso.place(width=600, x=200, y=43)

frame_ingreso = Frame(panel_CalculoBase)
frame_ingreso.config(background="white")
frame_ingreso.place(width=280, height=230, x=530, y=90)
base_ingreso = Label(frame_ingreso, text="base de ingreso")
base_ingreso.config(font=("Verdana", 16, "italic"), background="#FFFFCC", foreground="red")
base_ingreso.place(x=60, y=10)
rb1i = Radiobutton(frame_ingreso, text="decimal", variable=opcion_ingreso, value=0, command=HabilitBaseIng)
rb2i = Radiobutton(frame_ingreso, text="binario", variable=opcion_ingreso, value=1, command=HabilitBaseIng)
rb3i = Radiobutton(frame_ingreso, text="octal", variable=opcion_ingreso, value=2, command=HabilitBaseIng)
rb4i = Radiobutton(frame_ingreso, text="base n", variable=opcion_ingreso, value=3, command=HabilitBaseIng)
rb5i = Radiobutton(frame_ingreso, text="hexadecimal", variable=opcion_ingreso, value=4, command=HabilitBaseIng)
rb1i.config(font=("Arial", 16), background="white", activeforeground="red")
rb2i.config(font=("Arial", 16), background="white", activeforeground="red")
rb3i.config(font=("Arial", 16), background="white", activeforeground="red")
rb4i.config(font=("Arial", 16), background="white", activeforeground="red")
rb5i.config(font=("Arial", 16), background="white", activeforeground="red")
rb1i.place(x=10, y=40)
rb2i.place(x=10, y=75)
rb3i.place(x=10, y=110)
rb4i.place(x=10, y=145)
rb5i.place(x=10, y=180)
entry_base_ingreso = Entry(frame_ingreso)
entry_base_ingreso.config(font=("Arial", 16, "bold"), justify="center", state="disabled", background="gray", textvariable=base_n_ingreso)
entry_base_ingreso.place(width=70, x=120, y=148)

frame_resultado = Frame(panel_CalculoBase)
frame_resultado.config(background="white")
frame_resultado.place(width=280, height=230, x=20, y=170)
base_resultado = Label(frame_resultado, text="base de resultado")
base_resultado.config(font=("Verdana", 16, "italic"), background="#FFFFCC", foreground="red")
base_resultado.place(x=60, y=10)
rb1o = Radiobutton(frame_resultado, text="decimal", variable=opcion_resultado, value=0, command=HabilitBaseOut)
rb2o = Radiobutton(frame_resultado, text="binario", variable=opcion_resultado, value=1, command=HabilitBaseOut)
rb3o = Radiobutton(frame_resultado, text="octal", variable=opcion_resultado, value=2, command=HabilitBaseOut)
rb4o = Radiobutton(frame_resultado, text="base n", variable=opcion_resultado, value=3, command=HabilitBaseOut)
rb5o = Radiobutton(frame_resultado, text="hexadecimal", variable=opcion_resultado, value=4, command=HabilitBaseOut)
rb1o.config(font=("Arial", 16), background="white", activeforeground="red")
rb2o.config(font=("Arial", 16), background="white", activeforeground="red")
rb3o.config(font=("Arial", 16), background="white", activeforeground="red")
rb4o.config(font=("Arial", 16), background="white", activeforeground="red")
rb5o.config(font=("Arial", 16), background="white", activeforeground="red")
rb1o.place(x=10, y=40)
rb2o.place(x=10, y=75)
rb3o.place(x=10, y=110)
rb4o.place(x=10, y=145)
rb5o.place(x=10, y=180)
entry_base_resultado = Entry(frame_resultado)
entry_base_resultado.config(font=("Arial", 16, "bold"), justify="center", state="disabled", background="gray", textvariable=base_n_resultado)
entry_base_resultado.place(width=70, x=120, y=148)

btn_calculo = Button(panel_CalculoBase, text = "Calcular", command=CalculoProceso)
btn_calculo.config(font=("Arial", 16, "bold"))
btn_calculo.place(width=200, height=50, x=200, y=410)

btn_borrado = Button(panel_CalculoBase, text = " Borrar ", command=LimpiarCLR)
btn_borrado.config(font=("Arial", 16, "bold"))
btn_borrado.place(width=200, height=50, x=430, y=410)


entry_resultado = Entry(panel_CalculoBase)
entry_resultado.config(font=("Arial", 16, "bold"), justify="left", state="disabled", background="gray", textvariable=out_valor)
entry_resultado.place(width=880, height=50, x=10, y=480)

#-----------------------------------------------------------------------------------------------------
panel_PuntoFlotante = PanedWindow(root, background="#FFFFCC")
panel_PuntoFlotante.config(width=1100, height=600)

label_ingreso2 = Label(panel_PuntoFlotante, text="Ingrese un valor")
label_ingreso2.config(font=("Verdana", 16, "italic"), background="#FFFFCC")
label_ingreso2.place(x=10, y=40)
entry_ingreso2 = Entry(panel_PuntoFlotante)
entry_ingreso2.config(font=("Arial", 16, "bold"), justify="right", foreground="red", textvariable=ing_valor)
entry_ingreso2.place(width=800, x=200, y=43)

frame_ingreso2 = Frame(panel_PuntoFlotante)
frame_ingreso2.config(background="white")
frame_ingreso2.place(width=340, height=190, x=530, y=90)
base_ingreso2 = Label(frame_ingreso2, text="base de ingreso")
base_ingreso2.config(font=("Verdana", 16, "italic"), background="#FFFFCC", foreground="red")
base_ingreso2.place(x=60, y=10)
rb1i2 = Radiobutton(frame_ingreso2, text="decimal", variable=opcion_ingreso, value=0)
rb2i2 = Radiobutton(frame_ingreso2, text="IEEE 754 simple        (32bits)", variable=opcion_ingreso, value=1)
rb3i2 = Radiobutton(frame_ingreso2, text="IEEE 754 compuesto (64bits)", variable=opcion_ingreso, value=2)
rb4i2 = Radiobutton(frame_ingreso2, text="IEEE 754 extendido   (80bits)", variable=opcion_ingreso, value=3)
rb1i2.config(font=("Arial", 16), background="white", activeforeground="red")
rb2i2.config(font=("Arial", 16), background="white", activeforeground="red")
rb3i2.config(font=("Arial", 16), background="white", activeforeground="red")
rb4i2.config(font=("Arial", 16), background="white", activeforeground="red")
rb1i2.place(x=10, y=40)
rb2i2.place(x=10, y=75)
rb3i2.place(x=10, y=110)
rb4i2.place(x=10, y=145)


frame_resultado2 = Frame(panel_PuntoFlotante)
frame_resultado2.config(background="white")
frame_resultado2.place(width=340, height=190, x=20, y=170)
base_resultado2 = Label(frame_resultado2, text="base de resultado")
base_resultado2.config(font=("Verdana", 16, "italic"), background="#FFFFCC", foreground="red")
base_resultado2.place(x=60, y=10)
rb1o2 = Radiobutton(frame_resultado2, text="decimal", variable=opcion_resultado, value=0)
rb2o2 = Radiobutton(frame_resultado2, text="IEEE 754 simple        (32bits)", variable=opcion_resultado, value=1)
rb3o2 = Radiobutton(frame_resultado2, text="IEEE 754 compuesto (64bits)", variable=opcion_resultado, value=2)
rb4o2 = Radiobutton(frame_resultado2, text="IEEE 754 extendido   (80bits)", variable=opcion_resultado, value=3)
rb1o2.config(font=("Arial", 16), background="white", activeforeground="red")
rb2o2.config(font=("Arial", 16), background="white", activeforeground="red")
rb3o2.config(font=("Arial", 16), background="white", activeforeground="red")
rb4o2.config(font=("Arial", 16), background="white", activeforeground="red")
rb1o2.place(x=10, y=40)
rb2o2.place(x=10, y=75)
rb3o2.place(x=10, y=110)
rb4o2.place(x=10, y=145)


btn_calculo2 = Button(panel_PuntoFlotante, text = "Calcular", command=CalculoFlotante)
btn_calculo2.config(font=("Arial", 16, "bold"))
btn_calculo2.place(width=200, height=50, x=200, y=370)

btn_borrado2 = Button(panel_PuntoFlotante, text = " Borrar ", command=LimpiarCLR)
btn_borrado2.config(font=("Arial", 16, "bold"))
btn_borrado2.place(width=200, height=50, x=430, y=370)


entry_resultado2 = Entry(panel_PuntoFlotante)
entry_resultado2.config(font=("Arial", 16, "bold"), justify="left", state="normal", background="gray", textvariable=out_valor)
entry_resultado2.place(width=1040, height=50, x=10, y=430)

#-----------------------------------------------------------------------------------------------------

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Calculo Base", command=CalculoBase)
filemenu.add_command(label="Punto Flotante", command=PuntoFlotante)
filemenu.add_command(label="Salir del programa", command=Salir)

menubar.add_cascade(menu=filemenu, label="Selector")
#-------------------------------------------------------------------

#-------------------------------------------------------------------
root.config(menu=menubar)
root.mainloop()
