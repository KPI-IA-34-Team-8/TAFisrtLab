# Team 8
import random
import time
import math

# o is the counter of how many replacements were done in the function.
# p is the counter of how many comparisons there were done in the function.

def bubble_sort(arr):
    l=len(arr)
    o = 0
    p = 0
    for i in range(len(arr)-1):
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                o += 1
            p += 1
    return o, p

def modified_bubble_sort(arr):
    l=len(arr)
    o = 0
    p = 0
    for i in range(l-1):
        flag = 0
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1]:
                flag=1
                arr[j],arr[j+1]=arr[j+1],arr[j]  
                o += 1
            p += 1
        if flag==0:
            break
        p += 1
    return o, p

def shell_sort_knuth(arr):
    jump = 0
    l = len(arr)
    o = 0
    p = 1
    while jump < l:
        jump = jump * 3 + 1
        p += 1
    jump = round(jump)
    p += 1
    while jump > 0:
        for i in range(jump, l):
            v = arr[i]
            ii = i
            p += 2
            while ii > jump - 1 and arr[ii - jump] >= v:
                arr[ii] = arr[ii - jump]
                o += 1
                ii = ii - jump
                p += 2
            arr[ii] = v
            o += 1
        jump = round((jump - 1)/3)
        p += 1
    return o, p



def test_sort(amount: int, alg: callable, sorting: int = 1) -> str:
    """Tests the sorting alogrithms in the code.

    Args:
        amount (int): The length of the array that will be created
        alg (function): The function that will sort the array in ascending order that will return 2 ints: 1st being o, second being p (look at lines 6-7 for explanation)
        sorting (int, optional): The type of sorting. 1 = in (ascending) order, 2 in opposite (descending) order, 3 = in random order. Defaults to 1.

    Returns:
        str: _description_
    """
    arr = []
    # first sorting is in (ascending) order.
    if sorting == 1:
        last_el = 0
        for i in range(amount):
            last_el = random.randint(last_el, (amount+last_el))
            arr.append(last_el)
    # second sorting is in opposite (descending) order
    elif sorting == 2:
        last_el = 0
        for i in range(amount):
            last_el = random.randint(last_el, (amount+last_el))
            arr.insert(0, last_el) 
    # third sorting is in random order
    elif sorting == 3:
        for i in range(amount):
            arr.append(random.randint(0,100000000000))
    # get the time in nanoseconds
    # note: time does not change after a nanosecond, it changes after a millisecond
    # so we can't take the array and sort it one time and do time_start - time_end, because it will = 0
    start_time = time.time_ns()
    # times we ran the sorting alogrithms
    ran = 0
    # lines 6-7 for explanation
    o = 0
    p = 0
    # we do sorting a ton of times, but if it takes more than a second then we stop
    for i in range(1000000):
        # we copy the array so that the original array does not get sorted
        # (if we don't sort, it'll get sorted the first time and the sorting algorithms may quit early)
        alg(arr.copy())
        # increase the amount of times we ran
        ran += 1
        # if we have done sorting for more than one second
        if time.time_ns() - start_time > 10**9:
            # we sort the original array 
            # lines 6-7 for explanations
            o, p = alg(arr)
            ran += 1
            break
    # https://gist.github.com/dakaugu/d01213ae54f304900f5e918dd07953ad
    # devided by (10**9) to get seconds
    elapsed_time = (time.time_ns() - start_time) / ((10**9) * ran)
    hours = elapsed_time / 3600
    elapsed_time = elapsed_time - math.floor(hours) * 3600
    minutes = elapsed_time / 60
    elapsed_time = elapsed_time - math.floor(minutes) * 60
    seconds = elapsed_time
    elapsed_time = elapsed_time - math.floor(seconds)
    ms = elapsed_time * 1000
    micros = elapsed_time * 1000 * 1000
    rs = f"Amount of replacements that were done: {o}\nAmount of comparisons that were done: {p}\n"
    rse = ""
    # we encode in utf 8 to be able to dump it into a file
    # commented out due to the fact that we actually don't need to manually check the array if it's sorted or not..
    # rse = f"\nSorted array:\n{str(arr).encode('utf-8')}"
    if hours > 1:
        return f"{rs}Ran the code {ran} times. Time required for one run is: \nApprox. {hours} hours {minutes} minutes {seconds} seconds{rse}"
    elif minutes > 1:
        return f"{rs}Ran the code {ran} times. Time required for one run is: \nApprox. {minutes} minutes {seconds} seconds{rse}"
    elif seconds > 1:
        return f"{rs}Ran the code {ran} times. Time required for one run is: \nApprox. {seconds} seconds {ms} ms{rse}"
    elif ms > 1:
        return f"{rs}Ran the code {ran} times. Time required for one run is: \nApprox. {ms} ms{rse}"
    return f"{rs}Ran the code {ran} times. Time required for one run is: \nApprox. {micros} microseconds{rse}"



if __name__ == "__main__":
    # not doing the following as required:
    # "for i in [10, 100, 1000, 5000, 10000, 20000, 50000]:"
    # due to the fact it takes a lot of time to do 20000, so it will take a lot more time to sort an array with 50000 elements
    amounts = [10, 100, 1000, 5000, 10000]
    sorting = [[1, "a sorted array"], [2, "an \"opposite\" sorted array"], [3, "an unsorted array"]]
    algorithm = [[bubble_sort, "bubble sort"], [modified_bubble_sort, "modified bubble sort"], [shell_sort_knuth, "shell sort (Knuth sequence)"]]
    for j in sorting:
        print("\n")
        print(f"Testing algorithms on {j[1]}:")
        for i in amounts:
                print("\n")
                print(f"{i} elements tests:")
                for k in algorithm:
                    print("\n")
                    print(f"Testing {k[1]} sort with {i} elements:")
                    print(test_sort(i, k[0], j[0]))