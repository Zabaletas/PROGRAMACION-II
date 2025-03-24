public class POOEstadistica {
    // Atributos
    private double[] datos;
    // Constructor
    public POOEstadistica(double[] datos) {
        this.datos = datos;
    }
    public double promedio() {
        double suma = 0;
        for (double dato : datos) {
            suma += dato;
        }
        return suma / datos.length;
    }
    public double desviacion() {
        double promedio = promedio();
        double sumaCuadrados = 0;
        for (double dato : datos) {
            sumaCuadrados += Math.pow(dato - promedio, 2);
        }
        return Math.sqrt(sumaCuadrados / (datos.length - 1));
    }
    public static void main(String[] args) {
        double[] datos = {1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2};
        // Crear un objeto de la clase Estadistica
        POOEstadistica estadisticas = new POOEstadistica(datos);
        // Calcular y mostrar el promedio
        double promedio = estadisticas.promedio();
        System.out.println("El promedio es " + promedio);
        // Calcular y mostrar la desviación estándar
        double desviacion = estadisticas.desviacion();
        System.out.println("La desviación estándar es " + desviacion);
    }
}