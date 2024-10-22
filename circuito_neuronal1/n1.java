import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Neurona {
    private double peso;
    private List<Neurona> neuronasSiguientes;
    private static LeyesDeProteccionHumana leyes = new LeyesDeProteccionHumana();
    private static int contadorRecuerdos = 0; // Contador para los recuerdos

    public Neurona(double peso) {
        this.peso = peso;
        this.neuronasSiguientes = new ArrayList<>();
    }

    public void agregarNeuronaSiguiente(Neurona neuronaSiguiente) {
        this.neuronasSiguientes.add(neuronaSiguientes);
    }

    public double activar(double entrada, String orden, boolean dañoHumano) {
        // Evaluar las leyes de protección antes de proceder
        if (!leyes.evaluarLeyes("Activar neurona", orden, dañoHumano)) {
            return 0; // No se permite la activación
        }

        // Aplicar la función de activación (sigmoide)
        double activacion = 1 / (1 + Math.exp(-entrada * peso));

        // Almacenar el recuerdo de la activación
        almacenarRecuerdo(activacion);

        // Propagar la activación a las neuronas siguientes
        for (Neurona neurona : neuronasSiguientes) {
            neurona.activar(activacion, orden, dañoHumano);
        }

        return activacion;
    }

    private void almacenarRecuerdo(double activacion) {
        String rutaDirectorio = "recuerdos"; // Carpeta donde se guardarán los recuerdos
        File directorio = new File(rutaDirectorio);
        if (!directorio.exists()) {
            directorio.mkdir(); // Crear la carpeta si no existe
        }

        String nombreArchivo = rutaDirectorio + "/recuerdo_" + contadorRecuerdos++ + ".csv";

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(nombreArchivo))) {
            writer.write("Activación");
            writer.newLine();
            writer.write(String.valueOf(activacion));
            System.out.println("Recuerdo almacenado en: " + nombreArchivo);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
