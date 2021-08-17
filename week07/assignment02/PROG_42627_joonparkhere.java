package assignment02;

import java.io.*;
import java.util.*;

public class PROG_42627_joonparkhere {

    static class Job implements Comparable<Job> {
        int threshold;
        int cost;

        public Job(int[] arr) {
            this.threshold = arr[0];
            this.cost = arr[1];
        }

        @Override
        public int compareTo(Job o) {
            return this.cost - o.cost;
        }
    }

    public static int solution(int[][] jobs) {
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        PriorityQueue<Job> heap = new PriorityQueue<>();
        int result = 0, current = 0, idx = 0, numOfJob = jobs.length;

        while (true) {
            while ( (idx < numOfJob) && (jobs[idx][0] <= current) ) {
                heap.add(new Job(jobs[idx]));
                idx += 1;
            }

            if (heap.isEmpty()) {
                if (idx < numOfJob) {
                    current += 1;
                    continue;
                }
                else {
                    break;
                }
            }

            Job job = heap.remove();
            result += (current - job.threshold + job.cost);
            current += job.cost;
        }

        return result / numOfJob;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        int[][] jobs = new int[input.length / 2][2];
        for (int i = 0; i < input.length; i += 2) {
            jobs[i / 2][0] = Integer.parseInt(input[i]);
            jobs[i / 2][1] = Integer.parseInt(input[i + 1]);
        }

        int result = solution(jobs);
        bw.append(String.valueOf(result));
        bw.flush();
        bw.close();
    }

}
