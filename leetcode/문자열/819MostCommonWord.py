from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('[^A-Za-z0-9 ]',' ', paragraph.lower())
        words = words.split()
        words = Counter(words)
        for i in banned:
            if(words.get(i)): 
                words[i] = -1
        return words.most_common(1)[0][0]
