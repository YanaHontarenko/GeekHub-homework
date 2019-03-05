# You have a histogram.
# Try to find the size of the largest rectangle,
# which can be constructed from histogram columns.

def findMaxGist(gist):
    result = []
    for i in range(0, len(gist)):
        result.append(gist[i])
        for j in range(i + 1, len(gist)):
            if gist[i] <= gist[j]:
                result[i] = result[i] + gist[i]
            else:
                break
    return result


gist = [2, 1, 4, 5, 1, 3, 3]
answer = findMaxGist(gist)
print(max(answer))
