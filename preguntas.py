"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    file=open("data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    suma=0
    for i in file:
        valor=int(i[1])
        suma=suma+valor
    return suma


def pregunta_02():
    file=open("data.csv", "r").readlines()
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
    lista.sort(reverse=False)
    return lista


def pregunta_03():
    file=open("data.csv", "r").readlines()
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
    lista.sort(reverse=False)
    return lista


def pregunta_04():
    file=open("data.csv", "r").readlines()
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
    lista.sort(reverse=False)
    return lista


def pregunta_05():
    file=open("data.csv", "r").readlines()
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
    tupla.sort(reverse=False)
    return tupla


def pregunta_06():
    file=open("data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    lista=[]
    for i in file:
        lista.append(i[4])
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
        for k in coso:
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
    tupla.sort(reverse=False)
    return tupla


def pregunta_07():
    file=open("data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    lista=[]
    #creo una lista que me trae todos los numeros me los organiza
    for i in file:
        if int(i[1]) not in lista:
            lista.append(int(i[1]))
    lista.sort(reverse=False)
    listafinal=[]
    auxiliar=[]
    # recorro los valores de mi lista con numeros 
    for m in lista:
    # recorro las letras de la lista
        for n in file:
            #condiciono si el numero en posicion 2 es = a mi n que es el numero de la lista de los numeros que cree 
            if int(n[1])==m:
            # me crea una lista con las letras que cumple
                auxiliar.append(n[0])
        listafinal.append(list(auxiliar))
        auxiliar.clear()    
    tupla=list(zip(lista, listafinal))
    tupla.sort(reverse=False)
    return tupla


def pregunta_08():
    file=open("data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    lista=[]
    #creo una lista que me trae todos los numeros me los organiza
    for i in file:
        if int(i[1]) not in lista:
            lista.append(int(i[1]))
    lista.sort(reverse=False)
    listafinal=[]
    auxiliar=[]
    # recorro los valores de mi lista con numeros 
    for m in lista:
    # recorro las letras de la lista
        for n in file:
            #condiciono si el numero en posicion 2 es = a mi n que es el numero de la lista de los numeros que cree 
            if int(n[1])==m:
            # me crea una lista con las letras que cumple
                auxiliar.append(n[0])
        listafinal.append(list(set((auxiliar))))
        auxiliar.clear()
    tupla=list(zip(lista, listafinal))
    tupla.sort(reverse=False)
    return tupla


def pregunta_09():
    file=open("data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    lista=[]
    #saco toda la columna 5 
    for i in file:
        lista.append(i[4])
    maindict=[row.split(",")for row in lista]
    #Creo una lista de toda la columna 5 larga
    coso2=[]
    for i in maindict:
        coso2.extend(i)
    final=[]
    #creo las claves
    for j in coso2:
        if j[:3]not in final:
            final.append(j[:3])
    final.sort(reverse=False)
    coso2=[z.split(":") for z in coso2]
    #itero si i esta en final y x esta en coso2 ub0 entonces contardor aumenta
    contador={}
    for i in final:
        for x in coso2:
            if i == x[0]:
                elemento=x[0]
                if elemento in contador.keys():
                    contador[elemento]=contador[elemento]+1
                else:
                    contador[elemento]=1
    dicci=dict(zip(contador.keys(), contador.values()))
    return dicci


def pregunta_10():
    file=open("data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    #aqui con un lend
    lista1=[]
    lista2=[]
    lista3=[]
    #creo una lista para cada columna 1 4 y 5
    for i in file:
        lista1.append(i[0])
        lista2.append(i[3])
        lista3.append(i[4])
    # saco las comas para la columna 4 y 5 para poder separar por elementos
    lista2=[row.split(",")for row in lista2]
    lista3=[row.split(",")for row in lista3]
    lista4=[]
    #saco la cantidad de elementos de las columnas 4 y 5
    for i in lista2:
        lista4.append(len(i))
    lista5=[]
    for k in lista3:
        lista5.append(len(k))
    listafinal=list(zip(lista1,lista4,lista5))
    return listafinal


def pregunta_11():
    file=open("data.csv", "r").readlines()
    file=[z.replace("\n","")for z in file]
    file=[z.replace("\t",";")for z in file]
    file=[z.split(";") for z in file]
    #saco la columna 4 y la separo
    lista=[]
    lista2=[]
    for i in file:
        lista.append(i[3]) 
        lista2.append(i[1])
    lista=[row.split(",")for row in lista]
    #cree una lista nueva con los numeros de la columna 2 y la nueva lista 
    lista3=list(zip(lista,lista2))
    #ahora creo la lista de claves
    lista4=[]
    listasuma=[]
    suma=0
    for j in lista3:
        #me saca las claves sin repetir aaaa bb cc dd ee ff etc
        for i in j[0]:
            if i[:3] not in lista4:
                lista4.append(i[:3])
    lista4.sort(reverse=False)
    #ahora si a iterar
    for l in lista4:
        for i in lista3:
            for k in i[0]:
                if k[:3]==l:
                    suma=suma+int(i[1])
        listasuma.append(suma)  
        suma=0
    dicci={}
    dicci=dict(zip(lista4,listasuma))
       
    return dicci


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
