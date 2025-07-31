class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def palindrome(s):
            return s == s[::-1]
        
        wordIdx = {}
        palindromeSet = set()
        emptySet = set()
        for i, word in enumerate(words):
            r_word = word[::-1]
            if word == r_word:
                if word != '': palindromeSet.add(i)
                else: emptySet.add(i)
            wordIdx[r_word] = i
                
        ans = []
        ''' three cases to consider:
            (1) 'abcd' + 'dcba' (word[i]== word[j][::-1]) 
            (2) 's' + 'lls' ('ll' prefix of 'lls' is a palindrome, the suffix 's' can form a palindrome with some word with prefix 's')   
            (3) '' + any palindrome is a valid answr (i, j), (j, i)
        '''

        for i, word in enumerate(words):
            
            # case 1
            if word in wordIdx and wordIdx[word] != i:
                ans.append([i, wordIdx[word]])

            # case 2
            for j in range(1, len(word)):
                prefix, suffix = word[:j], word[j:]
                if palindrome(prefix) and suffix in wordIdx:
                    ans.append([wordIdx[suffix], i])
                if palindrome(suffix) and prefix in wordIdx:
                    ans.append([i, wordIdx[prefix]])
        # case 3
        for i in emptySet:
            for j in palindromeSet:
                ans.append([i, j])
                ans.append([j, i])
        
        return ans

                


        