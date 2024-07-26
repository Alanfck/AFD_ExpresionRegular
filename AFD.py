#           0   |   1
#.  q0  |   q1  |   q2
#.  q1  |   re  |   q1
#.  q2  |   q2  |   re
#.  re  |   re  |   re

# tambien puede verse como la funcion:
# delta(q0,0)=q1
# delta(q0,1)=q2
# delta(q1,0)=re
# delta(q1,1)=q1
# delta(q2,0)=q2
# delta(q2,1)=re
# delta(re,0)=re
# delta(re,1)=re



delta = {
    #llave: valor
    ("q0", 0): "q1",
    ("q0", 1): "q2",
    ("q1", 0): "re",
    ("q1", 1): "q1",
    ("q2", 0): "q2",
    ("q2", 1): "re",
    ("re", 0): "re",
    ("re", 1): "re",

}

transiciones = [["q1","q2"],["re","q1"],["q2","re"],["re","re"]]

lista = ["0011", "00", "001", "0111111", "100000","11", "1010", "1011", "101","1000"]

estado = "q0"   #estado Inicial

for cadena in lista:#agarramos cada cadena dentro de la lista
    # para leer uno por uno todos los valores de la cadena, si ponemos el if dentro de este for, estaria rechazando todo,
    # debido a que hara la condicion "estado == "q0" para cada valor sin dejar que termine de leer la cadena
    for letra in cadena:
        estado = delta[estado,int(letra)] #leemos la cadena letra por letra
    if estado == "q1" or estado == "q2":
        print("Estado Final:", estado)
        print("Cadena:", cadena)
        print("aceptado\n")

    else:
        print("Estado Final:", estado)
        print("Cadena:", cadena)
        print("no aceptado\n")
    estado = "q0"