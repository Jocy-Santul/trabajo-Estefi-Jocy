from tablet import Tablet

def mostrar_menu():
    #comentario de prueba
    # Función que muestra las opciones disponibles al usuario
    print("\n" + "-"*45)
    print("             TABLET")
    print("-"*45)
    print("1. Registrar otra tablet")
    print("2. Ver información de la tablet")
    print("3. Usar tablet (consumir batería)")
    print("4. Cargar batería")
    print("5. Ver el almacenamiento")
    print("6. Contar archivos (len)")
    print("7. Comparar tablets (suma de archivos)")
    print("8. Salir")
    print("-"*45)

def crear_tablet():
    # Función para crear una tablet nueva pidiendo datos al usuario
    print("\n--- REGISTRAR TABLET ---")
    try:
        # Pedimos los datos básicos
        marca = input("Ingrese la marca: ")
        color_fondo = input("Ingrese el color: ")
        pulgadas = float(input("Ingrese el tamaño en pulgadas: "))
        archivos = int(input("Ingrese la cantidad de archivos: "))
        
        # El almacenamiento es opcional - si no ingresa nada, usa 128GB por defecto
        almacenamiento = input("Ingrese almacenamiento en GB (presione Enter para 128GB): ")
        if almacenamiento:  # Si escribió algo
            almacenamiento = int(almacenamiento)
        else:  # Si no escribió nada, usa el valor por defecto
            almacenamiento = 128
            
        # Creamos y devolvemos la nueva tablet
        return Tablet(pulgadas, color_fondo, archivos, marca, almacenamiento)
    except ValueError:
        # Si ingresó algo mal (letras donde van números), mostramos error
        print("Error: Ingrese valores numéricos válidos")
        return None

def main():
    # Función principal - acá manejamos todo el programa
    tablet = None    # Variable para guardar la primera tablet
    tablet2 = None   # Variable para guardar la segunda tablet (para comparar)
    
    while True:  # Bucle infinito hasta que el usuario elija salir
        mostrar_menu()  # Mostramos las opciones
        
        try:
            opcion = input("\nSeleccione una opción (1-8): ")
            
            if opcion == "1":
                # Opción 1: Crear tablet
                nueva_tablet = crear_tablet()
                if nueva_tablet:  # Si se creó correctamente
                    if tablet is None:  # Si es la primera tablet
                        tablet = nueva_tablet
                        print("✓ Primera tablet creada exitosamente!")
                    else:  # Si ya hay una, esta es la segunda
                        tablet2 = nueva_tablet
                        print("✓ Segunda tablet creada exitosamente!")
            
            elif opcion == "2":
                # Opción 2: __str__
                if tablet:  # Si hay al menos una tablet
                    print(f"\n--- INFORMACIÓN DE LA TABLET ---")
                    print(tablet)  # Acá se ejecuta automáticamente __str__
                    if tablet2:  # Si hay segunda tablet, también la mostramos
                        print(f"\nSegunda tablet:")
                        print(tablet2)
                else:
                    print(" No hay tablets creadas. Use la opción 1 primero.")
            
            elif opcion == "3":
                # Opción 3: Usar tablet (nuestro COMPORTAMIENTO 1)
                if tablet:
                    resultado = tablet.usar_tablet()  # Llamamos al método
                    print(f"\n{resultado}")
                else:
                    print(" No hay tablets creadas. Use la opción 1 primero.")
            
            elif opcion == "4":
                # Opción 4: Cargar batería (nuestro COMPORTAMIENTO 2)
                if tablet:
                    resultado = tablet.cargar_bateria()  # Llamamos al método
                    print(f"\n{resultado}")
                else:
                    print(" No hay tablets creadas. Use la opción 1 primero.")
            
            elif opcion == "5":
                # Opción 5: Ver almacenamiento (nuestro COMPORTAMIENTO 3)
                if tablet:
                    info = tablet.calcular_espacio_usado()  # Llamamos al método
                    print(f"\n--- USO DE ALMACENAMIENTO ---")
                    print(f"Espacio usado: {info['espacio_usado']} GB")
                    print(f"Espacio libre: {info['espacio_libre']} GB")
                    print(f"Porcentaje usado: {info['porcentaje_usado']:.1f}%")
                else:
                    print(" No hay tablets creadas. Use la opción 1 primero.")
            
            elif opcion == "6":
                # Opción 6: Usar __len__ 
                if tablet:
                    cantidad = len(tablet) 
                    print(f"\n La tablet tiene {cantidad} archivos")
                else:
                    print(" No hay tablets creadas. Use la opción 1 primero.")
            
            elif opcion == "7":
                # Opción 7: Usa __add__ 
                if tablet and tablet2:  # Necesitamos las dos tablets
                    resultado = tablet + tablet2  # Acá se ejecuta __add__
                    print(f"\n{resultado}")
                elif tablet:  # Si solo hay una tablet
                    print(" Necesita crear una segunda tablet para compararlas.")
                else:
                    print(" No hay tablets creadas. Use la opción 1 primero.")
            
            elif opcion == "8":
                # Opción 8: Salir del programa
                print("Gracias por usar nuestro programa de crear tablets. Vuelva pronto!!")
                print("\n¡Chauuu!")
                break  # while
            
        except Exception as e:
            # Cualquier otro error 
            print(f" Error inesperado: {e}")
            
# Punto de entrada del programa - desde acá empieza todo
if __name__ == "__main__":
  main()  # Llamamos a la función principal
