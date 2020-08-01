class DetectCap:
    def detectCapital(self, word):
        first = word[0].isupper()
        cap = 0
        n = len(word)
        for i in range(n):
            if word[i].isupper():
                cap += 1
            if first == True:
                if cap != 1 and cap != i+1: #USA
                    return False
                elif cap != 0: 
                    return False
        return True