class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_freq = 0
        max_len =0
        right = 0
        left = 0
        char_frequency = {}


        for right in range(len(s)):
            char_frequency[s[right]] = char_frequency.get(s[right], 0) + 1
            max_freq = max(max_freq, char_frequency[s[right]])
            while (right - left + 1) - max_freq > k:
                char_frequency[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left +1)
        return max_len