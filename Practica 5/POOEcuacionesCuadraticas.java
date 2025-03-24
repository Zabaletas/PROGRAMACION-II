public class POOEcuacionesCuadraticas {
    // Atributos
    private double a;
    private double b;
    private double c;
    // Constructor
    public POOEcuacionesCuadraticas(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public double getDiscriminante() {
        return b * b - 4 * a * c;
    }
    public double getRaiz1() {
        double discriminante = getDiscriminante();
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }
    public double getRaiz2() {
        double discriminante = getDiscriminante();
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }
    public static void main(String[] args) {
        double a = 1.0;
        double b = 3;
        double c = 1;
        POOEcuacionesCuadraticas ecuacion = new POOEcuacionesCuadraticas(a, b, c);
        // Calcular el discriminante
        double discriminante = ecuacion.getDiscriminante();
        // Mostrar resultados según el discriminante
        if (discriminante > 0) {
            double r1 = ecuacion.getRaiz1();
            double r2 = ecuacion.getRaiz2();
            System.out.println("La ecuación tiene dos raíces: " + r1 + " y " + r2);
        } else if (discriminante == 0) {
            double r1 = ecuacion.getRaiz1();
            System.out.println("La ecuación tiene una raíz: " + r1);
        } else {
            System.out.println("La ecuación no tiene raíces reales");
        }
    }
}