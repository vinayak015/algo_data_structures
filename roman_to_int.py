class Solution:
    def romanToInt(self, s: str) -> int:
        r2d = {
            'I': 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for r in s:
            num = r2d[s]
