package utils;

import models.Particle;

import java.util.List;

public class CPM {
    private static final double R_MIN = 0.1;
    private static final double R_MAX = 0.37;
    private static final double MAX_VD = 0.95;
    private static final double BETA = 0.9;
    private static final double TAU = 0.5;
    public static final double DELTA_T = R_MIN / (2 * MAX_VD);
    private static final double DELTA_R = R_MAX / (TAU / DELTA_T);

    public static final Tuple TARGET = new Tuple(9.5, 10.5);

    public static void newVd(Particle particle) {
        particle.setV(
                MAX_VD * Math.pow((particle.getR() - R_MIN) / (R_MAX - R_MIN), BETA)
        );
    }

    public static void calculateTarget(Particle particle) {
        if(particle.getPosition().getLeft() >= TARGET.getLeft() && particle.getPosition().getLeft() <= TARGET.getRight())
            particle.setTarget(new Tuple(particle.getPosition().getLeft(), 0));
        else if(particle.getPosition().getLeft() < TARGET.getLeft())
            particle.setTarget(new Tuple(TARGET.getLeft(), 0));
        else
            particle.setTarget(new Tuple(TARGET.getRight(), 0));
        particle.setAngle(
                1 / Math.tan(Math.abs(particle.getPosition().getLeft() - particle.getTarget().getLeft()) / particle.getPosition().getRight())
        );
    }

    public static void calculateVelocity(Particle particle, List<Particle> collisions) {
        if(collisions.isEmpty())
            calculateVd(particle);
        else
            calculateVe(particle, collisions);
    }

    private static void calculateVd(Particle particle) {
        particle.setVelocity(new Tuple(
                particle.getV() * Math.sin(particle.getAngle()),
                particle.getV() * Math.cos(particle.getAngle())
        ));
    }

    private static Tuple e(Particle particle, Particle other) {
        Tuple dif = new Tuple(
                particle.getPosition().getLeft() - other.getPosition().getLeft(),
                particle.getPosition().getLeft() - other.getPosition().getRight());
        return dif.divide(dif.norm());
    }

    private static void calculateVe(Particle particle, List<Particle> collisions) {
         Tuple sum = collisions
                 .stream()
                 .map(particle1 -> e(particle, particle1))
                 .reduce(new Tuple(0, 0), Tuple::add);
         Tuple res = sum.divide(sum.norm()).multiply(MAX_VD);
         particle.setVelocity(res);
    }

    public static void calculatePosition(Particle particle) {
        particle.setPosition(particle.getPosition().add(particle.getVelocity().multiply(DELTA_T)));
    }

    public static void updateR(Particle particle) {
        particle.setR(particle.getR() + DELTA_R);
    }

    public static void resetR(Particle particle) {
        particle.setR(R_MIN);
    }


}
