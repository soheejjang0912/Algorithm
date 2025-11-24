import java.util.HashMap;

class Solution {

    // 핵심 로직은 solution에, 반복적인 작업만 함수로 분리한 버전
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> playerCountMap = countParticipants(participant);

        // 완주자 차감
        for (String completionName : completion) {
            playerCountMap.put(completionName, playerCountMap.get(completionName) - 1);
        }

        // 남은 사람 찾기
        for (String playerName : playerCountMap.keySet()) {
            if (playerCountMap.get(playerName) > 0) {
                return playerName;
            }
        }

        return "";
    }

    // 참가자 카운팅만 함수로 분리
    private HashMap<String, Integer> countParticipants(String[] participantList) {
        HashMap<String, Integer> playerCountMap = new HashMap<>();
        for (String participantName : participantList) {
            playerCountMap.put(participantName, playerCountMap.getOrDefault(participantName, 0) + 1);
        }
        return playerCountMap;
    }
}