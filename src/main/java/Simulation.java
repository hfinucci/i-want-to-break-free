import models.Particle;
import utils.CPM;
import utils.ParticleGenerator;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Simulation {

    public static void main(String[] args) {
        List<Particle> particlesList = new ArrayList<>();
        ParticleGenerator.initParticles(particlesList);

        try {
            FileWriter myWriter = new FileWriter("src/main/resources/states.txt");
            PrintWriter printWriter = new PrintWriter(myWriter);

            double time = 0;

            while (time < 1000) {
                printWriter.println(printParticle(particlesList, time));
                for (Particle firstParticle : particlesList) {
                    List<Particle> collisions = new ArrayList<>();
                    for (Particle secondParticle : particlesList) {
                        if (firstParticle.equals(secondParticle)) continue;
                        if (firstParticle.isColliding(secondParticle)) {
                            collisions.add(secondParticle);
                        }
                    }
                    firstParticle.addWallCollisions();
                    firstParticle.setCollisions(collisions);
                }
                for (Particle particle : particlesList) {
                    if (particle.getCollisions().isEmpty()) {
                        CPM.updateR(particle);
                    } else {
                        CPM.resetR(particle);
                    }
                }
                for (Particle particle : particlesList) {
                    CPM.calculateVelocity(particle);
                    CPM.calculatePosition(particle);
                    CPM.calculateAngle(particle);
                }
                time = CPM.updateTime(time);
            }

            printWriter.close();
            myWriter.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static String printParticle(List<Particle> particles, double time) {
        StringBuilder sb = new StringBuilder();
//        sb.append(particles.stream().filter(b -> !b.isDisabled()).count()).append("\n");
        sb.append(particles.size()).append("\n");
        sb.append(time).append("\n");
//        sb.append(gen).append("\n");
        for (Particle particle : particles) {
//            if (ball.isDisabled())
//                continue;
            String sb_line = particle.getId() + "\t" +
                    particle.getPosition().getLeft() + "\t" +
                    particle.getPosition().getRight() + "\t" +
                    particle.getVelocity().getLeft() + "\t" +
                    particle.getVelocity().getLeft() + "\t" +
                    particle.getR() + "\t" +
                    particle.getAngle() + "\t";
            sb.append(sb_line).append("\n");
        }
        sb.append("\n");

        return sb.toString();
    }
}
