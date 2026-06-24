
#lista temporal de personajes
personajes = []

def buscar(nombre):
    for i in range(len(personajes)):
        if personajes[i]["nombre"]==nombre:
            return i #retorna la posicion del personaje
    return -1 #si el personaje no se encuentra es -1

def agregar(nombre,clase,nivel,rango):

    if len(nombre.strip())==0 or len(nombre.strip())>20:
        print("nombre no valido")
        return
    elif buscar(nombre)>=0:
        print("nombre ya existe")
        return
    elif clase not in ("Guerrero", "Mago", "Picaro"):
        print("clase no valida, debe ser Guerrero, Mago, Picaro")
        return
    elif nivel<= 0 or nivel >50:
        print("El nivel debe estar entre 1 y 50")
        return

    rango= "recluta"
    if rango>=30: rango = "elite"
    pj={"nombre":nombre,"clase":clase,"nivel":nivel,"rango":rango}
    personajes.append(pj)
    print("Personaje registrado")