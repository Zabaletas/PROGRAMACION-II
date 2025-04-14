class A {
    public int x;
    public int z;

    public A(int x, int z) {
        this.x = x;
        this.z = z;
    }

    public void incrementaXZ() {
        this.x = this.x + 1;
        this.z = this.z + 1;
    }

    public void incrementaZ() {
        this.z = this.z + 1;
    }
}

class B {
    public int y;
    public int z;

    public B(int y, int z) {
        this.y = y;
        this.z = z;
    }

    public void incrementaYZ() {
        this.y = this.y + 1;
        this.z = this.z + 1;
    }

    public void incrementaZ() {
        this.z = this.z + 1;
    }
}

class D extends A {
    B b;

    public D(int x, int y, int z) {
        super(x, z);
        this.b = new B(y, z);
    }

    public void incrementaXYZ() {
        this.x = this.x + 1;
        this.b.y = this.b.y + 1;
        this.z = this.z + 1;
        this.b.z = this.b.z + 1;
    }

    public void incrementaYZ() {
        this.b.incrementaYZ();
    }

    // Java no permite herencia múltiple, así que debemos manejar B manualmente
    public void incrementaZB() {
        this.b.incrementaZ();
    }

    @Override
    public String toString() {
        return "(x=" + this.x + ", y=" + this.b.y + ", z=" + this.z + ")";
    }
}

public class HerenciaMult {
    public static void main(String[] args) {
        D d = new D(5, 10, 15);
        System.out.println("original: " + d);
        System.out.println("\nUsando los métodos de A:");
        d.incrementaXZ();
        System.out.println("Después de incrementaXZ: " + d);
        d.incrementaZ();
        System.out.println("Después de incrementaZ: " + d);
        System.out.println("\nUsando los métodos de B:");
        d.incrementaYZ();
        System.out.println("Después de incrementaYZ: " + d);
        d.incrementaZB(); // Nota: En Java necesitamos un método diferente para B
        System.out.println("Después de incrementaZ (de B): " + d);
        System.out.println("\nUsando el método de D:");
        d.incrementaXYZ();
        System.out.println("Después de incrementaXYZ: " + d);
    }
}