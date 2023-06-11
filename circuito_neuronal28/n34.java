//1000 neuronas
public class Neurona {
    private double peso;
    private List<Neurona> neuronasSiguientes;
    
    public Neurona(double peso) {
        this.peso = peso;
        this.neuronasSiguientes = new ArrayList<>();
    }
    
    public void agregarNeuronaSiguiente(Neurona neuronaSiguiente) {
        this.neuronasSiguientes.add(neuronaSiguiente);
    }
    
    public double activar(double entrada) {
        // Aplicar una función de activación, por ejemplo, la función sigmoide
        double activacion = 1 / (1 + Math.exp(-entrada * peso));
        
        for (Neurona neurona : neuronasSiguientes) {
            // Propagar la activación a cada una de las neuronas siguientes
            neurona.activar(activacion);
        }
        
        // Retornar la activación
        return activacion;
    }
}

public class Main {
    public static void main(String[] args) {
        List<Neurona> neuronas = new ArrayList<>();
        
        // Crear las 1000 neuronas y agregarlas a la lista
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
        
        // Propagar la entrada a través de las neuronas
        double salida = neuronas.get(0).activar(entrada);
        
        System.out.println("Salida de la red neuronal: " + salida);
    }
}
