public class Vector3D {
    private double x;
    private double y;
    private double z;
    // Constructores
    public Vector3D() {
        this(0, 0, 0);
    }
    public Vector3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    public Vector3D sumar(Vector3D otro) {
        return new Vector3D(
            this.x + otro.x,
            this.y + otro.y,
            this.z + otro.z
        );
    }
    public Vector3D multiplicar(double escalar) {
        return new Vector3D(
            this.x * escalar,
            this.y * escalar,
            this.z * escalar
        );
    }
    public double longitud() {
        return Math.sqrt(x*x + y*y + z*z);
    }
    //  Vector normalizado
    public Vector3D normalizar() {
        double magnitud = this.longitud();
        if (magnitud == 0) return new Vector3D();
        return new Vector3D(
            x/magnitud,
            y/magnitud,
            z/magnitud
        );
    }
    //  Producto escalar
    public double productoPunto(Vector3D otro) {
        return x*otro.x + y*otro.y + z*otro.z;
    }
    //  Producto vectorial
    public Vector3D productoCruz(Vector3D otro) {
        return new Vector3D(
            y*otro.z - z*otro.y,
            z*otro.x - x*otro.z,
            x*otro.y - y*otro.x
        );
    }
    public boolean esPerpendicular(Vector3D otro) {
        return Math.abs(this.productoPunto(otro)) < 1e-10;
    }
    public Vector3D proyeccion(Vector3D otro) {
        double factor = this.productoPunto(otro) / Math.pow(otro.longitud(), 2);
        return otro.multiplicar(factor);
    }
    public double componente(Vector3D otro) {
        return this.productoPunto(otro) / otro.longitud();
    }
    @Override
    public String toString() {
        return String.format("(%.2f, %.2f, %.2f)", x, y, z);
    }
    public static void main(String[] args) {
        Vector3D a = new Vector3D(2, 5, 0);
        Vector3D b = new Vector3D(0, 1, 0);
        Vector3D c = new Vector3D(1, 1, 0);
        // Pruebas de operaciones básicas
        System.out.println("Suma a + b: " + a.sumar(b));
        System.out.println("Producto por escalar (2*a): " + a.multiplicar(2));
        System.out.println("Longitud de c: " + c.longitud());
        System.out.println("Vector normalizado de c: " + c.normalizar());
        System.out.println("Producto punto a·b: " + a.productoPunto(b));
        System.out.println("Producto cruz a×b: " + a.productoCruz(b));
        // Pruebas de funcionalidades adicionales
        System.out.println("¿a y b son perpendiculares? " + a.esPerpendicular(b));
        System.out.println("Proyección de c sobre a: " + c.proyeccion(a));
        System.out.println("Componente de c en a: " + c.componente(a));
    }
}