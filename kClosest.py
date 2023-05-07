def kClosest(points,k):
    result = []
    final_result = []
    for i in range(len(points)):
        dist = math.sqrt((points[i][0])**2 + (points[i][1]) **2)
        result.append(dist)
    for i in range(1,len(result)):
        temp = result[i]
        temp2 = points[i]
        j = i -1
        while temp < result[j] and j > -1:
            result[j+1] = result[j]
            points[j+1] = points[j]
            result[j] = temp
            points[j] = temp2
            j -= 1
    for c in range(k):
        final_result.append(points[c])
    return final_result
