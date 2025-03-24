import json
import funciones
animales = r"c:\Users\angel\Desktop\Visual\ProyectoJson\animales.json"

try:
    with open(animales, 'r', encoding='utf-8') as file:
        data = json.load(file)  
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{animales}'")
    exit()
except json.JSONDecodeError:
    print(f"Error: El archivo '{animales}' tiene un formato inválido")
    exit()
def mostrar_menu():
    print("\n")
    print("Menú de opciones")
    print("1. Listar información")
    print("2. Contar población")
    print("3. Filtrar por peso")
    print("4. Buscar por alimento")
    print("5. Continente y población")
    print("6. Salir")
def main():
    continuar = True
    while continuar == True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            funciones.listar_informacion(data)

        elif opcion == "2":
            funciones.contar_poblacion(data)

        elif opcion == "3":
            funciones.filtrar_por_peso(data)

        elif opcion == "4":
            funciones.buscar_por_alimento(data)
        
        elif opcion == "5":
            funciones.continente_poblacion(data)

        elif opcion == "6":
            print("Saliendo del programa...")
            continuar = False
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()