package assignment01;

import java.util.*;

public class LEET_743_joonparkhere {

    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> graph = new HashMap<>();

        for (int[] edge : times) {
            if (!graph.containsKey(edge[0]))
                graph.put(edge[0], new ArrayList<>());

            graph.get(edge[0]).add(new int[]{edge[1], edge[2]});
        }

        Map<Integer, Integer> delayMap = new HashMap<>();
        PriorityQueue<int[]> heap = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]); // sorted ascending distance
        heap.offer(new int[]{0, k});    // {distance, node}

        while (!heap.isEmpty()) {
            int[] info = heap.poll();
            int delay = info[0], cur = info[1];

            if (delayMap.containsKey(cur)) continue;
            delayMap.put(cur, delay);

            if (!graph.containsKey(cur)) continue;

            for (int[] edge : graph.get(cur)) {
                int next = edge[0], weight = edge[1];

                if (!delayMap.containsKey(next))
                    heap.offer(new int[]{delay + weight, next});
            }
        }

        int result = -1;
        if (delayMap.size() == n)
            for (int delay : delayMap.values())
                result = Math.max(result, delay);

        return result;
    }

}
