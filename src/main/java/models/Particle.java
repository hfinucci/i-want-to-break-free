package models;

import utils.Tuple;

public class Particle {

    private Tuple position;
    private Tuple velocity;
    private double v;
    private double r;
    private Tuple target;
    private double angle;

    public Tuple getPosition() {
        return position;
    }

    public void setPosition(Tuple position) {
        this.position = position;
    }

    public Tuple getVelocity() {
        return velocity;
    }

    public void setVelocity(Tuple velocity) {
        this.velocity = velocity;
    }

    public double getR() {
        return r;
    }

    public void setR(double r) {
        this.r = r;
    }

    public double getV() {
        return v;
    }

    public void setV(double v) {
        this.v = v;
    }

    public Tuple getTarget() {
        return target;
    }

    public void setTarget(Tuple target) {
        this.target = target;
    }

    public double getAngle() {
        return angle;
    }

    public void setAngle(double angle) {
        this.angle = angle;
    }
}
