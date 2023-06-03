package utils;

import models.Particle;
import org.apache.commons.math3.distribution.UniformRealDistribution;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ParticleGenerator {

    private static final int COUNT = 200;
    private static final int SIZE = 20;

    public static void initParticles(List<Particle> particleList) {
        Map<Tuple, Integer> positioned = new HashMap<>();
        UniformRealDistribution urd = new UniformRealDistribution(0 + CPM.getRMin(), SIZE - CPM.getRMin());
        while(positioned.size() < COUNT) {
            Tuple pos = new Tuple(urd.sample(), urd.sample());
            if(!positioned.containsKey(pos)) {
                positioned.put(pos, 1);
                particleList.add(new Particle(pos.getLeft(), pos.getRight()));
            }
        }
    }
}
