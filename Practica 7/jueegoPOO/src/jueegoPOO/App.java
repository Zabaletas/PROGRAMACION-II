package jueegoPOO;
public class App {
    public static void main(String[] args) {
        JuegoAdivinaNumero juegoNormal = new JuegoAdivinaNumero(3);
        JuegoAdivinaPar juegoPar = new JuegoAdivinaPar(3);
        JuegoAdivinaImpar juegoImpar = new JuegoAdivinaImpar(3);

        System.out.println("----- JUEGO NORMAL -----");
        juegoNormal.juega();

        System.out.println("\n----- JUEGO PAR -----");
        juegoPar.juega();

        System.out.println("\n----- JUEGO IMPAR -----");
        juegoImpar.juega();
    }
}