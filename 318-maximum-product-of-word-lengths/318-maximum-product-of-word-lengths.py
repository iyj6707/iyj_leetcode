class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        bits = []
        for word in words:
            bits.append(self.word_to_bits(word))
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bits[i] & bits[j] == 0:
                    max_len = max(max_len, len(words[i]) * len(words[j]))
        return max_len
        
    def word_to_bits(self, s):
        bits = 0
        for c in s:
            bits |= 1 << (ord(c) - ord('a'))
        return bits