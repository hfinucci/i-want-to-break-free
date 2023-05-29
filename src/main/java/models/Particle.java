package models;

import utils.CPM;
import utils.Tuple;

import java.util.ArrayList;
import java.util.List;

public class Particle {

    private static int global_id = 0;
    private int id;
    private Tuple position;
    private Tuple velocity = new Tuple(0,0);
    private double v = 0;
    private double r;
    private Tuple target;
    private double angle;

    private List<Particle> collisions =new ArrayList<>();

    public Particle(double x, double y) {
        this.id = global_id++;
        this.position = new Tuple(x, y);
        CPM.calculateTarget(this);
        CPM.resetR(this);
    }

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

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Particle> getCollisions() {
        return collisions;
    }

    public void setCollisions(List<Particle> collisions) {
        this.collisions = collisions;
    }

    public boolean isColliding(Particle other) {
        return this.getPosition().subtract(other.getPosition()).norm() <= this.getR() + other.getR();
    }
}
