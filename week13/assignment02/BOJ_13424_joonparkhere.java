package assignment02;

import java.io.*;
import java.util.*;

public class BOJ_13424_joonparkhere {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static List<List<int[]>> edgeList;
    static List<Integer> positionList;

    public static void main(String[] args) throws IOException {
        int numOfTest = Integer.parseInt(br.readLine());
        for (int i = 0; i < numOfTest; i++) {
            init();
            solution();
        }
        bw.flush();
        bw.close();
    }

    static void init() throws IOException {
        edgeList = new ArrayList<>();
        positionList = new ArrayList<>();

        String[] spaceInfo = br.readLine().split(" ");
        int numOfRoom = Integer.parseInt(spaceInfo[0]);
        int numOfPath = Integer.parseInt(spaceInfo[1]);

        for (int i = 0; i <= numOfRoom; i++)
            edgeList.add(new ArrayList<>());

        for (int i = 0; i < numOfPath; i++) {
            String[] pathInfo = br.readLine().split(" ");
            int roomA = Integer.parseInt(pathInfo[0]);
            int roomB = Integer.parseInt(pathInfo[1]);
            int weight = Integer.parseInt(pathInfo[2]);

            edgeList.get(roomA).add(new int[]{roomB, weight});  // room, weight
            edgeList.get(roomB).add(new int[]{roomA, weight});
        }

        int numOfMember = Integer.parseInt(br.readLine());
        String[] positionInfo = br.readLine().split(" ");
        for (int i = 0; i < numOfMember; i++)
            positionList.add(Integer.parseInt(positionInfo[i]));
    }

    private static void solution() throws IOException {
        int targetRoom = 0;
        int targetCost = Integer.MAX_VALUE;
        for (int room = 1; room < edgeList.size(); room++) {
            int cost = dijkstra(room);
            if (cost < targetCost) {
                targetRoom = room;
                targetCost = cost;
            }
        }

        bw.append(String.valueOf(targetRoom));
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
        heap.offer(new int[]{start, 0});    // node, cost

        while (!heap.isEmpty()) {
            int[] info = heap.poll();
            int cur = info[0];
            int cost = info[1];

            if (distanceMap.containsKey(cur))
                continue;
            distanceMap.put(cur, cost);

            for (int[] edgeInfo : edgeList.get(cur)) {
                int next = edgeInfo[0];
                int weight = edgeInfo[1];

                if (!distanceMap.containsKey(next))
                    heap.offer(new int[]{next, cost + weight});
            }
        }

        int totalCost = 0;
        for (int position : positionList)
            totalCost += distanceMap.get(position);

        return totalCost;
    }

}
