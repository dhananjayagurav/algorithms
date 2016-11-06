#Code reference : http://quiz.geeksforgeeks.org/binary-search/

def bin_search(arr, ele):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-1)/2
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele:
            low = mid + 1
        else:
            high = mid -1
    #If element is not present in array, return -1
    return -1


myarr = (2,3,6,18,22,28,35,41,48,57,63,69,72,81)
key=35
index = bin_search(myarr, key)

print "Desired index of element in array is : " + str(index)
