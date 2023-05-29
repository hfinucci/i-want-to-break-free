package utils;

public class Tuple {
    double left;
    double right;

    public Tuple(double left, double right) {
        this.left = left;
        this.right = right;
    }

    public double getLeft() {
        return left;
    }

    public void setLeft(double left) {
        this.left = left;
    }

    public double getRight() {
        return right;
    }

    public void setRight(double right) {
        this.right = right;
    }

    public double dot(Tuple t){
        return left * t.getLeft() + right * t.getRight();
    }

    public Tuple multiply(double d){
        return new Tuple(left * d, right * d);
    }

    public Tuple add(Tuple t){
        return new Tuple(left + t.getLeft(), right + t.getRight());
    }

    public Tuple subtract(Tuple t){
        return new Tuple(left - t.getLeft(), right - t.getRight());
    }
    public Tuple subtract(double d){
        return new Tuple(left - d, right - d);
    }

    public Tuple divide(double d){
        return new Tuple(left / d, right / d);
    }

    public double norm() {
        return Math.sqrt(left * left + right * right);
    }

    public Tuple versor(Tuple t) {
        return this.subtract(t).divide(this.subtract(t).norm());
    }

}
