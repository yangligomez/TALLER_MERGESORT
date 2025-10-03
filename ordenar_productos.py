import csv

# MERGE SORT 
def merge_sort(lista):
    """
    Ordena una lista de productos usando el algoritmo Merge Sort.
    Primero ordena por calificacion (descendente).
    Si la calificacion es igual, ordena por precio (ascendente).
    """
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return merge(izquierda, derecha)


def merge(izquierda, derecha):
    """
    Fusiona dos listas ordenadas de productos segun los criterios definidos.
    """
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        # Comparacion principal: calificacion (descendente)
        if izquierda[i]['calificacion'] > derecha[j]['calificacion']:
            resultado.append(izquierda[i])
            i += 1
        elif izquierda[i]['calificacion'] < derecha[j]['calificacion']:
            resultado.append(derecha[j])
            j += 1
        else:
            # Si la calificacion es igual, ordenar por precio (ascendente)
            if izquierda[i]['precio'] < derecha[j]['precio']:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


# LECTURA DEL CSV
productos = []
with open("productos.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        productos.append({
            "id": int(row["id"]),
            "nombre": row["nombre"],
            "precio": float(row["precio"]),
            "calificacion": int(row["calificacion"]),
            "stock": int(row["stock"])
        })

# ORDENAR
productos_ordenados = merge_sort(productos)

# MOSTRAR MEJORES 
print(" Mejores Productos:")
for p in productos_ordenados[:10]:  # Los 10 mejores
    print(f"{p['id']} | {p['nombre']} | Calificacion: {p['calificacion']} | Precio: ${p['precio']} | Stock: {p['stock']}")
