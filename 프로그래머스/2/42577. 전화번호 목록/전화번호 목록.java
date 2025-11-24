/*
1. phone_book을 sort 시킨다.
2. phone_book을 순회하며 
    phone_book[i]와 그 뒤의 전화번호를 비교한다.
*/

import java.util.Arrays;
class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book); 
        
        for (int index = 0; index < phone_book.length -1; index++){
            String currentNumber = phone_book[index];
            String nextNumber = phone_book[index+1];
            
            if (nextNumber.startsWith(currentNumber)){
                return false;
            }
        }
         
        return true;
    }
}