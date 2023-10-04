import math

def CorredorComa(val):
    valor = ""
    n = 0
    if (val.count('.') == 1):    
        lk = val.split('.')
    else:
        lk[0] = val
        lk[1] = ""     
    lp = str(lk[0])
    lq = str(lk[1])    
    # Cuando n es positivo
    if ((str(lp)) != "0"):
        while((len(lp)) != 1):
            if (lp[len(lp) - 1] == "1"):
                lq = "1" + lq                
            else:
                if (lp[len(lp) - 1] == "0"):
                    lq = "0" + lq
            lp = lp[:-1]
            n += 1
        valor = lq        
        
    # Cuando n es negativo    
    else:
        i = 0
        lp = ""
        b = True       
        while(b):            
            if (lq[i] == "1"):
                b = False
            i += 1
        lp = lq[i:]
        n = (-1) * i
        valor = lp      
          
    return [ valor , str(n) ]

def Decimal_a_Binario(ing_data, topbit):
    pol = [ '0' , '1' ]
    valor = ""
    lk = list()
    num = float(ing_data)
            
    if (num < 0):
        num *= (-1)
    v = str(num)
    if (v.count('.') == 1):    
        lk = v.split('.')
    else:
        lk[0] = v
        lk[1] = "0"         
    # calcular el entero       
    num = int(lk[0])
    while(num > 2):
        valor = str(pol[int(num % 2)]) + valor
        num /= 2
    valor = str(pol[int(num % 2)]) + valor    
    # calcular el decimal
    if (float(lk[1]) != 0.0):
        valor += "."
        fnum = float(str("0." + (str(lk[1]))))
        i = len(valor) - 1
        while((fnum > 0.0) and (i < topbit)):
            fnum *= 2
            if (fnum >= 1):            
                valor += "1"
                fnum -= 1.0 
            else:
                valor += "0"
            i += 1    
    return (valor)

def Decimal_a_Base_N(type_base, entero, decima, base):
    num = str("")
    Intero = int(entero)
    
    while(Intero >= base):
        num = str(type_base[int(Intero % base)]) + num
        Intero /= base
    num = str(type_base[int(Intero)]) + num        
    if ((int(decima)) != 0):
        num += "."
        i = 0
        Decima = float("0." + decima)   
        while((Decima != 0.0) and (i < 32)):
            Decima *= base
            r = str(Decima)
            rem = r[0]
            num += r[0]
            r = r.replace(rem,"0")
            Decima = float(r)
            i += 1
            
    return (num)

def Base_N_a_Decimal(type_base, entero, decima, base):
    n = t = len(entero) - 1
    num = 0
    
    while(n >= 0):
        f = entero[n]
        i = 0
        while((i < base) and (entero[n] != type_base[i])):
            i += 1
        num += i * (math.pow(base, (t - n)))
        n -= 1
    if (decima != ""):
        n = 0
        while(n < (len(decima))):
            i = 0
            while(i < base) and (decima[n] != type_base[i]):
                i += 1
            num += i * (math.pow(base, (-1) * (n + 1)))
            n += 1
    return num

def VerificarIngreso(type_base, valor, base):
    k = True
    i = 0
    j = 0
    while((i < (len(valor))) and (k == True)):
        while((j < base) and (valor[i] != type_base[j])):
            j += 1
        if (j < base):
            j = 0
            i += 1
        else:
            k = False
    return k

def IdentificarBase(opcion, base_n):
    tope = -1
    if (opcion == 0):
        tope = 10
    elif (opcion == 1):
        tope = 2
    elif (opcion == 2):
        tope = 8    
    elif (opcion == 3):
        try:
            tope = int(base_n) 
            if (tope >= 36):
                tope = -1
        except:
            tope = -1
    elif (opcion == 4):
        tope = 16
    return tope