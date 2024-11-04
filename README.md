# Cerebro Positronico IA 
# inteligencia artificial que replica un cerebro Humano, en su version digital
Proyecto open source, lenguaje de programacion en Python 3.0

Nota el  24 de Octubre de 2024 migramos de Java a Python la razon es el peso en kb que se generaba cuando el cerebro se ejecutaba creando un entorno imposible para la ejecucion en hardware robotico aun creando multiples hilos, ademas cambiamos el nombre de areadebroca_ia a cerebroPositronico_IA

Objetivo de proyecto, recrear un cerebro positronico, que ayude a conectar partes roboticas al cuerpo humano usando un casco y diferentes sensores

Para Ejecutar el Cerebro positronico Bastara este comando:  python -m bulboraquideo.bulbo_raquideo
 
 Resultado Esperado:
<code>
**Iniciando el Cerebro Positronico...**
**Iniciando captura de datos sensoriales...**
**Datos auditivos capturados**
**Datos visuales capturados**
**Datos sensoriales almacenados.**
**Ejecutando acción: mover a la derecha**
**Deteniendo captura de datos sensoriales...**
**Cerebro Positronico detenido.**
</code>

**HardWare Recomendado para hacer Pruebas.**

**Sensores Compatibles con Arduino:**

**Sensores Auditivos:**
Módulo KY-038 (sensor de sonido)
Módulo MAX9814 (micrófono amplificado)
Módulo LM393 (detector de sonido)
**Sensores Visuales:**
Módulo OV7670 (cámara VGA)
Sensor Pixy2 (cámara con procesamiento)
Módulo HC-SR04 (sensor ultrasónico para detección de distancia)
Fotoresistencias LDR (para detección de luz)
**Actuadores/Motores:**
Servomotores (para movimientos precisos)
Motores DC con driver L298N
Motores paso a paso con driver A4988
Módulo de relés para control de dispositivos
Placas Arduino Recomendadas:

**Arduino Mega 2560:**
Más pines y memoria que el Arduino UNO
Mejor para proyectos complejos
Más puertos seriales
**Arduino UNO:**
Bueno para prototipos iniciales
Compatible con la mayoría de shields
Fácil de programar

Ejemplo de codigo de conexion en Arduino hacia el cerebro positronico:

<code>
// Código para Arduino
void setup() {
  Serial.begin(9600);
  // Configurar pines para sensores y actuadores
}

void loop() {
  // Leer sensores
  int datosSensor = analogRead(A0);
  
  // Enviar datos al Cerebro Positrónico
  Serial.println(datosSensor);
  
  // Recibir comandos
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    // Ejecutar acción según el comando
  }
}
</code>

**Recomendaciones Adicionales:**

**Protección:**
Usa resistencias pull-up/pull-down según necesites
Protege los pines con resistencias limitadoras de corriente
Considera usar optoacopladores para aislar circuitos
**Alimentación:**
Usa una fuente de alimentación externa para los motores
Mantén separadas las tierras de potencia y señal
Considera usar capacitores de desacoplo
**Expansión:**
Puedes usar múltiples Arduinos para diferentes funciones
Considera usar un multiplexor para más sensores
I2C o SPI para comunicación con múltiples dispositivos

**Asegúrate de instalar la biblioteca pyserial en tu entorno virtual**

<code>pip install pyserial desde python </code>

David Arriaga | El Salvador, Centro America alimentadorweb@gmail.com

Simulacion de Recuerdos:
<img src="https://github.com/alimentadorweb/CerebroPositronicoIA/blob/main/cerebroIA.png" />
