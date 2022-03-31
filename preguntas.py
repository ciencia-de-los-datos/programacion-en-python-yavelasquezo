"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    file=open("/content/programacion-en-python-yavelasquezo/data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    suma=0
    for i in file:
        valor=int(i[1])
        suma=suma+valor
    return suma

def pregunta_02():
    file=open("/content/programacion-en-python-yavelasquezo/data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    contador={}
    for i in file:
        elemento=i[0]
        if elemento in contador.keys():
            contador[elemento] = contador[elemento]+1
        else:
            contador[elemento]=1
    lista=list(zip(contador.keys(), contador.values()))
    return lista


def pregunta_03():
    file=open("/content/programacion-en-python-yavelasquezo/data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    suma={}
    for i in file:
        elemento=i[0]
        if elemento in suma.keys():
            suma[elemento] = suma[elemento]+int(i[1])
        else:
            suma[elemento]=int(i[1])
    lista=list(zip(suma.keys(), suma.values()))
    return lista


def pregunta_04():
    file=open("/content/programacion-en-python-yavelasquezo/data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    #genero mi diccionario en 0
    contador={}
    #empiezo mi ciclo
    for i in file:
        #hago lista de la 3era fila
        elemento=i[2].split("-")
        #genero lista de solo los meses
        coso=elemento[1]
        #cuento segun el mes
        if coso in contador.keys():
            contador[coso]=contador[coso]+1
        else:
            contador[coso]=1
    lista=list(zip(contador.keys(),contador.values()))
  
  
    return lista


def pregunta_05():
    file=open("/content/programacion-en-python-yavelasquezo/data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    lista=[]
    for i in file:
        if i[0] not in lista:
            lista.append(i[0])
    lista.sort(reverse=False)
    listamin=[]
    listamax=[]
    for j in lista:
        maxia=0
        for k in file:
            if k[0]==j:
                if int(k[1])>maxia:
                    maxia=int(k[1])
        listamax.append(maxia)
        mini=maxia
        for k in file:
            if k[0]==j:
                if int(k[1])<mini:
                    mini=int(k[1])
        listamin.append(mini)
    tupla=list(zip(lista, listamax, listamin))
    return tupla


def pregunta_06():
    file=open("/content/programacion-en-python-yavelasquezo/data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    lista=[]
    xlista=[row.split(",")for row in lista]

    coso=[]
    for i in xlista:
        coso.append(i)
    final=[]
    for j in coso:
        if j[:3] not in final:
            final.append(j[:3])
    final.sort(reverse=False)
    listamin=[]
    listamax=[]
    auxiliar=[]

    for m in final:
        for k in coso2:
             if k[:3] ==m:
                auxiliar.append(int(k[4:]))  
        mini=min(auxiliar)
        maxi=max(auxiliar)
        listamin.append(mini)
        listamax.append(maxi)
        mini=0
        maxi=0
        auxiliar.clear()

    tupla=list(zip(final,listamin,listamax))
     return tupla


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    file=open("/content/programacion-en-python-yavelasquezo/data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    lista=[]
    xlista=[row.split(",")for row in lista]

    coso=[]
    for i in xlista:
        coso.append(i)
    final=[]
    for j in coso:
        if j[:3] not in final:
            final.append(j[:3])
    final.sort(reverse=False)
    
    contador={}
        for i in coso:
        elemento=i[0]
            if elemento in contador.keys():
                contador[elemento] = contador[elemento]+1
            else:
                contador[elemento]=1
    lista=list(zip(contador.keys(), contador.values()))

   
   
    return lista


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
