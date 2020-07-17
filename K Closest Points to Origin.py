# Time Complexity - O (N * log K) - N is length of points and min heap of size 'K'

import heapq

class Solution:
    def kClosest(self, points, K):
        
        heap = []
        
        for (x,y) in points:
            
            dist = -(x*x + y*y)
            
            if (len(heap) == K):
                heapq.heappushpop(heap, (dist,x,y))
                # heappushpop combines the functioning of both push and pop operations in one statement, increasing efficiency and heap order is maintained after this operation 
                
            else:
                heapq.heappush(heap, (dist,x,y))
                # Inserting element into heap, order is adjusted so heap structure is maintained
        
        # Returning K closest points in the heap
        closestPoints = []
        for (dist, x, y) in heap:
            closestPoints.append((x,y))
            
        return closestPoints

points = [[3,3],[5,-1],[-2,4]]
K = 2

print(Solution().kClosest(points,K))