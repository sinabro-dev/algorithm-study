package assignment02;

import java.io.*;
import java.util.*;

public class BOJ_1967_joonparkhere {

    private static class Node {
        private final int idx;
        private final int weight;

        public Node(int idx, int weight) {
            this.idx = idx;
            this.weight = weight;
        }
    }

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final List<List<Node>> graph = new ArrayList<>();

    private static int[] distance;
    private static int numOfNode = 0;
    private static int endNodeIdx = 0;
    private static int diameter = 0;

    public static void main(String[] args) throws IOException {
        initTree();
        distance = new int[numOfNode + 1];

        Arrays.fill(distance, -1);
        distance[1] = 0;
        dfs(1);
        updateFarthestNode();

        Arrays.fill(distance, -1);
        distance[endNodeIdx] = 0;
        dfs(endNodeIdx);
        updateFarthestNode();

        bw.append(String.valueOf(diameter));
        bw.flush();
        bw.close();
    }

    private static void initTree() throws IOException {
        numOfNode = Integer.parseInt(br.readLine());
        for (int idx = 0; idx <= numOfNode; idx++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 1; i < numOfNode; i++) {
            String[] input = br.readLine().split(" ");
            int parent = Integer.parseInt(input[0]);
            int child = Integer.parseInt(input[1]);
            int weight = Integer.parseInt(input[2]);

            graph.get(parent).add(new Node(child, weight));
            graph.get(child).add(new Node(parent, weight));
        }
    }

    private static void dfs(int current) {
        for (Node next : graph.get(current)) {
            if (distance[next.idx] != -1) {
                continue;
            }
            distance[next.idx] = distance[current] + next.weight;
            dfs(next.idx);
        }
    }

    private static void updateFarthestNode() {
        for (int i = 1; i <= numOfNode; i++) {
            if (diameter < distance[i]) {
                diameter = distance[i];
                endNodeIdx = i;
            }
        }
    }

}
