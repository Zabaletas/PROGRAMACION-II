package figurasProyecto;

public class Main {
    public static void main(String[] args) {
        Figura[] figuras = new Figura[5];

        for (int i = 0; i < figuras.length; i++) {
            int tipo = (Math.random() < 0.5) ? 1 : 2;
            String color = (Math.random() < 0.5) ? "Rojo" : "Azul";

            if (tipo == 1) {
                double lado = 1 + Math.random() * 10;
                figuras[i] = new Cuadrado(color, lado);
            } else {
                double radio = 1 + Math.random() * 10;
                figuras[i] = new Circulo(color, radio);
            }
        }

        for (Figura f : figuras) {
            System.out.println(f);
            System.out.printf("Área: %.2f | Perímetro: %.2f%n", 
                f.calcularArea(), f.calcularPerimetro());

            if (f instanceof Coloreado) {
                System.out.println("Coloración: " + ((Coloreado)f).comoColorear());
            }
            System.out.println("------------------------");
        }
    }
}