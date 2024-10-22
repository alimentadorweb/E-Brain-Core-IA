public class leyesDeProteccionHumana {
    // Método para evaluar las leyes
    public static boolean evaluarLeyes(String accion, String orden, boolean dañoHumano) {
        // Ley 1: No dañar a un ser humano
        if (dañoHumano) {
            System.out.println("Acción prohibida: Dañar a un ser humano.");
            return false;
        }

        // Ley 2: Obedecer órdenes humanas
        if (orden != null && !orden.isEmpty()) {
            System.out.println("Orden recibida: " + orden);
            // Aquí puedes añadir lógica adicional para evaluar la orden
        }

        // Ley 3: Proteger la propia existencia
        // Implementa la lógica de protección si es necesario

        System.out.println("Acción permitida: " + accion);
        return true; // Si todas las condiciones se cumplen, la acción es permitida
    }
}