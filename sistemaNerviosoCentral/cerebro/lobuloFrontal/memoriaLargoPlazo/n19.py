from red_neuronal import Neurona

class Neuro(Neurona):
    def __init__(self):
        super().__init__(peso=1.9)  # Peso diferente para n19

    def activar(self, entrada, orden, daño_humano):
        # Lógica específica para n19
        print("Activando neurona n19")
        
        # Llamar al método de activación de la clase base
        activacion = super().activar(entrada, orden, daño_humano)

        # Almacenar el recuerdo de la activación
        self.almacenar_recuerdo(activacion)
        
        return activacion

    def almacenar_recuerdo(self, activacion):
        # Lógica para almacenar el recuerdo
        ruta_directorio = "recuerdos"  # Carpeta donde se guardarán los recuerdos
        nombre_archivo = f"{ruta_directorio}/recuerdo_n19.csv"

        # Crear el directorio si no existe
        import os
        if not os.path.exists(ruta_directorio):
            os.makedirs(ruta_directorio)

        with open(nombre_archivo, "a") as f:
            f.write(f"{activacion}\n")  # Almacenar la activación en un archivo
            print(f"Recuerdo almacenado en: {nombre_archivo}")
