package figurasProyecto;
public class Cuadrado extends Figura implements Coloreado {
    private final double lado;

    public Cuadrado(String color, double lado) {
        super(color);
        this.lado = lado;
    }

    public double calcularArea() {
        return lado * lado;
    }

    public double calcularPerimetro() {
        return 4 * lado;
    }

    public String comoColorear() {
        return "Colorear los cuatro lados";
    }

    public String toString() {
        return String.format("Cuadrado [Color: %s, Lado: %.2f]", getColor(), lado);
    }
}