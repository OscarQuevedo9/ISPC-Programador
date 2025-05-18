from dispositivos import listar_dispositivos, agregar_dispositivo, eliminar_dispositivo, buscar_dispositivo
from automatizacion import ejecutar_automatizacion

"""
def grupo(los_404_not_found):
    integrantes = [
        "Camolotto Alejo Nicolas - DNI 44.606.044",
        "Flores Lopez Giancarlo - DNI 95.113.172",
        "Quevedo Jorge Francisco - DNI 31.218.408",
        "Quevedo Oscar Alberto - DNI 34.839.723"
    ]

    print(f"Grupo: {los_404_not_found}")
    print("Integrantes:")
    for i, persona in enumerate(integrantes, 1):
        print(f"{i}. {persona}")

grupo("Los 404 Not Found")
"""

def mostrar_menu():
    print("\n--- Sistema SmartHome ---")
    print("1. Listar dispositivos")
    print("2. Buscar dispositivo")
    print("3. Agregar dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Ejecutar automatización")
    print("6. Salir")

def main():
    dispositivos = []

    while True:
        mostrar_menu()
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            listar_dispositivos(dispositivos)
        elif opcion == "2":
            buscar_dispositivo(dispositivos)
        elif opcion == "3":
            agregar_dispositivo(dispositivos)
        elif opcion == "4":
            eliminar_dispositivo(dispositivos)
        elif opcion == "5":
            ejecutar_automatizacion(dispositivos)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()