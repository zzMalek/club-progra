## se debe calcular el costo de un masaje para enviarlo por telegrafo. para esto se sabe que cada letra cuesta 1 peso, los 
# caracteres especiales que no sean letras cuestan 3 y los digitos tienen un valor de 2 cada no. los espacios no tienen 
#valor y las letras del castellano (ñ,á,é,í,ó,ú) se consideran caracteres especiales 



esp = {"ñ","á","é","í","ó","ú"}
mensaje = str (input("ingrese su mensaje: "))

costo = 0


for letra in mensaje:
    if (letra.isdigit()):
        costo += 2
    elif (letra.isalpha() and letra not in esp):
        costo+= 1
    
    elif not letra.isspace() or letra in esp :
        costo+= 3
       
        

print (f"el costo es: ${costo}")
    

