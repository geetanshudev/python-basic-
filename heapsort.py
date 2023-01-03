def heapify (arr,N,i):
    largest = i #initialize largest as root
    l = 2*i+1 #left=2*i+1
    r = 2*i+2 #right=2*i+2
    
    #if left child of root exists and greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l
        
    #if right child of root exist and greater than root
    if r < N and arr[largest]  < arr[r]:
        largest = r
        
    #to change the root
    if largest != i:
        arr[i],arr[largest]=arr[largest],arr[i]
        
        heapify(arr,N,largest)
        
        
#heapsort

def heapSort (arr):
    N = len(arr)
    #to built maxheap
    for i in range(N//2-1,-1,-1):
        heapify(arr,N,i)
        
    #one by one extract element
    for i in range(N-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
        
#main program 

arr = [40,80,35,90,45,50,70]
print("unsorted list=>",arr)
heapSort(arr)
N=len(arr)
print("sorted list")
for i in range(N):
    print(arr[i],end=" ")