package assignment02;

import java.util.*;

public class LEET_743_joonparkhere {

    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] edge : times) {
            if (!graph.containsKey(edge[0])) {
                graph.put(edge[0], new ArrayList<>());
            }

            graph.get(edge[0]).add(new int[]{edge[1], edge[2]});
        }

        PriorityQueue<int[]> heap = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]);
        heap.offer(new int[]{0, k});

        Map<Integer, Integer> distanceMap = new HashMap<>();

        while (!heap.isEmpty()) {
            int[] info = heap.poll();
            int distance = info[0];
            int cur = info[1];

            if (distanceMap.containsKey(cur)) {
                continue;
            }
            distanceMap.put(cur, distance);

            if (!graph.containsKey(cur)) {
                continue;
            }

            for (int[] edge : graph.get(cur)) {
                int next = edge[0];
                int weight = edge[1];

                if (!distanceMap.containsKey(next)) {
                    heap.offer(new int[]{distance + weight, next});
                }
            }
        }

        if (distanceMap.size() != n) {
            return -1;
        }

        int result = 0;
        for (int distance : distanceMap.values()) {
            result = Math.max(result, distance);
        }
        return result;
    }

}
