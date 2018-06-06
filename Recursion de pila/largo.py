#Entrada: es un numero entero
#Restricciones: es un entero mayor a cero
#Salida: suma de los digitos

#Codigo de comprobacion (comprueba las restricciones que debe llevar el numero)
def largo (num):
    if isinstance (num,int) and (num >= 0):
        return largo_aux (abs(num))
    else:
        return "Error"

#Codigo de funcion (ejecuta la operacion)
def largo_aux (num):
    if (num == 0):
        return 0
    else:
        return 1 + largo_aux (num // 10)
