public class PMEEcuacionesCuadraticas {
    public static double getDiscriminante(double a, double b, double c) {
        return b * b - 4 * a * c;
    }
    public static double getRaiz1(double a, double b, double discriminante) {
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }
    public static double getRaiz2(double a, double b, double discriminante) {
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }
    public static void main(String[] args) {
        double a = 1;
        double b = 2.0;
        double c = 1;
        // Calcular el discriminante
        double discriminante = getDiscriminante(a, b, c);
        // Mostrar resultados según el discriminante
        if (discriminante > 0) {
            double r1 = getRaiz1(a, b, discriminante);
            double r2 = getRaiz2(a, b, discriminante);
            System.out.println("La ecuación tiene dos raíces: " + r1 + " y " + r2);
        } else if (discriminante == 0) {
            double r1 = getRaiz1(a, b, discriminante);
            System.out.println("La ecuación tiene una raíz: " + r1);
        } else {
            System.out.println("La ecuación no tiene raíces reales");
        }
    }
}