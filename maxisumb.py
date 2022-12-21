def SubarrayWithMaxSum(nums):
     
    # Initialize currMax and globalMax
    # with first value of nums
    currMax = nums[0]
    globalMax = nums[0]
 
    # Iterate for all the elements
    # of the array
    for i in range(1, len(nums)):
 
        # Update currMax
        currMax = max(nums[i],
                      nums[i] + currMax)
 
        # Check if currMax is greater
        # than globalMax
        if (currMax > globalMax):
            globalMax = currMax
            endIndex = i
     
    startIndex = endIndex
 
    # Traverse in left direction to
    # find start Index of subarray
    while (startIndex >= 0):
        globalMax -= nums[startIndex]
 
        if (globalMax == 0):
            break
 
        # Decrement the start index
        startIndex -= 1
     
    # Printing the elements of
    # subarray with max sum
    for i in range(startIndex, endIndex + 1):
        print(nums[i], end = " ")
     
# Driver Code
 
# Given array arr[]
arr = [ -2, -5, 6, -2,
        -3, 1, 5, -6 ]
 
# Function call
SubarrayWithMaxSum(arr)
