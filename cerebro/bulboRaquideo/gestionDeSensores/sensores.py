# gestiondesensores/sensores.py

class SensorAuditivo:
    def capturar(self):
        # Lógica para capturar datos auditivos
        return "Datos auditivos capturados"

class SensorVision:
    def capturar(self):
        # Lógica para capturar datos visuales
        return "Datos visuales capturados"

class MotorMovimiento:
    def mover(self, accion):
        # Lógica para mover el motor según la acción
        print(f"Ejecutando acción: {accion}")