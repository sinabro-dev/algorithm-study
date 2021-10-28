package assignment01;

import java.io.*;

public class BOJ_2239_joonparkhere {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static int[][] board = new int[9][9];
    static boolean[][] isRowExist = new boolean[9][10];
    static boolean[][] isColExist = new boolean[9][10];
    static boolean[][] isBlockExist = new boolean[9][10];

    public static void main(String[] args) throws IOException {
        init();
        check(0);
    }

    static void init() throws IOException {
        int cur = 0;
        for (int i = 0; i < 9; i++) {
            String inputStr = br.readLine();

            for (char c : inputStr.toCharArray()) {
                int row = cur / 9;
                int col = cur % 9;

                int num = c - '0';
                board[row][col] = num;
                if (num != 0) {
                    isRowExist[row][num] = true;
                    isColExist[col][num] = true;
                    isBlockExist[3 * (row / 3) + (col / 3)][num] = true;
                }

                cur++;
            }
        }
    }

    static void check(int cur) throws IOException {
        if (cur == 81) {
            print();
            System.exit(0);
        }

        int row = cur / 9;
        int col = cur % 9;

        if (board[row][col] != 0) {
            check(cur + 1);
            return;
        }

        for (int num = 1; num <= 9; num++) {
            if (!isValid(cur, num))
                continue;

            isRowExist[row][num] = true;
            isColExist[col][num] = true;
            isBlockExist[3 * (row / 3) + (col / 3)][num] = true;
            board[row][col] = num;

            check(cur + 1);

            isRowExist[row][num] = false;
            isColExist[col][num] = false;
            isBlockExist[3 * (row / 3) + (col / 3)][num] = false;
            board[row][col] = 0;
        }
    }

    private static boolean isValid(int cur, int num) {
        int row = cur / 9;
        int col = cur % 9;

        if (isRowExist[row][num])
            return false;
        if (isColExist[col][num])
            return false;
        if (isBlockExist[3 * (row / 3) + (col / 3)][num])
            return false;

        return true;
    }

    private static void print() throws IOException {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                bw.append(String.valueOf(board[row][col]));
            }
            bw.newLine();
        }

        bw.flush();
        bw.close();
    }

}
