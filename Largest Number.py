class Solution:
    
    def largestNumber(self, nums):
        
        # Parameter nums is a list of integers
        num = list(map(str, nums))  # Converting "integer" list to "string" list
        # map() doesn't return a list in python 3, so using list() it can be converted to list
        
        def mycomparator(a,b): 
            if a+b>b+a:  # if a+b is greater then returning 1 in maximum function 
                return 1 
            elif a+b<b+a :
                return -1
            else:
                return 0
      
    # "cmp_to_key" function converts a cmp= function into a key= function 
    #  It is because the list.sort() method no longer accepts a cmp function in Python 3
        def cmp_to_key(mycmp):
            'Convert a cmp= function into a key= function'
            class K(object):
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0
                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0
                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0
                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0  
                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0
                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0
            return K
        
        
        num.sort(key = cmp_to_key(mycomparator),reverse = True) # Sorting list elements in descending order using mycomparator() function
        
        return str(int(''.join(num))) # Concatenating items in list to strings
        """
        :type nums: List[int]
        :rtype: str
        """      

nums = [10,2]
print(Solution().largestNumber(nums))