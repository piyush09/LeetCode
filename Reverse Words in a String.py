class Solution:
    def reverseWords(self, s):
        
        s = " ".join(s.split()) # Removing multiple spaces in between words and joining them by single space 
        s = s.strip() # Removing whitespace at beginning and end of string
        words = s.split(' ') # Splitting the string by space
        string = [] # Initializing the string list as empty
        
        for word in words:
            string.insert(0, word) # Iterating through each word and inserting into string list at the beginning
            
        return (" ".join(string)) # Returning the joined string
        
str = "a good   example"
print(Solution().reverseWords(str))