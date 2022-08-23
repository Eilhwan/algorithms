public class MergeSort {

    int[] mergeSort(int[] arr){
        int[] tmp = new int[arr.length];
        mergeSort(arr, tmp, 0, arr.length - 1);
        return arr;
    }

    void mergeSort(int[] arr, int[] tmp, int left, int right){
        if(left < right){
            int mid = (left + right) / 2;
            mergeSort(arr, tmp, left, mid);
            mergeSort(arr, tmp, mid + 1, right);
            merge(arr, tmp, left, mid, right);
        }
    }
    void merge(int[] arr, int[] tmp, int left, int mid, int right){
        for(int i = left; i <= right; i++){
            tmp[i] = arr[i];
        }
        int pi1 = left;
        int pi2 = mid + 1;
        int index = left;

        while (pi1 <= mid && pi2 <= right){
            if (tmp[pi1] <= tmp[pi2]){
                arr[index] = tmp[pi1];
                pi1++;
            }else{
                arr[index] = tmp[pi2];
                pi2++;
            }
            index++;
        }
        for(int i = 0; i <= mid - pi1; i++){
            arr[index + 1] = tmp[pi1 + 1];
        }
    }

    public static void main(String[] args) {
        int[] arr = {4, 3, 2, 1};
        MergeSort m = new MergeSort();
        int[] sorted_arr = m.mergeSort(arr);
        for (int e: sorted_arr) {
            System.out.println(e);
        }
    }
}
