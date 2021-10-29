package assignment01;

import java.io.*;
import java.util.*;

public class BOJ_2239_joonparkhere {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static final int SUDOKU_SIZE = 9;

    static int[][] board = new int[SUDOKU_SIZE][SUDOKU_SIZE];
    static List<int[]> candidateList = new ArrayList<>();
    static boolean[][] isBlockExist = new boolean[SUDOKU_SIZE][SUDOKU_SIZE + 1];
    static boolean[][] isRowExist = new boolean[SUDOKU_SIZE][SUDOKU_SIZE + 1];
    static boolean[][] isColExist = new boolean[SUDOKU_SIZE][SUDOKU_SIZE + 1];

    public static void main(String[] args) throws IOException {
        init();
        check(0);
    }

    private static void updateExist(int row, int col, int value) {
        int blockIdx = 3 * (row / 3) + (col / 3);
        isBlockExist[blockIdx][value] = !isBlockExist[blockIdx][value];
        isRowExist[row][value] = !isRowExist[row][value];
        isColExist[col][value] = !isColExist[col][value];
    }

    static void init() throws IOException {
        for (int row = 0; row < SUDOKU_SIZE; row++) {
            String inputStr = br.readLine();

            for (int col = 0; col < SUDOKU_SIZE; col++) {
                int value = inputStr.charAt(col) - '0';
                board[row][col] = value;

                if (value == 0) {
                    candidateList.add(new int[]{row, col});
                } else {
                    updateExist(row, col, value);
                }
            }
        }
    }

    static void check(int idx) throws IOException {
        if (idx == candidateList.size()) {
            print();
            System.exit(0);
        }

        int[] candidate = candidateList.get(idx);
        int row = candidate[0], col = candidate[1];

        for (int value = 1; value <= SUDOKU_SIZE; value++) {
            if (!isValid(row, col, value))
                continue;

            updateExist(row, col, value);
            board[row][col] = value;

            check(idx + 1);

            updateExist(row, col, value);
            board[row][col] = 0;
        }
    }

    private static boolean isValid(int row, int col, int value) {
        int blockIdx = 3 * (row / 3) + (col / 3);
        if (isBlockExist[blockIdx][value])
            return false;
        if (isRowExist[row][value])
            return false;
        if (isColExist[col][value])
            return false;

        return true;
    }

    private static void print() throws IOException {
        for (int row = 0; row < SUDOKU_SIZE; row++) {
            for (int col = 0; col < SUDOKU_SIZE; col++)
                bw.append(String.valueOf(board[row][col]));
            bw.newLine();
        }

        bw.flush();
        bw.close();
    }

}
