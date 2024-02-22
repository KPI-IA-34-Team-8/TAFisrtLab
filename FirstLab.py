# Team 8
import random
import time
import math

# o is the counter of how many replacements were done in the function.

def bubble_sort(arr):
    l=len(arr)
    o = 0
    for i in range(len(arr)-1):
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                o += 1
    return o

def modified_bubble_sort(arr):
    l=len(arr)
    o = 0
    for i in range(l-1):
        flag = 0
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1]:
                flag=1
                arr[j],arr[j+1]=arr[j+1],arr[j]  
                o += 1
        if flag==0:
            break
    return o

def shell_sort_knuth(arr):
    jump = 0
    l = len(arr)
    o = 0
    while jump < l:
        jump = jump * 3 + 1
    jump = round(jump)
    while jump > 0:
        for i in range(jump, l):
            v = arr[i]
            ii = i
            while ii > jump - 1 and arr[ii - jump] >= v:
                arr[ii] = arr[ii - jump]
                o += 1
                ii = ii - jump
            arr[ii] = v
            o += 1
        jump = round((jump - 1)/3)
    return o

        

def test_sort(amount: int, alg: callable[[list], int], sorting: int = 1) -> str:
    """Tests the sorting alogrithms in the code.

    Args:
        amount (int): The length of the array that will be created
        alg (function): The function that will sort the array in ascending order that will return the amount of replacements that were done during the sorting of the algorithm
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
    print("Unsorted array:")
    # we do this to make sure we can dump it into a txt file
    # otherwise it errors
    print(str(arr).encode("utf-8"))
    # get the time in nanoseconds
    # note: time does not change after a nanosecond, it changes after a millisecond
    # so we can't take the array and sort it one time and do time_start - time_end, because it will = 0
    start_time = time.time_ns()
    # times we ran the sorting alogrithms
    ran = 0
    # the amount of replacements we have done (required in the report)
    o = 0
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
            # get the amount of replacements we have done in the array that was sorted
            o = alg(arr)
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
    print("Sorted array:")
    print(str(arr).encode("utf-8"))
    print("Amount of replacements in the array:")
    print(o)
    if hours > 1:
        return f"Ran the code {ran} times. Time required for one run is: \nApprox. {hours} hours {minutes} minutes {seconds} seconds"
    elif minutes > 1:
        return f"Ran the code {ran} times. Time required for one run is: \nApprox. {minutes} minutes {seconds} seconds"
    elif seconds > 1:
        return f"Ran the code {ran} times. Time required for one run is: \nApprox. {seconds} seconds {ms} ms"
    elif ms > 1:
        return f"Ran the code {ran} times. Time required for one run is: \nApprox. {ms} ms"
    return f"Ran the code {ran} times. Time required for one run is: \nApprox. {micros} μs"
        


if __name__ == "__main__":
    # not doing the following as required:
    # "for i in [10, 100, 1000, 5000, 10000, 20000, 50000]:"
    # due to the fact it takes a lot of time to do 20000, so it will take a lot more time to sort an array with 50000 elements
    amounts = [10, 100, 1000, 5000, 10000]
    print("Running the tests..")
    for i in amounts:
        print(f"\n\n\nTesting modified bubble sort with {i} elements:")
        print("\nTest on a sorted algorithm:")
        print(test_sort(i, modified_bubble_sort, 1).encode("utf-8"))
        print("\nTest on an \"opposite\" sorted algorithm:")
        print(test_sort(i, modified_bubble_sort, 2).encode("utf-8"))
        print("\nTest on an unsorted algorithm:")
        print(test_sort(i, modified_bubble_sort, 3).encode("utf-8"))
    print("\n\n\n")
    for i in amounts:
        print(f"\n\n\nTesting bubble sort with {i} elements:")
        print("\nTest on a sorted algorithm:")
        print(test_sort(i, bubble_sort, 1).encode("utf-8"))
        print("\nTest on an \"opposite\" sorted algorithm:")
        print(test_sort(i, bubble_sort, 2).encode("utf-8"))
        print("\nTest on an unsorted algorithm:")
        print(test_sort(i, bubble_sort, 3).encode("utf-8"))
    print("\n\n\n")
    for i in amounts:
        print(f"\n\n\nTesting shell sort (Knuth sequence) with {i} elements:")
        print("\nTest on a sorted algorithm:")
        print(test_sort(i, shell_sort_knuth, 1).encode("utf-8"))
        print("\nTest on an \"opposite\" sorted algorithm:")
        print(test_sort(i, shell_sort_knuth, 2).encode("utf-8"))
        print("\nTest on an unsorted algorithm:")
        print(test_sort(i, shell_sort_knuth, 3).encode("utf-8"))