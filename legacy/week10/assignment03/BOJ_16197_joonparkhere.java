package assignment03;

import java.io.*;
import java.util.*;

public class BOJ_16197_joonparkhere {

    static class Coin {
        int row;
        int col;

        Coin(int row, int col) {
            this.row = row;
            this.col = col;
        }

        boolean canMove() {
            if (row >= 0 && row < rowSize && col >= 0 && col < colSize && board[row][col] == -1)
                return false;
            return true;
        }

        boolean isDropped() {
            if (row >= 0 && row < rowSize && col >= 0 && col < colSize)
                return false;
            return true;
        }
    }

    static class Element {
        int count;
        List<Coin> coinList;

        public Element(int count, List<Coin> coinList) {
            this.count = count;
            this.coinList = coinList;
        }
    }

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static final int MAX_COUNT = 10;
    static final int DIRECTION_NUM = 4;
    static final int[] dRow = {-1, 0, 1, 0};
    static final int[] dCol = {0, 1, 0, -1};

    static int rowSize;
    static int colSize;
    static int[][] board;
    static List<Coin> initCoinList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        solve();
    }
    
    static void init() throws IOException {
        String[] inputStr = br.readLine().split(" ");
        rowSize = Integer.parseInt(inputStr[0]);
        colSize = Integer.parseInt(inputStr[1]);
        board = new int[rowSize][colSize];

        for (int row = 0; row < rowSize; row++) {
            String states = br.readLine();
            for (int col = 0; col < colSize; col++) {
                switch (states.charAt(col)) {
                    case 'o':
                        initCoinList.add(new Coin(row, col));
                    case '.':
                        board[row][col] = 1;
                        break;
                    case '#':
                        board[row][col] = -1;
                        break;
                }
            }
        }
    }

    static void solve() throws IOException {
        boolean[][][][] isVisit = new boolean[rowSize][colSize][rowSize][colSize];
        isVisit[initCoinList.get(0).row][initCoinList.get(0).col][initCoinList.get(1).row][initCoinList.get(1).col] = true;

        Queue<Element> queue = new LinkedList<>();
        queue.add(new Element(0, initCoinList));

        while (!queue.isEmpty()) {
            Element current = queue.remove();

            if (current.count >= MAX_COUNT) break;

            for (int direction = 0; direction < DIRECTION_NUM; direction++) {
                List<Coin> nextCoinList = new ArrayList<>();
                int droppedCount = 0;

                for (Coin coin : current.coinList) {
                    int nextRow = coin.row + dRow[direction];
                    int nextCol = coin.col + dCol[direction];
                    Coin nextCoin = new Coin(nextRow, nextCol);

                    if (!nextCoin.canMove()) {
                        nextCoin.row = coin.row;
                        nextCoin.col = coin.col;
                    }
                    if (nextCoin.isDropped())
                        droppedCount++;

                    nextCoinList.add(nextCoin);
                }

                if (droppedCount == 1) {
                    bw.append(String.valueOf(current.count + 1));
                    bw.flush();
                    bw.close();
                    return;
                }
                if (droppedCount == 0) {
                    if (!isVisit[nextCoinList.get(0).row][nextCoinList.get(0).col][nextCoinList.get(1).row][nextCoinList.get(1).col]) {
                        isVisit[nextCoinList.get(0).row][nextCoinList.get(0).col][nextCoinList.get(1).row][nextCoinList.get(1).col] = true;
                        queue.add(new Element(current.count + 1, nextCoinList));
                    }
                }
            }
        }

        bw.append("-1");
        bw.flush();
        bw.close();
    }

}
