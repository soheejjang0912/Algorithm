import java.util.*;

class Solution {
    public int solution(int[] array) { 
        
        HashMap<Integer, Integer> hm = new HashMap<>();
        
        for(int num : array){
            hm.put(num, hm.getOrDefault(num, 0) +1);
        }
        
        int maxCount = 0;
        int answer = -1;
        boolean isDup = false;
        
        for(Map.Entry<Integer, Integer> entry : hm.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
            
            if(value > maxCount){
                maxCount = value;
                answer = key;
                isDup = false;
                
            } else if(value == maxCount){
                isDup = true;
            }
        }
        
        return isDup ? -1 : answer;
    }
}
