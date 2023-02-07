#realizar una funcion que resiva como parametros una palabra y devuelva si es palindroma




def palindroma (frase):
    
    frase = frase.lower()
    frase = frase.replace(" ","")
    frase = frase.replace("á","a")
    frase = frase.replace("é","e")
    frase = frase.replace("í","i")
    frase = frase.replace("ó","o")
    frase = frase.replace("ú","u")
    
    a = 0
    n = len(frase) - 1
    
    for i in range (0, len(frase)):
        if frase[a] == frase[n]:
            a+=1 
            n-=1
        else:
            return False
    return True
        
            
frase =  (input("ingrese la frase: "))
        
    