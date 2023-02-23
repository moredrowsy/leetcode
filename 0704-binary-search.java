class Solution {
    public int search(int[] nums, int target) {
        // Binary search template

        // left pointer always 0
        int left = 0;
        // right pointer always lenght of array - 1 to ensure index bounds
        int right = nums.length - 1;

        // ((left + 1 < right) conditional only if length >= 2
        // lenght=1; left=0; right=1-1=0; (0 + 1 < 0)=false; no while loop
        // lenght=2; left=0; right=2-1=1; (0 + 1 < 1)=false; no while loop
        // length=3; left=0; right=3-1=2; (0 + 1 < 2)=true; yes while loop
        while (left + 1 < right) {

            // (left + right) / 2; might result in int overflow
            // (right-left) / 2; prevents int overflow
            int mid = left + (right - left) / 2;

            if (target == nums[mid]) {
                return mid;
            } else if (target < nums[mid]) {
                right = mid;
            } else {
                left = mid;
            }
        }

        // For lenght=1 or lenght=2 or not found
        if (target == nums[left]) {
            return left;
        } else if (target == nums[right]) {
            return right;
        } else {
            return -1;
        }
    }
}
