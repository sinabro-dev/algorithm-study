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
        boardSize = n;
        isRowExist = new boolean[n];
        isColExist = new boolean[n];
        isDiagonalAExist = new boolean[2 * n - 1];
        isDiagonalBExist = new boolean[2 * n - 1];

        place(0);

        return answer;
    }

    private static void place(int start) {
        if (placed == boardSize) {
            answer++;
            return;
        }

        for (int pos = start; pos < boardSize * boardSize; pos++) {
            if (!canPlace(pos))
                continue;

            isRowExist[pos / boardSize] = true;
            isColExist[pos % boardSize] = true;
            isDiagonalAExist[getDiagonalAIdx(pos)] = true;
            isDiagonalBExist[getDiagonalBIdx(pos)] = true;
            placed++;

            place(nextPos(pos));

            isRowExist[pos / boardSize] = false;
            isColExist[pos % boardSize] = false;
            isDiagonalAExist[getDiagonalAIdx(pos)] = false;
            isDiagonalBExist[getDiagonalBIdx(pos)] = false;
            placed--;
        }
    }

    private static boolean canPlace(int pos) {
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

    private static int nextPos(int cur) {
        if (boardSize <= 2)
            return cur + 1;

        int next = ((cur / boardSize) + 1) * boardSize;

        while (true) {
            if (!(next - boardSize == cur || next - boardSize + 1 == cur || next - boardSize - 1 == cur))
                break;
            next++;
        }
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
