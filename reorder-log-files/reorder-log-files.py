class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #The letter-logs come before all digit-logs
        letterlog=[]
        digitlog=[]
        for log in logs:
            if log[-1].isdigit():
                digitlog.append(log)
            else:
                letterlog.append(log)
        
        #The letter-logs are sorted lexicographically by their contents then idf.
        letterlog.sort(key=lambda i: (i.split(" ")[1:],i.split(" ")[0]))
        print(letterlog,digitlog)
        return letterlog+digitlog
        
        