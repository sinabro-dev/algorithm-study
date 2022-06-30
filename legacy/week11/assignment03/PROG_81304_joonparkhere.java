package assignment03;

import java.util.*;

public class PROG_81304_joonparkhere {

    int[][] distance;
    List<List<Node>> adjList;
    Map<Integer, Integer> trapMap;

    class Node implements Comparable<Node> {
        int index;
        int cost;
        int state;

        public Node(int index, int cost, int state) {
            this.index = index;
            this.cost = cost;
            this.state = state;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    public int solution(int n, int start, int end, int[][] roads, int[] traps) {
        setUp(n, roads, traps);
        return dijkstra(start, end);
    }

    void setUp(int n, int[][] roads, int[] traps) {
        adjList = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adjList.add(new ArrayList<>());
        for (int[] road : roads) {
            adjList.get(road[0]).add(new Node(road[1], road[2], 0));
            adjList.get(road[1]).add(new Node(road[0], road[2], 1));
        }

        trapMap = new HashMap<>();
        for (int i = 0; i < traps.length; i++)
            trapMap.put(traps[i], i);

        distance = new int[n + 1][1 << 10];
        for (int i = 1; i <= n; i++)
            Arrays.fill(distance[i], Integer.MAX_VALUE);
    }

    int dijkstra(int startIdx, int endIdx) {
        int answer = Integer.MAX_VALUE;
        distance[startIdx][0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(startIdx, 0, 0));

        while (!pq.isEmpty()) {
            Node current = pq.remove();

            if (current.index == endIdx) {
                answer = Math.min(answer, current.cost);
                continue;
            }

            if (current.cost > distance[current.index][current.state])
                continue;

            for (Node next : adjList.get(current.index)) {
                if (!isConnect(current, next))
                    continue;

                int newCost = current.cost + next.cost;
                int newState = getNewState(current, next);

                if (newCost >= distance[next.index][newState])
                    continue;

                distance[next.index][newState] = newCost;
                pq.add(new Node(next.index, newCost, newState));
            }
        }

        return answer;
    }

    boolean isConnect(Node current, Node next) {
        boolean isCurrentTrap = false;
        if (trapMap.containsKey(current.index))
            isCurrentTrap = ((current.state & (1 << trapMap.get(current.index))) != 0);

        boolean isNextTrap = false;
        if (trapMap.containsKey(next.index))
            isNextTrap = ((current.state & (1 << trapMap.get(next.index))) != 0);

        int relation = (isCurrentTrap ^ isNextTrap ? 1 : 0);
        return next.state == relation;
    }

    int getNewState(Node current, Node next) {
        int newState = current.state;
        if (trapMap.containsKey(next.index))
            newState ^= (1 << trapMap.get(next.index));
        return newState;
    }

}
