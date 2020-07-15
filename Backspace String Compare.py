class Solution:
    def backspaceCompare(self, S, T):
        
        ## Bruteforce solution
        stringList1 = []
        stringList2 = []
        for char in S: # Reading each character of the string S
            if char == "#" and (len(stringList1) != 0): # Checking if character is '#' and stringList1 is not empty 
                stringList1.pop()
            
            elif ((len(stringList1) == 0) and char == "#"): # If stringList1 is empty and char is "#", then do nothing
                pass # pass denotes do nothing condition in Python
                
            else:
                stringList1.append(char) # In the other case, appending the particular character to the list
        # print (stringList1)
            
        for char in T: # Reading each character of the string T
            if char == "#" and (len(stringList2) != 0):
                stringList2.pop()
            
            elif ((len(stringList2) == 0) and char == "#"):
                pass
            
            else:
                stringList2.append(char)
        # print (stringList2)
        
        if len(stringList1) != len(stringList2): # If lengths of two stringLists are not equal then they cannot be equal
            return False
        
        length = len(stringList1)
        final_list = [] # Making final_list to check difference between stringList1 and stringList2 
        for i in range(0,length):
            if (stringList1[i] == stringList2[i]): # Checking each character of both the lists
                pass
            else:
                final_list.append(stringList1[i])
        
        if (len(final_list) == 0): # If final_list is empty then stringList1 and stringList2 are same, hence they are equal strings
            return True
        else:
            return False

S = "a##c"
T = "#a#c"

print(Solution().backspaceCompare(S, T))