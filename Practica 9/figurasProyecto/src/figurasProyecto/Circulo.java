package figurasProyecto;
public class Circulo extends Figura {
    private final double radio;

    public Circulo(String color, double radio) {
        super(color);
        this.radio = radio;
    }

    public double calcularArea() {
        return Math.PI * radio * radio;
    }

    public double calcularPerimetro() {
        return 2 * Math.PI * radio;
    }

    public String toString() {
        return String.format("Círculo [Color: %s, Radio: %.2f]", getColor(), radio);
    }
}