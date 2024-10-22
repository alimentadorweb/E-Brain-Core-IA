import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Neurona> neuronas = new ArrayList<>();
        
        // Crear las 100000 neuronas y agregarlas a la lista
        for (int i = 0; i < 1000; i++) {
            Neurona neurona = new Neurona(Math.random());
            neuronas.add(neurona);
        }
        
        // Establecer las conexiones entre las neuronas
        for (int i = 0; i < neuronas.size() - 1; i++) {
            Neurona neuronaActual = neuronas.get(i);
            Neurona neuronaSiguiente = neuronas.get(i + 1);
            neuronaActual.agregarNeuronaSiguiente(neuronaSiguiente);
        }
        
        double entrada = 0.9;
        String orden = "Actuar con cuidado";
        boolean dañoHumano = false;
        
        // Propagar la entrada a través de las neuronas
        double salida = neuronas.get(0).activar(entrada, orden, dañoHumano);
        
        System.out.println("Salida de la red neuronal: " + salida);
    }
}