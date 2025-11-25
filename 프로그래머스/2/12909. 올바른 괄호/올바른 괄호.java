import java.util.ArrayDeque;

// if ( push
// if ) pop

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        ArrayDeque<Character> stak = new ArrayDeque<>();
        
        char[] a = s.toCharArray();
        
        for (char c : a){ 
            if(c == '('){
                stak.push(c);
            }else{
                if(stak.isEmpty()){
                    return false;
                }
                stak.pop();
            }
        } 

        if(stak.isEmpty()){
            return true;
        }else{
            return false;
        } 
    }
}