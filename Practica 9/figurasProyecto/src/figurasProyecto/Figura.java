package figurasProyecto;
public abstract class Figura {
    protected String color;
    
    public Figura(String color) {
        this.color = color;
    }
    
    public String getColor() {
        return color;
    }
    
    public String toString() {
        return "Color: " + color;
    }
    
    public abstract double calcularArea();
    public abstract double calcularPerimetro();
}