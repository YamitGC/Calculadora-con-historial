import os

historial_operaciones = []

VERDE = ("\033[32m")
ROJO = ("\033[31m")

def menu():
    while True:
        print("="*23)
        print("="*5,"CALCULADORA","="*5)
        print("="*23)
        print("\n1. Operaciones.")
        print("2. Historial.")
        print("3. Salir del programa.")

        opcion = input("\nSelecciona una opcion: ")
        if opcion == "1":
            operaciones()
        elif opcion == "2":
            historial()
        elif opcion == "3":
            print("\nSaliendo del programa...")
            break
        else:
            print(f"Opcion no válida. Intenta nuevamente.")

def limpiar_pantalla():
    os.system('clear')

def operaciones():
    limpiar_pantalla()
    global historial_operaciones # Damos permiso para modificar la lista
    
    try:
        num1 = float(input("Ingresa el primer dígito: "))
        num2 = float(input("Ingresa el segundo dígito: "))
        
        operacion = input("Ingresa el tipo de operacion ('+' '-' '*' '/'): ")

        # Historial añadido en cada paso
        if operacion == "+":
            resultado = num1 + num2
            print(f"El resultado de la operacion es: {resultado}\n")
            historial_operaciones.append(f"{num1} + {num2} = {resultado}")
            
        elif operacion == "-":
            resultado = num1 - num2
            print(f"El resultado de la operacion es: {resultado}\n")
            historial_operaciones.append(f"{num1} - {num2} = {resultado}")
            
        elif operacion == "*":
            resultado = num1 * num2
            print(f"El resultado de la operacion es: {resultado}\n")
            historial_operaciones.append(f"{num1} * {num2} = {resultado}")
            
        elif operacion == "/":
            if num2 == 0:
                print(f"{ROJO}Error. No se puede dividir entre 0.")
            else:
                resultado = num1 / num2
                print(f"El resultado de la operacion es: {resultado}\n")
                historial_operaciones.append(f"{num1} / {num2} = {resultado}")
        else:
            print("Error. Digita una de las operaciones correctas ('+' '-' '*' '/').")
            
    except ValueError:
        print(f"Error: Entrada no válida. Debes ingresar números.")

def historial():
    limpiar_pantalla()
    if not historial_operaciones:
        print("No hay operaciones registradas.\n")
        return False
    print("Lista de operaciones:\n")
    for registro in historial_operaciones:
        print("-" * 20)
        print(f"{registro}")
        print("-" * 20)
        
if __name__ == "__main__":
    menu()


