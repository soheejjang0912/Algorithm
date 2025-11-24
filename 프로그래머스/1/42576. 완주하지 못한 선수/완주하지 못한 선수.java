// participant: 참여한 선수 이름 
// completion: 완주한 선수
// 완주하지 못한 선수의 이름을 return 
/*
동명이인 있음 -> 단순 포함 여부로 판단 불가 

1. participant, completion 정렬하기
2. participant 와 completion가 다른 순간 return 

*/ 
import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        // 1. participant, completion 정렬하기
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        // 2. participant 와 completion가 다른 순간 return
        for (int runner = 0; runner < completion.length; runner++){
            if (!participant[runner].equals(completion[runner])){
                return participant[runner];
            } 
        }
        
        return participant[participant.length-1];
    }
}