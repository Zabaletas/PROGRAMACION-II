class AlgebraVectorial {
    private double x;
    private double y;
    private double z;
    // Constructores
    public AlgebraVectorial() {
        this(0, 0, 0);
    }
    public AlgebraVectorial(double x, double y) {
        this(x, y, 0);
    }
    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    private double productoPunto(AlgebraVectorial otro) {
        return this.x * otro.x + this.y * otro.y + this.z * otro.z;
    }
    private AlgebraVectorial productoCruz(AlgebraVectorial otro) {
        return new AlgebraVectorial(
            this.y * otro.z - this.z * otro.y,
            this.z * otro.x - this.x * otro.z,
            this.x * otro.y - this.y * otro.x
        );
    }
    private double magnitud() {
        return Math.sqrt(x*x + y*y + z*z);
    }
    // 1. Determinar si dos vectores son perpendiculares (versión a·b = 0)
    public boolean sonPerpendiculares(AlgebraVectorial otro) {
        return Math.abs(this.productoPunto(otro)) < 1e-10;
    }
    // 2. Determinar si dos vectores son paralelos (versión a×b = 0)
    public boolean sonParalelos(AlgebraVectorial otro) {
        return this.productoCruz(otro).magnitud() < 1e-10;
    }
    // 3. Determinar la proyección de a sobre b
    public AlgebraVectorial proyeccionSobre(AlgebraVectorial otro) {
        double factor = this.productoPunto(otro) / Math.pow(otro.magnitud(), 2);
        return new AlgebraVectorial(
            otro.x * factor,
            otro.y * factor,
            otro.z * factor
        );
    }
    // 4. Determinar el componente de a en b
    public double componenteEn(AlgebraVectorial otro) {
        return this.productoPunto(otro) / otro.magnitud();
    }
    @Override
    public String toString() {
        return String.format("(%.2f, %.2f, %.2f)", x, y, z);
    }
    public static void main(String[] args) {
        // Vectores de prueba
        AlgebraVectorial a = new AlgebraVectorial(1, 2, 3);
        AlgebraVectorial b = new AlgebraVectorial(-2, 1, 0);
        AlgebraVectorial c = new AlgebraVectorial(0, 0, 0);
        AlgebraVectorial d = new AlgebraVectorial(-3,-6, 5);
        // Pruebas
        System.out.println("¿a y b son perpendiculares? " + a.sonPerpendiculares(b));
        System.out.println("¿a y c son paralelos? " + a.sonParalelos(c));
        AlgebraVectorial proyeccion = d.proyeccionSobre(a);
        System.out.println("Proyección de d sobre a: " + proyeccion);
        double componente = d.componenteEn(a);
        System.out.println("Componente de d en a: " + componente);
    }
}