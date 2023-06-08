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
    private boolean outside = false;

    private List<Particle> collisions = new ArrayList<>();
    private List<Tuple> collisionsWall = new ArrayList<>();

    public Particle(double x, double y) {
        this.id = global_id++;
        this.angle = Math.PI;
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

    public List<Tuple> getCollisionsWall() {
        return collisionsWall;
    }

    public void setCollisionsWall(List<Tuple> collisionsWall) {
        this.collisionsWall = collisionsWall;
    }

    public boolean isColliding(Particle other) {
        return this.getPosition().subtract(other.getPosition()).norm() <= this.getR() + other.getR();
    }

    public void addWallCollisions() {
        collisionsWall = new ArrayList<>();
        if(getPosition().getLeft() + getR() > 20)
            collisionsWall.add(new Tuple(20, getPosition().getRight()));
        else if(getPosition().getLeft() - getR() < 0)
            collisionsWall.add(new Tuple(0, getPosition().getRight()));
        else if(getPosition().getRight() + getR() > 20)
            collisionsWall.add(new Tuple(getPosition().getLeft(), 20));
        else if(!isOutside() && getPosition().getRight() - getR() < 0 && (getPosition().getLeft() > CPM.getTarget().getRight() || getPosition().getLeft() < CPM.getTarget().getLeft()))
            collisionsWall.add(new Tuple(getPosition().getLeft(), 0));
    }

    public boolean isOutside() {
        return outside;
    }

    public void setOutside(boolean outside) {
        this.outside = outside;
    }
}
