class Solution {
    public int solution(int price) {
        double discountRate = 0.0;

        if (price >= 500000) {
            discountRate = 0.20;
        } else if (price >= 300000) {
            discountRate = 0.10;
        } else if (price >= 100000) {
            discountRate = 0.05;
        }

        return (int)(price * (1 - discountRate));
    }
}
