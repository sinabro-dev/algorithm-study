package assignment01;

import java.io.*;
import java.util.*;

public class BOJ_2239_joonparkhere {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static final int SUDOKU_SIZE = 9;

    static int[][] board = new int[SUDOKU_SIZE][SUDOKU_SIZE];
    static List<int[]> candidateList = new ArrayList<>();
    static int[] isRowExist = new int[SUDOKU_SIZE];
    static int[] isColExist = new int[SUDOKU_SIZE];
    static int[] isBlockExist = new int[SUDOKU_SIZE];

    public static void main(String[] args) throws IOException {
        init();
        check(0);
    }

    static void init() throws IOException {
        for (int row = 0; row < SUDOKU_SIZE; row++) {
            String inputStr = br.readLine();

            for (int col = 0; col < SUDOKU_SIZE; col++) {
                board[row][col] = inputStr.charAt(col) - '0';

                if (board[row][col] == 0) {
                    candidateList.add(new int[]{row, col});
                } else {
                    int digit = 1 << board[row][col];
                    isRowExist[row] |= digit;
                    isColExist[col] |= digit;
                    isBlockExist[3 * (row / 3) + (col / 3)] |= digit;
                }
            }
        }
    }

    static void check(int idx) throws IOException {
        if (idx == candidateList.size()) {
            print();
            System.exit(0);
        }

        int row = candidateList.get(idx)[0];
        int col = candidateList.get(idx)[1];
        int curDigit = isRowExist[row] | isColExist[col] | isBlockExist[3 * (row / 3) + (col / 3)];

        for (int value = 1; value <= SUDOKU_SIZE; value++) {
            int nextDigit = 1 << value;

            if ((curDigit & nextDigit) != 0)
                continue;

            board[row][col] = value;
            isRowExist[row] |= nextDigit;
            isColExist[col] |= nextDigit;
            isBlockExist[3 * (row / 3) + (col / 3)] |= nextDigit;

            check(idx + 1);

            board[row][col] = 0;
            isRowExist[row] &= ~nextDigit;
            isColExist[col] &= ~nextDigit;
            isBlockExist[3 * (row / 3) + (col / 3)] &= ~nextDigit;
        }
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
