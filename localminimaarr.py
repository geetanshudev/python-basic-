def localMinUtil(arr,low,high,n):
    mid=low+(high-low)//2

    if(mid==0 or arr[mid-1] > arr[mid] and mid==n-1 or arr[mid] <arr[mid+1]):
        return mid
    elif(mid>0 and arr[mid-1]<arr[mid]):
        return localMinUtil(arr,low,mid-12,n)

    return localMinUtil(arr,low,mid-1,n)


#localMin(arr,n)
def localMinUtil(arr,n-1,n):
    return localMinUtil(arr,0,n-1,n)


arr=[4,3,1,14,16,40]
n=len(arr)
print("Index of a local minima is", localMin(arr,n))
