package dataStructures;

import java.util.ArrayList;
import java.util.List;

public class Nhn3 {
    public static void main(String[] args) {
        // 갈등의 갯수
        int[][] conflicts = {{3, 4}, {3, 5}};
        solution(4, conflicts);
    }


    public static void solution(int n, int[][] conflicts){
        // 아이들 수는 8 고정
        int totalCase = 1;
        int[] kids = {1, 2, 3, 4, 5, 6, 7, 8};


        ArrayList<Integer> permutations = new ArrayList<>();
        for(int i = 0; i < kids.length; i++){
            permutations(permutations, 0, 0, 8);
        }

        for(int i = 1; i < 9; i++){
            totalCase *= i;
        }

        // 경우의 수를 뺀다.



        System.out.println(totalCase);
    }

    private static ArrayList<ArrayList<Integer>> permutations(int[] kid, int depth, int r, int n) {

        ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();

        for(int i = 0; i < n; i++) {
            arr.(permutation(kid, i, r, n));
        }

        return arr;
    }

    private static ArrayList<Integer> permutation(int[] list, int depth, int r, int n){
        int i = list.length - 1;
        int j = list.length - 1;

        /** 1. 꼭대기 찾기 **/
        while(i > 0 && list[i-1] >= list[i]) --i;
        if(i <= 0) return false;	// 꼭대기가 0번째 인덱스라면 마지막순열

        /** 2. j값 찾기 **/
        while(list[i-1] > list[j]) --j;
        swap(i-1,j);

        /** 3. 순서 정해주기 **/
        j = list.length - 1;
        for(; i < j; ++i, --j) {
            swap(i,j);
        }
        return true;
    }

}
