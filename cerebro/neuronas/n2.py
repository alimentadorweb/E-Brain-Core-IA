from red_neuronal import Neurona  # Importa la clase Neurona

class Neuro(Neurona):  # Hereda de la clase Neurona
    def __init__(self):
        super().__init__(peso=0.2)  # Define un peso por defecto
        # Aquí puedes agregar más inicialización si es necesario

# Aquí puedes definir otras funciones específicas para esta neurona