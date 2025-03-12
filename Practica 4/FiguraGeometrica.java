class FiguraGeometrica {
    
    double area(double radio) {
        return Math.PI*radio*radio; //Círculo
    }
    double area(double base, double altura) {
        return base*altura; //Rectángulo
    }
    double area(double base, double altura, double hipotenusa) {
        return (base*altura)/2; //Triángulo rect
    }
    double area(double baseMenor, double baseMayor, double altura, double inclinacion) {
        return ((baseMenor+baseMayor)*altura)/2; //Trapecio
    }
    double area(double lado, double apotema, double radio, double perimetro, double tipo) {
        return (5*lado*apotema)/2; //Pentágono
    }
    public static void main(String[] args) {
        FiguraGeometrica f1=new FiguraGeometrica();
        FiguraGeometrica f2=new FiguraGeometrica();
        FiguraGeometrica f3=new FiguraGeometrica();
        FiguraGeometrica f4=new FiguraGeometrica();
        FiguraGeometrica f5=new FiguraGeometrica();
        System.out.println("Círculo:"+f1.area(1));
        System.out.println("Rectángulo:"+f2.area(2, 3));
        System.out.println("Triángulo Rectángulo:"+f3.area(3, 5, 7));
        System.out.println("Trapecio:"+f4.area(2, 5, 7, 9));
        System.out.println("Pentágono:"+f5.area(2, 3, 6, 7, 9));
    }
}
