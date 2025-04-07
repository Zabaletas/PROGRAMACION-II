package jueegoPOO;
import java.util.Scanner;

public class JuegoAdivinaImpar extends JuegoAdivinaNumero {
    public JuegoAdivinaImpar(int vidasIniciales) {
        super(vidasIniciales);
    }

    @Override
    public boolean validaNumero(int numero) {
        if (!super.validaNumero(numero)) {
            return false;
        }
        if (numero % 2 == 0) {
            System.out.println("Error: Debes ingresar un número impar");
            return false;
        }
        return true;
    }

    @Override
    public void juega() {
        reiniciaPartida();
        numeroAdivinar = (int)(Math.random() * 5) * 2 + 1; // Números impares 1-9
        
        System.out.println("Adivina un número IMPAR entre 0 y 10:");
        super.juega();
    }
}