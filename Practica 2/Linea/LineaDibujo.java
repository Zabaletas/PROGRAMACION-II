import javax.swing.*;
import java.awt.*;

class Punto {
    public int x, y;

    public Punto(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Linea extends JPanel {
    private Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
        setPreferredSize(new Dimension(600, 600)); 
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.PINK);
        g.drawLine(p1.x*70, p1.y*70, p2.x*70, p2.y*70);
    }

    public void dibujarLinea() {
        JFrame frame = new JFrame("Dibujar Linea");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        frame.add(this);
        frame.pack();
        frame.setLocationRelativeTo(null); 
        frame.setVisible(true);
    }
}
    
    public class LineaDibujo {
        public static void main(String[] args) {
            SwingUtilities.invokeLater(() -> {
                Punto p1 = new Punto(3, 3);
                Punto p2 = new Punto(6, 6);
                Linea linea = new Linea(p1, p2);
                linea.dibujarLinea();
            });
        }
    }