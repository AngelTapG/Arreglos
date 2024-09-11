departamentos = ["Ropa", "Deportes", "Juguetería"]
ventas = [[0]*12 for _ in range(3)]  

def insertar_ventas(departamento):
    if departamento in departamentos:
        index = departamentos.index(departamento)
        print(f"Inserte las ventas para el departamento de {departamento}:")
        for i in range(12):
            ventas[index][i] = float(input(f"Mes {i + 1}: "))
    else:
        print("Departamento no encontrado.")

def buscar_venta(departamento, mes):
    if departamento in departamentos and 1 <= mes <= 12:
        index = departamentos.index(departamento)
        print(f"Ventas del departamento de {departamento} en el mes {mes}: {ventas[index][mes - 1]}")
    else:
        print("Departamento o mes inválido.")

def eliminar_ventas(departamento):
    if departamento in departamentos:
        index = departamentos.index(departamento)
        ventas[index] = [0] * 12
        print(f"Ventas del departamento de {departamento} han sido eliminadas.")
    else:
        print("Departamento no encontrado.")

def mostrar_ventas():
    print("Ventas por Departamento (Mes 1 a Mes 12):")
    print(" " * 15 + "Mes 1  Mes 2  Mes 3  Mes 4  Mes 5  Mes 6  Mes 7  Mes 8  Mes 9  Mes 10 Mes 11 Mes 12")
    for i, departamento in enumerate(departamentos):
        print(f"{departamento: <10}:", end=" ")
        for j in range(12):
            print(f"{ventas[i][j]:7.2f}", end=" ")
        print() 

