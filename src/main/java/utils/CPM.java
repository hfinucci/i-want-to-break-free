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
    public static final Tuple TARGET_OUTSIDE = new Tuple(8.5, 11.5);

    private static void newVd(Particle particle) {
        particle.setV(
                MAX_VD * Math.pow((particle.getR() - R_MIN) / (R_MAX - R_MIN), BETA)
        );
    }

    public static void calculateTarget(Particle particle) {
        if (particle.getPosition().getLeft() >= TARGET.getLeft() && particle.getPosition().getLeft() <= TARGET.getRight())
            particle.setTarget(new Tuple(particle.getPosition().getLeft(), 0));
        else if (particle.getPosition().getLeft() < TARGET.getLeft())
            particle.setTarget(new Tuple(TARGET.getLeft(), 0));
        else
            particle.setTarget(new Tuple(TARGET.getRight(), 0));
        calculateAngle(particle);
    }

    public static void calculateTargetOutside(Particle particle) {
        if (particle.getPosition().getLeft() >= TARGET_OUTSIDE.getLeft() && particle.getPosition().getLeft() <= TARGET_OUTSIDE.getRight())
            particle.setTarget(new Tuple(particle.getPosition().getLeft(), -10));
        else if (particle.getPosition().getLeft() < TARGET_OUTSIDE.getLeft())
            particle.setTarget(new Tuple(TARGET_OUTSIDE.getLeft(), -10));
        else
            particle.setTarget(new Tuple(TARGET_OUTSIDE.getRight(), -10));
    }

    public static void calculateVelocity(Particle particle) {
        if(particle.getCollisions().isEmpty())
            calculateVd(particle);
        else
            calculateVe(particle);
    }

    private static void calculateVd(Particle particle) {
        newVd(particle);
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

    private static void calculateVe(Particle particle) {
         Tuple sum = particle.getCollisions()
                 .stream()
                 .map(particle1 -> e(particle, particle1))
                 .reduce(new Tuple(0, 0), Tuple::add);
         Tuple res = sum.divide(sum.norm()).multiply(MAX_VD);
         particle.setVelocity(res);
    }

    public static void calculatePosition(Particle particle) {
        particle.setPosition(
                particle.getPosition().add(particle.getVelocity().multiply(DELTA_T))
        );
        if (particle.getPosition().getRight() < 0) {
            particle.setOutside(true);
            calculateTargetOutside(particle);
        }
    }

    public static void updateR(Particle particle) {
        if (particle.getR() < R_MAX) {
            particle.setR(particle.getR() + DELTA_R);
        }
    }

    public static void calculateAngle(Particle particle) {
        if (particle.isOutside()) {
            if (particle.getPosition().getLeft() != particle.getTarget().getLeft()) {
                particle.setAngle(
                        Math.atan(Math.abs(particle.getPosition().getLeft() - particle.getTarget().getLeft()) / 10)
                );
                if (particle.getPosition().getLeft() < TARGET_OUTSIDE.getLeft()) {
                    particle.setAngle(Math.PI - particle.getAngle());
                }
                else if (particle.getPosition().getLeft() > TARGET_OUTSIDE.getRight()) {
                    particle.setAngle(Math.PI + particle.getAngle());
                }
            }
        } else {
            if (particle.getPosition().getLeft() != particle.getTarget().getLeft()) {
                particle.setAngle(
                        Math.atan(Math.abs(particle.getPosition().getLeft() - particle.getTarget().getLeft()) / particle.getPosition().getRight())
                );
                if (particle.getPosition().getLeft() < TARGET.getLeft()) {
                    particle.setAngle(Math.PI - particle.getAngle());
                }
                else if (particle.getPosition().getLeft() > TARGET.getRight()) {
                    particle.setAngle(Math.PI + particle.getAngle());
                }
            }
        }
    }

    public static void resetR(Particle particle) {
        particle.setR(R_MIN);
    }

    public static double updateTime(double time) {
        return time + DELTA_T;
    }


}
