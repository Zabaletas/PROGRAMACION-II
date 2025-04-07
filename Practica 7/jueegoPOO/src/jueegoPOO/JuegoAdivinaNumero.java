package jueegoPOO;
import java.util.Scanner;

public class JuegoAdivinaNumero extends Juego {
    protected int numeroAdivinar;
    protected Scanner scanner;

    public JuegoAdivinaNumero(int vidasIniciales) {
        super(vidasIniciales);
        scanner = new Scanner(System.in);
    }

    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }

    public void juega() {
        reiniciaPartida();
        numeroAdivinar = (int)(Math.random() * 11); // Número entre 0-10
        
        System.out.println("Adivina un número entre 0 y 10:");

        boolean adivinado = false;
        while (!adivinado && numeroDeVidas > 0) {
            int numeroUsuario = scanner.nextInt();
            
            if (!validaNumero(numeroUsuario)) {
                System.out.println("Número no válido. Debe estar entre 0 y 10. Intenta de nuevo:");
                continue;
            }

            if (numeroUsuario == numeroAdivinar) {
                System.out.println("¡Acertaste!");
                actualizaRecord();
                adivinado = true;
            } else {
                System.out.println(numeroUsuario < numeroAdivinar ? "El número es mayor" : "El número es menor");
                if (!quitaVida()) {
                    break;
                }
                System.out.println("Intenta de nuevo:");
            }
        }
    }
}