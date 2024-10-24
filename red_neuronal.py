import importlib.util
import os
import math

   

class LeyesDeProteccionHumana:
    @staticmethod
    def evaluar_leyes(accion, orden, daño_humano, peligro_robot=False):
        # Ley 1: No dañar a un ser humano
        if daño_humano:
            print("Acción prohibida: Dañar a un ser humano.")
            return False

        # Ley 2: Obedecer órdenes humanas
        if orden:
            print(f"Orden recibida: {orden}")
            # Aquí puedes añadir lógica adicional para evaluar la orden

        # Ley 3: Proteger la propia existencia del robot
        if peligro_robot:
            print("Acción prohibida: Poner en peligro la vida del robot.")
            return False

        print(f"Acción permitida: {accion}")
        return True  # Si todas las condiciones se cumplen, la acción es permitida


class RedNeuronal:
    def __init__(self):
        self.neuronas = []

    def cargar_neurona(self, nombre_archivo):
        ruta = f"neurona/{nombre_archivo}.py"
        if os.path.exists(ruta):
            spec = importlib.util.spec_from_file_location(nombre_archivo, ruta)
            neurona_mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(neurona_mod)

            # Crear una instancia de la neurona y agregarla a la lista
            neurona_instance = neurona_mod.Neuro()  # Asegúrate de que la clase se llama 'Neuro'
            self.neuronas.append(neurona_instance)

    def activar_neuronas(self, entrada, orden, daño_humano):
        for neurona in self.neuronas:
            neurona.activar(entrada, orden, daño_humano)

class Neurona:
    contador_recuerdos = 0  # Contador para los recuerdos

    def __init__(self, peso):
        self.peso = peso
        self.n1_siguientes = []  # Otras neuronas a las que se conecta
        self.leyes = LeyesDeProteccionHumana()

    def agregar_n1_siguiente(self, n1_siguiente):
        self.n1_siguientes.append(n1_siguiente)

    def activar(self, entrada, orden, daño_humano):
        # Evaluar las leyes de protección antes de proceder
        if not self.leyes.evaluar_leyes("Activar neurona", orden, daño_humano):
            return 0  # No se permite la activación

        # Aplicar la función de activación (sigmoide)
        activacion = 1 / (1 + math.exp(-entrada * self.peso))

        # Almacenar el recuerdo de la activación
        self.almacenar_recuerdo(activacion)

        # Propagar la activación a las n1 siguientes
        for n1 in self.n1_siguientes:
            n1.activar(activacion, orden, daño_humano)

        return activacion

    def almacenar_recuerdo(self, activacion):
        ruta_directorio = "recuerdos"  # Carpeta donde se guardarán los recuerdos
        if not os.path.exists(ruta_directorio):
            os.makedirs(ruta_directorio)  # Crear la carpeta si no existe

        nombre_archivo = f"{ruta_directorio}/recuerdo_{Neurona.contador_recuerdos}.csv"
        Neurona.contador_recuerdos += 1

        with open(nombre_archivo, 'w') as writer:
            writer.write("Activación\n")
            writer.write(f"{activacion}\n")
            print(f"Recuerdo almacenado en: {nombre_archivo}")
