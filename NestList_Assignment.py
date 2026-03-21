""" 
Write a code that separates positive and negative numbers into positiveList[ ]and negativeList[ ] for any pre-defined nested list,. For example,
#pre-defined list
nList = [[-2,5,-99,99],[-3,8,1,-2,10],[1,-7,100,-10]]
Output: Positive Numbers = [[5, 99], [8, 1, 10], [1, 100]]
Output: Negative Numbers = [[-2, -99], [-3, -2], [-7, -10]]
"""

nList = [[-2,5,-99,99],[-3,8,1,-2,10],[1,-7,100,-10]]
positive = []
negative = []

for sublist in nList:
    positive_sub = []
    negative_sub = []
    
    for num in sublist:
        if num > 0:
            positive_sub.append(num)
        else:
            negative_sub.append(num)
    positive.append(positive_sub)
    negative.append(negative_sub)
print(f"Output: Positive Numbers = ", positive)
print(f"Output: Negative Numbers = ", negative)