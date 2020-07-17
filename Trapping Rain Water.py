class Solution:
    def trap(self, height):
        
        if not height:
            return 0
        
        ans = 0  # result value
        n = len(height) # number of elements in the array
        
        left_max = [0]*n
        right_max = [0]*n
        
        # Filling left_max array
        left_max[0] = height[0] # Assigning value to 0th element of left_max array
        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i])
            
        # Filling right_max array
        right_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1], height[i])
          
        # Adding the water amount collected for each bar(index) in the array
        for i in range(0,n):
            ans += (min(left_max[i], right_max[i]) - height[i])
            
        return ans
            
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))