class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        #dict[abr]=word
        self.dic={}
        for word in set(dictionary):
            if len(word)<=2:abr=word
            else:
                abr=word[0]+str(len(word)-2)+word[-1]
            if abr not in self.dic:
                self.dic[abr]=word
            else:self.dic[abr]=False

    def isUnique(self, word: str) -> bool:
        #true:abr of word is not key of dic/ in dict and dict[abr]==word
        #false:in dict and dict[abr]!=word
        if len(word)<=2:abr=word
        else:
            abr=word[0]+str(len(word)-2)+word[-1]
        if abr in self.dic and ( not self.dic[abr]==word or self.dic[abr]==False):
            return False
        return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)