package assignment03;

import java.io.*;
import java.util.*;

public class BOJ_2589_joonparkhere {

    static final int[] dRow = {-1, 0, 1, 0};
    static final int[] dCol = {0, -1, 0, 1};

    static char[][] board;
    static int maxCost;

    static class Point {
        int row;
        int col;

        public Point(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        solve();
    }

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int rowSize = Integer.parseInt(st.nextToken());
        int colSize = Integer.parseInt(st.nextToken());

        board = new char[rowSize][colSize];
        for (int row = 0; row < rowSize; row++) {
            String input = br.readLine();
            for (int col = 0; col < colSize; col++)
                board[row][col] = input.charAt(col);
        }
    }

    static void solve() throws IOException {
        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board[0].length; col++) {
                if (board[row][col] == 'W') continue;
                bfs(new Point(row, col));
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.append(String.valueOf(maxCost));
        bw.flush();
        bw.close();
    }

    static void bfs(Point start) {
        Queue<Point> queue = new LinkedList<>();
        queue.add(start);

        int[][] cost = new int[board.length][board[0].length];
        for (int row = 0; row < board.length; row++)
            for (int col = 0; col < board[0].length; col++)
                cost[row][col] = -1;
        cost[start.row][start.col] = 0;

        while (!queue.isEmpty()) {
            Point current = queue.remove();

            for (int i = 0; i < dRow.length; i++) {
                int row = current.row + dRow[i];
                int col = current.col + dCol[i];

                if (row < 0 || row >= board.length || col < 0 || col >= board[0].length) continue;
                if (board[row][col] == 'W' || cost[row][col] != -1) continue;

                queue.add(new Point(row, col));
                cost[row][col] = cost[current.row][current.col] + 1;
                if (cost[row][col] > maxCost)
                    maxCost = cost[row][col];
            }
        }
    }

}
