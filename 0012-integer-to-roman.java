class Solution {
    public String intToRoman(int num) {
        String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] digits = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

        String roman = "";
        for (int i = 0; i < digits.length; ++i) {
            roman += romans[i].repeat(num / digits[i]);
            num %= digits[i];
        }

        return roman;
    }
}
