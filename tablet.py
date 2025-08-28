
class Tablet:
    # Esta es nuestra clase principal que representa una tablet
    # Atributos de la clase
    def __init__(self, pulgadas, archivos, marca, color_fondo, almacenamiento=128, bateria=100):
        # Elegimos estos atributos porque son las características más importantes
        self.__pulgadas = pulgadas          # Tamaño de pantalla
        self.__archivos = archivos          # Cuántos archivos tiene guardados
        self.__marca = marca 
        self.__color_fondo = color_fondo# Samsung, iPad, etc.
        self.__almacenamiento = almacenamiento  # Este es nuestro atributo OPCIONAL (128GB por defecto)
        self.__bateria = bateria            # Porcentaje de batería (100% por defecto)
    
   
    def get_pulgadas(self):
        # Devuelve el tamaño de pantalla
        return self.__pulgadas
    
    def get_archivos(self):
        # Devuelve cuántos archivos tiene
        return self.__archivos
    
    def get_almacenamiento(self):
        # Devuelve la capacidad total de almacenamiento
        return self.__almacenamiento
    
    def get_marca(self):
        # Devuelve la marca de la tablet
        return self.__marca
    
    def get_color(self):
        # Devuelve el tamaño de pantalla
        return self.__color_fondo
    
    def get_bateria(self):
        # Devuelve el porcentaje actual de batería
        return self.__bateria
    
    # COMPORTAMIENTO 1: Usar la tablet (gasta batería)
   
    def usar_tablet(self):
        if self.__bateria >= 5:  # Si tiene al menos 5% de batería
            self.__bateria -= 5  # Le restamos 5
            return f"Usando tablet... Batería: {self.__bateria}%"
        else:
            # Si tiene menos del 5%, se apaga
            self.__bateria = 0
            return "Tablet sin batería. Necesita cargar."
    
    # COMPORTAMIENTO 2: Cargar la batería

    def cargar_bateria(self):
        if self.__bateria < 100:  # Si no está completa
            self.__bateria = min(100, self.__bateria + 10)  # Suma 10 pero no pasa de 100
            return f"Cargando... Batería: {self.__bateria}%"
        else:
            return "Batería completa (100%)"
    
    # COMPORTAMIENTO 3: Calcular espacio usado
   
    def calcular_espacio_usado(self, tamaño_promedio=2):
        espacio_usado = self.__archivos * tamaño_promedio  # Multiplicamos archivos x 2GB
        espacio_libre = self.__almacenamiento - espacio_usado  # Restamos del total
        porcentaje_usado = (espacio_usado / self.__almacenamiento) * 100  # Calculamos %
        
        # Devolvemos un diccionario con toda la info
        return {
            "espacio_usado": espacio_usado,
            "espacio_libre": max(0, espacio_libre),  # No puede ser negativo
            "porcentaje_usado": min(100, porcentaje_usado)  # No puede ser más de 100%
        }
    
    # MÉTODO MÁGICO 1: 
    def __str__(self):
        info_almacenamiento = self.calcular_espacio_usado()  # Usamos nuestro método
        # Devolvemos un string con toda la info importante de la tablet
        return (f"Tablet {self.__marca} - {self.__pulgadas}\" | "
                f"Batería: {self.__bateria}% | "
                f"Archivos: {self.__archivos} | "
                f"Almacenamiento: {info_almacenamiento['espacio_usado']}GB/"
                f"{self.__almacenamiento}GB usado")
    
    # MÉTODO MÁGICO 2: 
    def __len__(self):
        return self.__archivos
    
    # MÉTODO MÁGICO 3: 
    def __add__(self, otra_tablet):
        # Verificamos que sea realmente una tablet
        if isinstance(otra_tablet, Tablet):
            total_archivos = self.__archivos + otra_tablet.__archivos
            return f"Total de archivos combinados: {total_archivos}"
        else:
            return "Error: Solo se pueden sumar tablets"
# comentario nuevo jocy..