package utils;

import models.Particle;

import java.util.List;

public class ParticleGenerator {

    public static void initParticles(List<Particle> particleList) {
        particleList.add(new Particle(10,10));
        particleList.add(new Particle(15,15));
        particleList.add(new Particle(8,8));
    }
}
