#!/usr/bin/python3

# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/
def queue_time(customers, n):
    customers.reverse()
    tills = [0] * n
    time = 0
    while any(customers + tills):
        tills = [t if t else customers.pop() if customers else 0 for t in tills]
        time += (next_customer := min(filter(None, tills))) if any(tills) else 0
        tills = [*map(lambda x: max(x - next_customer, 0), tills)]
    return time
