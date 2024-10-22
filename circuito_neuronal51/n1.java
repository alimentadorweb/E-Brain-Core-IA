import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class Neurona {
    private double peso;
    private List<Neurona> neuronasSiguientes;
    private int id; // ID único para cada neurona

    public Neurona(double peso, int id) {
        this.peso = peso;
        this.neuronasSiguientes = new ArrayList<>();
        this.id = id; // Asignar el ID único
    }

    public void agregarNeuronaSiguiente(Neurona neuronaSiguiente) {
        this.neuronasSiguientes.add(neuronaSiguente);
    }

    public double activar(double entrada) {
        // Aplicar la función de activación (sigmoide)
        double activacion = 1 / (1 + Math.exp(-entrada * peso));
        
        // Guardar la activación en un archivo CSV
        guardarActivacionEnCSV(activacion);

        // Propagar la activación a las neuronas siguientes
        for (Neurona neurona : neuronasSiguientes) {
            neurona.activar(activacion);
        }

        return activacion;
    }

    // Método para guardar la activación en un archivo CSV con ID único
    private void guardarActivacionEnCSV(double activacion) {
        // Crear carpeta /recuerdos si no existe
        File directorio = new File("recuerdos");
        if (!directorio.exists()) {
            directorio.mkdir(); // Crea la carpeta
        }

        // Nombre del archivo con el ID único
        String nombreArchivo = "recuerdos/neurona_" + id + ".csv";

        // Guardar activación en el archivo
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(nombreArchivo, true))) {
            writer.write(String.valueOf(activacion));
            writer.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
