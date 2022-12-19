package assignment01;

import java.io.*;
import java.util.*;

public class BOJ_4386_joonparkhere {

    private static class Point {
        private final double x;
        private final double y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    private static class Edge implements Comparable<Edge> {
        private final int vertexA;
        private final int vertexB;
        private final double weight;

        public Edge(int vertexA, int vertexB, double weight) {
            this.vertexA = vertexA;
            this.vertexB = vertexB;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge o) {
            return Double.compare(this.weight, o.weight);
        }
    }

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final List<Edge> edgeList = new ArrayList<>();
    private static int[] set;
    private static int numOfVertex = 0;

    public static void main(String[] args) throws IOException {
        initEdgeList();
        findMST();
    }

    private static void initEdgeList() throws IOException {
        numOfVertex = Integer.parseInt(br.readLine());
        List<Point> pointList = new ArrayList<>();

        for (int i = 0; i < numOfVertex; i++) {
            String[] input = br.readLine().split(" ");
            Point point = new Point(Double.parseDouble(input[0]), Double.parseDouble(input[1]));
            pointList.add(point);
        }

        for (int i = 0; i < numOfVertex; i++) {
            Point pointA = pointList.get(i);
            for (int j = i + 1; j < numOfVertex; j++) {
                Point pointB = pointList.get(j);
                double distance = Math.hypot(pointA.x - pointB.x, pointA.y - pointB.y);
                Edge edge = new Edge(i, j, distance);
                edgeList.add(edge);
            }
        }

        Collections.sort(edgeList);
    }

    private static void findMST() throws IOException {
        double sum = 0;

        set = new int[numOfVertex];
        for (int i = 0; i < numOfVertex; i++) {
            set[i] = i;
        }

        for (Edge edge : edgeList) {
            int setA = find(edge.vertexA);
            int setB = find(edge.vertexB);
            if (setA != setB) {
                sum += edge.weight;
                union(edge.vertexA, edge.vertexB);
            }
        }

        bw.append(String.format("%.2f", sum));
        bw.flush();
        bw.close();
    }

    private static int find(int vertex) {
        if (set[vertex] == vertex)
            return vertex;
        set[vertex] = find(set[vertex]);
        return set[vertex];
    }

    private static void union(int vertexA, int vertexB) {
        int setA = set[vertexA];
        int setB = set[vertexB];
        if (setA != setB) {
            set[setB] = setA;
        }
    }

}
