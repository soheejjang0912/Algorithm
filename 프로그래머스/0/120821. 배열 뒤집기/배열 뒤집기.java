class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            result[i] = num_list[n - 1 - i];
        }

        return result;
    }
}
