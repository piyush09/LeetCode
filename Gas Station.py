class Solution:
    def canCompleteCircuit(self, gas, cost):
        
        sumGas = 0 # Initializing sum of gas values to 0
        sumCost = 0 # Initializing sum of cost values to 0
        start = 0 # To maintain start index
        tank = 0 # To maintain the amount of fuel in the tank
        
        for i in range(len(gas)):
            sumGas += gas[i]
            sumCost += cost[i]
            tank += gas[i]-cost[i]
            
            if(tank<0): # Whenever tank is getting to negative value, we are increasing the start index 
                start = i+1
                tank = 0
        
        if (sumGas < sumCost): # If sum of gas is less than sum of cost, there won't be a solution
            return -1
        else:
            return start


gas  = [2,3,4]
cost = [3,4,3]       
print (Solution().canCompleteCircuit(gas, cost))