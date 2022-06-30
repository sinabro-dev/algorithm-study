package assignment03;

import java.io.*;

public class PROG_12952_joonparkhere {

    private static int boardSize;
    private static int placed = 0;
    private static int answer = 0;

    private static boolean[] isRowExist;
    private static boolean[] isColExist;
    private static boolean[] isDiagonalAExist;
    private static boolean[] isDiagonalBExist;

    public static int solution(int n) {
        setUp(n);
        backTracking(0);
        return answer;
    }

    private static void setUp(int n) {
        boardSize = n;
        isRowExist = new boolean[n];
        isColExist = new boolean[n];
        isDiagonalAExist = new boolean[2 * n - 1];
        isDiagonalBExist = new boolean[2 * n - 1];
    }

    private static void backTracking(int start) {
        if (placed == boardSize) {
            answer++;
            return;
        }

        for (int i = 0; i < boardSize; i++) {
            int pos = start + i;

            if (!canPlace(pos))
                continue;

            updateExist(pos, true);
            placed++;

            backTracking(nextQueen(pos));

            updateExist(pos, false);
            placed--;
        }
    }

    private static boolean canPlace(int pos) {
        if (pos >= boardSize * boardSize)
            return false;

        if (isRowExist[pos / boardSize])
            return false;
        if (isColExist[pos % boardSize])
            return false;
        if (isDiagonalAExist[getDiagonalAIdx(pos)])
            return false;
        if (isDiagonalBExist[getDiagonalBIdx(pos)])
            return false;

        return true;
    }

    private static void updateExist(int pos, boolean value) {
        isRowExist[pos / boardSize] = value;
        isColExist[pos % boardSize] = value;
        isDiagonalAExist[getDiagonalAIdx(pos)] = value;
        isDiagonalBExist[getDiagonalBIdx(pos)] = value;
    }

    private static int getDiagonalAIdx(int pos) {
        if (boardSize == 1)
            return 0;

        if (pos == 0)
            return 0;
        if (pos == boardSize * boardSize - 1)
            return isDiagonalAExist.length - 1;

        int remain = pos % (boardSize - 1);
        boolean isSmall = pos < (boardSize - 1) * (remain + 1);

        if (isSmall)
            return remain;
        else
            return remain + (boardSize - 1);
    }

    private static int getDiagonalBIdx(int pos) {
       if (boardSize == 1)
            return 0;
        if (boardSize == 2)
            switch (pos) {
                case 1:
                    return 0;
                case 0:
                case 3:
                    return 1;
                case 2:
                    return 2;
            }

        int remain = pos % (boardSize + 1);
        boolean isSmall = pos < (boardSize + 1) * (((boardSize - 1) - remain) + 1);

        if (isSmall)
            return (boardSize - 1) - remain;
        else
            return (boardSize - 1) + (boardSize + 1) - remain;
    }

    private static int nextQueen(int cur) {
        if (boardSize <= 2)
            return cur + 1;

        int next = ((cur / boardSize) + 1) * boardSize;

        while (next - boardSize == cur || next - boardSize + 1 == cur || next - boardSize - 1 == cur)
            next++;

        return next;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int answer = solution(N);

        bw.append(String.valueOf(answer));
        bw.flush();
        bw.close();
    }

}
