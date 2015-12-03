__author__ = 'mdu'
def next_permutation(arr,k):
    # Reverse k+1...n suffix to skip k+1...n positions permutations
    arr[k : ] = arr[len(arr) - 1 : k - 1 : -1]
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True

n,k=([int(i) for i in input().split()])
#arr = [0, 1, 2, 3]
arr=[i for i in range(n)]
#k=2
while True:
    print(*arr[0 :k])
    if not next_permutation(arr,k):
        exit(0)
