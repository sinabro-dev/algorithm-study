package assignment02;

import java.io.*;
import java.util.*;

public class BOJ_13424_joonparkhere {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static List<List<Path>> pathList = new ArrayList<>();
    static List<Integer> memberPositionList = new ArrayList<>();

    static class Path {
        int to;
        int cost;

        public Path(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        int numOfTest = Integer.parseInt(br.readLine());
        for (int i = 0; i < numOfTest; i++) {
            init();
            solution();
        }
    }

    static void init() throws IOException {
        String[] spaceInfo = br.readLine().split(" ");
        int numOfRoom = Integer.parseInt(spaceInfo[0]);
        int numOfPath = Integer.parseInt(spaceInfo[1]);

        for (int i = 0; i <= numOfRoom; i++) {
            pathList.add(new ArrayList<>());
        }

        for (int i = 0; i < numOfPath; i++) {
            String[] pathInfo = br.readLine().split(" ");
            int roomA = Integer.parseInt(pathInfo[0]);
            int roomB = Integer.parseInt(pathInfo[1]);
            int cost = Integer.parseInt(pathInfo[2]);

            pathList.get(roomA).add(new Path(roomB, cost));
            pathList.get(roomB).add(new Path(roomA, cost));
        }

        int numOfMember = Integer.parseInt(br.readLine());
        String[] memberInfo = br.readLine().split(" ");
        for (int i = 0; i < numOfMember; i++) {
            memberPositionList.add(Integer.parseInt(memberInfo[i]));
        }
    }

    private static void solution() throws IOException {
        int result = Integer.MAX_VALUE;
        for (int room = 1; room < pathList.size(); room++) {
            result = Math.min(result, dijkstra(room));
        }

        bw.append(String.valueOf(result));
        bw.newLine();
    }

    private static int dijkstra(int start) {
        Map<Integer, Integer> distanceMap = new HashMap<>();
        PriorityQueue<int[]> heap = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });
        heap.offer(new int[]{start, 0});    // node, distance

        while (!heap.isEmpty()) {
            int[] info = heap.poll();
            int cur = info[0];
            int distance = info[1];

            if (distanceMap.containsKey(cur))
                continue;
            distanceMap.put(cur, distance);

            for (Path path : pathList.get(cur)) {
                int next = path.to;
                int cost = path.cost;

                if (!distanceMap.containsKey(next))
                    heap.offer(new int[]{next, cost});
            }
        }

        int sum = 0;
        for (int target : memberPositionList) {
            sum += distanceMap.get(target);
        }

        return sum;
    }

}
