def minTimeToVisitAllPoints(points):
    totalVisitTime = 0
    for i in range(len(points) - 1):
        xShift = abs(points[i + 1][0] - points[i][0])
        yShift = abs(points[i + 1][1] - points[i][1])
        totalVisitTime += max(xShift, yShift)

    return totalVisitTime

points = [[1,1],[3,4],[-1,0]]
print (minTimeToVisitAllPoints(points))
