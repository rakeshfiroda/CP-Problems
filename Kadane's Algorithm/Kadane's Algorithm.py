def maxSubArraySum(a,size):
    ##Your code here
    maximum = a[0]
    temp = 0
    for i in a:
        temp += i
        if temp > maximum:
            maximum = temp
        if temp < 0:
            temp = 0
        
    return maximum
