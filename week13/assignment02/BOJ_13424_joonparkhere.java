package assignment02;

import java.io.*;
import java.util.*;

public class BOJ_13424_joonparkhere {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static final int MAX_COST = 5000000;

    static int[][] graph;
    static int[] positionList;

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
        String[] spaceInfo = br.readLine().split(" ");
        int numOfRoom = Integer.parseInt(spaceInfo[0]);
        int numOfPath = Integer.parseInt(spaceInfo[1]);

        graph = new int[numOfRoom + 1][numOfRoom + 1];
        for (int i = 1; i <= numOfRoom; i++) {
            Arrays.fill(graph[i], MAX_COST);
            graph[i][i] = 0;
        }

        for (int i = 0; i < numOfPath; i++) {
            String[] pathInfo = br.readLine().split(" ");
            int roomA = Integer.parseInt(pathInfo[0]);
            int roomB = Integer.parseInt(pathInfo[1]);
            int weight = Integer.parseInt(pathInfo[2]);

            graph[roomA][roomB] = weight;
            graph[roomB][roomA] = weight;
        }

        int numOfMember = Integer.parseInt(br.readLine());
        positionList = new int[numOfMember];

        String[] positionInfo = br.readLine().split(" ");
        for (int i = 0; i < numOfMember; i++)
            positionList[i] = Integer.parseInt(positionInfo[i]);
    }

    private static void solution() throws IOException {
        floyd();

        int targetRoom = 0;
        int targetCost = Integer.MAX_VALUE;

        for (int room = 1; room <= graph[0].length - 1; room++) {
            int cost = 0;
            for (int position : positionList)
                cost += graph[room][position];

            if (cost < targetCost) {
                targetRoom = room;
                targetCost = cost;
            }
        }

        bw.append(String.valueOf(targetRoom));
        bw.newLine();
    }

    private static void floyd() {
        int numOfRoom = graph[0].length - 1;
        for (int k = 1; k <= numOfRoom; k++) {
            for (int i = 1; i <= numOfRoom; i++) {
                for (int j = 1; j <= numOfRoom; j++) {
                    if (i == j)
                        continue;

                    graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }
    }

}
