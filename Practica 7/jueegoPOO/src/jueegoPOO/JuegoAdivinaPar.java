package jueegoPOO;
import java.util.Scanner;

public class JuegoAdivinaPar extends JuegoAdivinaNumero {
    public JuegoAdivinaPar(int vidasIniciales) {
        super(vidasIniciales);
    }
    @Override
    public boolean validaNumero(int numero) {
        if (!super.validaNumero(numero)) {
            return false;
        }
        if (numero % 2 != 0) {
            System.out.println("Error: Debes ingresar un número par");
            return false;
        }
        return true;
    }
    @Override
    public void juega() {
        reiniciaPartida();
        numeroAdivinar = (int)(Math.random() * 6) * 2; // Números pares 0-10
        
        System.out.println("Adivina un número PAR entre 0 y 10:");
        super.juega();
    }
}
