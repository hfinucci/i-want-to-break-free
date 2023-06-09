package utils;

import models.Particle;
import org.apache.commons.math3.distribution.UniformRealDistribution;

import java.util.List;
import java.util.stream.Collectors;

public class CPM {
    private static final double R_MIN = 0.1;
    private static final double R_MAX = 0.37;
    private static final double MAX_VD = 2.0;
    private static final double BETA = 0.9;
    private static final double TAU = 0.5;
    private static final double D = 3.0;
    public static final double DELTA_T = R_MIN / (2 * MAX_VD);
    private static final double DELTA_R = R_MAX / (TAU / DELTA_T);

    public static final Tuple TARGET = new Tuple(10.0 - (D - 0.2)/2, 10 + (D - 0.2)/2);
    public static final Tuple TARGET_OUTSIDE = new Tuple(8.5, 11.5);

    private static void newVd(Particle particle) {
        particle.setV(
                MAX_VD * Math.pow((particle.getR() - R_MIN) / (R_MAX - R_MIN), BETA)
        );
    }

    public static void calculateTarget(Particle particle) {
        if (particle.getPosition().getLeft() >= TARGET.getLeft() && particle.getPosition().getLeft() <= TARGET.getRight())
            particle.setTarget(new Tuple(particle.getPosition().getLeft(), 0));
        else {
            UniformRealDistribution urd = new UniformRealDistribution(TARGET.getLeft(), TARGET.getRight());
            particle.setTarget(new Tuple(urd.sample(), 0));
        }
        calculateAngle(particle);
    }

    public static void calculateTargetOutside(Particle particle) {
        if (particle.getPosition().getLeft() >= TARGET_OUTSIDE.getLeft() && particle.getPosition().getLeft() <= TARGET_OUTSIDE.getRight())
            particle.setTarget(new Tuple(particle.getPosition().getLeft(), -10));
        else {
            UniformRealDistribution urd = new UniformRealDistribution(TARGET_OUTSIDE.getLeft(), TARGET_OUTSIDE.getRight());
            particle.setTarget(new Tuple(urd.sample(), -10));
        }
        calculateAngle(particle);
    }

    public static void calculateVelocity(Particle particle) {
        if(particle.getCollisions().isEmpty() && particle.getCollisionsWall().isEmpty())
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
                particle.getPosition().getRight() - other.getPosition().getRight());
        calculateTarget(particle);
        return dif.divide(dif.norm());
    }

    private static Tuple eWithWall(Particle particle, Tuple wall) {
        Tuple dif = new Tuple(
                particle.getPosition().getLeft() - wall.getLeft(),
                particle.getPosition().getRight() - wall.getRight());
        return dif.divide(dif.norm());
    }

    private static void calculateVe(Particle particle) {
         Tuple sum = particle.getCollisions()
                 .stream()
                 .map(particle1 -> e(particle, particle1))
                 .reduce(new Tuple(0, 0), Tuple::add);
         Tuple wall = particle.getCollisionsWall()
                 .stream()
                 .map(tuple -> eWithWall(particle, tuple))
                 .reduce(new Tuple(0, 0), Tuple::add);
         sum = sum.add(wall);
         Tuple res = sum.divide(sum.norm()).multiply(MAX_VD);
         particle.setVelocity(res);
    }

    public static void calculatePosition(Particle particle) {
        particle.setPosition(
                particle.getPosition().add(particle.getVelocity().multiply(DELTA_T))
        );
        if (!particle.isOutside() && particle.getPosition().getRight() < 0) {
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
            else
                particle.setAngle(Math.PI);
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
            } else
                particle.setAngle(Math.PI);
        }
    }

    public static List<Particle> deleteParticles(List<Particle> particles) {
        return particles.stream().filter(particle -> particle.getPosition().getRight() + getRMin() > -10).collect(Collectors.toList());
    }

    public static void resetR(Particle particle) {
        particle.setR(R_MIN);
    }

    public static double updateTime(double time) {
        return time + DELTA_T;
    }

    public static double getRMin() {
        return R_MIN;
    }

    public static double getD() {
        return D;
    }

    public static Tuple getTarget() {
        return TARGET;
    }
}
