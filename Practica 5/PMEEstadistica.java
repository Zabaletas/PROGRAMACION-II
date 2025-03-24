public class PMEEstadistica {
    public static double promedio(double[] datos) {
        double suma = 0;
        for (double dato : datos) {
            suma += dato;
        }
        return suma / datos.length;
    }
    public static double desviacion(double[] datos) {
        double promedio = promedio(datos);
        double sumaCuadrados = 0;
        for (double dato : datos) {
            sumaCuadrados += Math.pow(dato - promedio, 2);
        }
        return Math.sqrt(sumaCuadrados / (datos.length - 1));
    }
    public static void main(String[] args) {
        // Valores de los datos (modificables directamente en el código)
        double[] datos = {1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2};
        // Calcular y mostrar el promedio
        double promedio = promedio(datos);
        System.out.println("El promedio es " + promedio);
        // Calcular y mostrar la desviación estándar
        double desviacion = desviacion(datos);
        System.out.println("La desviación estándar es " + desviacion);
    }
}