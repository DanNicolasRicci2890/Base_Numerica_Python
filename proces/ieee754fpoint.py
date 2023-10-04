from proces.calculus import *

def VerifIngresoData(opcion_in, ing_data):
    BaseIN = 1

    # analizar el ingreso.
    if (opcion_in == 0):  # decimal
        try:
            if ((str(ing_data).count(',')) <= 1):
                val = str(ing_data).replace(',','.')
                float(val)
            else:
                float(ing_data)                        
        except:
            BaseIN = -1                
    if (opcion_in != 0):  # simple 32 bits, 64 bits y 80 bits
        tope = 0
        if (opcion_in == 1):  # simple 32 bits
            tope = 32
        if (opcion_in == 2):  # simple 64 bits
            tope = 64            
        if (opcion_in == 3):  # simple 80 bits
            tope = 80                        
        try:
            if ((len(str(ing_data))) == tope):
                int(str(ing_data), 2)            
            else:
                BaseIN = -1            
        except:
            BaseIN = -1            
    return BaseIN


def Decimal_IEEE_754(ing_data, exp, mant):
    val = ""
    signo = ""
    exponente = ""
    mantisa = ""
    
    if (str(ing_data).count(',') == 1):
        val = str(ing_data).replace(',','.')
    else:
        val = str(ing_data)
#------------- calculo del signo -------------------
    if ((float(val)) < 0):
        signo += "1"
    else:
        signo += "0"      
    
#------------- calculo del exponente ---------------
    val = Decimal_a_Binario(val, mant)
    kt = CorredorComa(val)    
    exponente = Decimal_a_Base_N(list(['0' , '1']), str(exp + int(kt[1])), "0", 2)
    
#------------- calculo de la mantisa ---------------
    mantisa = str(kt[0]).ljust(mant, "0")
    return (signo + " " + exponente + " " + mantisa)

def IEEE_754_Decimal(ing_data, bit_exp, bit_mant):
    signo = str(ing_data)[0]
    exponente = str(ing_data)[1:bit_exp + 1]
    mantisa = str(ing_data)[bit_exp + 1:] 
    
    exp = (int(Base_N_a_Decimal(list(['0','1']), exponente, "", 2))) - (int((2 ** (bit_exp - 1)) - 1))
    
    if (exp >= 0):
        vk = "1"
        i = 0
        while(i < exp):
            vk += mantisa[0]
            mantisa = mantisa[1:]
            i += 1
        vk = vk + "." + mantisa
        mantisa = vk        
    
    if (exp < 0):
        pass
    
    pol = mantisa.split('.')
    valor = float(Base_N_a_Decimal(list(['0','1']), str(pol[0]), str(pol[1]), 2))
    if (signo == "1"):
        valor *= (-1)
    return (str(valor))
    