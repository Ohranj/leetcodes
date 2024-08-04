# Search Insert Position

def searchInsert(arr, target):
    indx = -1;
    for x in range(0, len(arr)):
        if arr[x] == target:
            indx = x;
            break;
        if arr[x] > target:
            indx = x
            break;
    if indx == -1:
        indx = len(arr);
    
    print(indx);

searchInsert([1, 3, 5, 6], 5)
searchInsert([1, 3, 5, 6], 2)
searchInsert([1, 3, 5, 6], 7)