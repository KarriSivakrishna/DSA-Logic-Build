class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        setWord = set(word)

        first = 0
        last = 0

        count = 0

        for char in setWord:
            if char.islower():
                if char.upper() in word:
                    first = word.find(char.upper())
                    last = word.rfind(char)

                    if first < 0:
                        first = 0
                    if last < 0:
                        last = 0

                    if last < first:
                        count += 1
        
        return count