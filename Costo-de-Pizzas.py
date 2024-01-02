from datetime import timedelta, datetime
now = datetime.now()

# Inicialización 

productos ={
    'Pequeña': 'P',
    'Mediana': 'M',
    'Grande': 'G',
    'precio_1': 80,
    'precio_2': 150,
    'precio_3': 280,
    'ing_1': 35,
    'ing_2': 55
}
lista_pedido = []
costo_total = 0

# Entradas del usuario

tamano_pizza_pedido = input("¿Qué tamaño de pizza quieres? (P, M o G):\n")
queso_extra = input("¿Vas a querer queso extra? (S o N): ")
peperoni_extra = input("¿Tu orden incluye peperoni extra también? (S o N): ")

# Preguntando tamaño de pizzas:

if tamano_pizza_pedido == productos['Pequeña']:
    costo_total += productos['precio_1']
    lista_pedido.append("1 Pizza Pequeña")

elif tamano_pizza_pedido == productos['Mediana']:
    costo_total += productos['precio_2']
    lista_pedido.append("1 Pizza Mediana")

elif tamano_pizza_pedido == productos['Grande']:
    costo_total += productos['precio_3']
    lista_pedido.append("1 Pizza Grande")

else:
    print("¡Asegurate de usar las letras especificadas!")

# Preguntando si quiere queso extra:

if queso_extra == "S":
    costo_total += productos["ing_1"]
    lista_pedido.append("1 Queso extra")

elif queso_extra == "N":
    costo_total
    
else:
    print("¡Responde la pregunta con si o no!")

# Preguntadno si quiere peperoni extra:

if peperoni_extra == "S":
    costo_total += productos["ing_2"]
    lista_pedido.append("1 Peperoni extra")

elif peperoni_extra == "N":
    costo_total

else:
    print("¡Responde la pregunta con si o no!")

print(f"""
--------------------------------              
PIZZERÍA Baches de Amalucan te atendió el
{now}
Tu pedido fue:""")

for producto in lista_pedido:
    print(producto)

print(f"""--------------------------------
Total: {costo_total}""")