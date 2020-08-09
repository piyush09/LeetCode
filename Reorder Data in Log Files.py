"""
Algo: Divide the logs into two parts - digitLogs and letterLogs.
      Sort the letter logs by first identifier in case of tie and then by suffix in it.
      Put digitLogs after letterLogs and return the result.

T.C. - O(N log N) - as custom sorting is being used in it, in addition O(N) time for iterating through logs list.
S.C. - O(N) - as space required to store digitLogs and letterLogs in it.
"""

class Solution:
    def reorderLogFiles(self, logs):
        
        # Initialising empty lists of letterLogs and digitLogs
        letterLogs = []
        digitLogs = []
        
        for log in logs:
            
            # If the string after splitting is digit, then append it to digits log list
            if log.split()[1].isdigit():
                digitLogs.append(log)
                
            else:
                letterLogs.append(log)
            
        # When suffix is same, split by identifier value (0th of the string after splitting)
        letterLogs.sort(key = lambda x:x.split()[0])
        
        letterLogs.sort(key = lambda x:x.split()[1:]) # Sorting by suffix
        
        resultLogs = letterLogs + digitLogs # Adding digitLogs after letterLogs
        
        return resultLogs

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

print (Solution().reorderLogFiles(logs))