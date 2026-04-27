from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Step 1: BFS to build graph (only shortest paths)
        parents = defaultdict(list)
        level = {beginWord}
        found = False
        
        while level and not found:
            next_level = set()
            wordSet -= level
            
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            if new_word == endWord:
                                found = True
                            next_level.add(new_word)
                            parents[new_word].append(word)
            
            level = next_level
        
        if not found:
            return []
        
        # Step 2: Backtrack to build paths
        res = []
        
        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])
        
        backtrack(endWord, [endWord])
        return res