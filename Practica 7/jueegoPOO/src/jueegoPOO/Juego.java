package jueegoPOO;
//Juego.java
public class Juego {
protected int numeroDeVidas;
protected int record;

public Juego(int vidasIniciales) {
   this.numeroDeVidas = vidasIniciales;
   this.record = 0;
}
public void reiniciaPartida() {
   this.numeroDeVidas = 3;
}
public void actualizaRecord() {
   if (numeroDeVidas > record) {
       record = numeroDeVidas;
       System.out.println("¡Nuevo récord! Ahora es: " + record);
   }
}
public boolean quitaVida() {
   numeroDeVidas--;
   if (numeroDeVidas <= 0) {
       System.out.println("¡Se acabaron las vidas!");
       return false;
   }
   System.out.println("Vidas restantes: " + numeroDeVidas);
   return true;
}
}