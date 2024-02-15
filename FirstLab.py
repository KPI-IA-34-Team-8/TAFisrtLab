# Team 8
import random
import time
import math

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

        

def test_sort(amount, alg, sorting=1):
    arr = []
    if sorting == 1:
        last_el = 0
        for i in range(amount):
            last_el = random.randint(last_el, (amount+last_el))
            arr.append(last_el)
    elif sorting == 2:
        last_el = 0
        for i in range(amount):
            last_el = random.randint(last_el, (amount+last_el))
            arr.insert(0, last_el) 
    elif sorting == 3:
        for i in range(amount):
            arr.append(random.randint(0,100000000000))
    # print("Created an array with the size of " + str(amount))
    print("Unsorted array:")
    print(str(arr).encode("utf-8"))
    start_time = time.time_ns()
    ran = 0
    o = 0
    for i in range(1000000):
        o += alg(arr.copy())
        ran += 1
        if time.time_ns() - start_time > 1000000000:
            o += alg(arr)
            ran += 1
            break
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
    print("Running the tests..")
    for i in [10, 100, 1000, 5000, 10000]:
    # for i in [10, 100, 1000, 5000, 10000, 20000, 50000]:
        print(f"\n\n\nTesting modified bubble sort with {i} elements:")
        print("\nTest on a sorted algorithm:")
        print(test_sort(i, modified_bubble_sort, 1).encode("utf-8"))
        print("\nTest on an \"opposite\" sorted algorithm:")
        print(test_sort(i, modified_bubble_sort, 2).encode("utf-8"))
        print("\nTest on an unsorted algorithm:")
        print(test_sort(i, modified_bubble_sort, 3).encode("utf-8"))
    print("\n\n\n")
    for i in [10, 100, 1000, 5000, 10000]:
    # for i in [10, 100, 1000, 5000, 10000, 20000, 50000]:
        print(f"\n\n\nTesting bubble sort with {i} elements:")
        print("\nTest on a sorted algorithm:")
        print(test_sort(i, bubble_sort, 1).encode("utf-8"))
        print("\nTest on an \"opposite\" sorted algorithm:")
        print(test_sort(i, bubble_sort, 2).encode("utf-8"))
        print("\nTest on an unsorted algorithm:")
        print(test_sort(i, bubble_sort, 3).encode("utf-8"))
    print("\n\n\n")
    for i in [10, 100, 1000, 5000, 10000]:
    # for i in [10, 100, 1000, 5000, 10000, 20000, 50000]:
        print(f"\n\n\nTesting shell sort (Knuth sequence) with {i} elements:")
        print("\nTest on a sorted algorithm:")
        print(test_sort(i, shell_sort_knuth, 1).encode("utf-8"))
        print("\nTest on an \"opposite\" sorted algorithm:")
        print(test_sort(i, shell_sort_knuth, 2).encode("utf-8"))
        print("\nTest on an unsorted algorithm:")
        print(test_sort(i, shell_sort_knuth, 3).encode("utf-8"))
    
