import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Solution {
    private Map<String, String> digitToLetters = Map.of(
            "2", "abc",
            "3", "def",
            "4", "ghi",
            "5", "jkl",
            "6", "mno",
            "7", "pqrs",
            "8", "tuv",
            "9", "wxyz"
    );

    public List<String> letterCombinations(String digits) {
        List<String> combinations = new ArrayList<>();
        List<String> combination = new ArrayList<>();
        if(digits.length() > 0) dfs(digits, 0, combination, combinations);
        return combinations;
    }

    public void dfs(String digits, int index, List<String> combination, List<String> combinations) {
        if (combination.size() == digits.length()) {
            String comb = String.join("", combination);
            combinations.add(comb);
            return;
        }

        String digit = String.valueOf(digits.charAt(index));
        String letters = digitToLetters.get(digit);
        for (int i = 0; i < letters.length(); ++i) {
            char letter = letters.charAt(i);
            combination.add(String.valueOf(letter));
            dfs(digits, index + 1, combination, combinations);
            combination.remove(combination.size() - 1);
        }
    }
}
