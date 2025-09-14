from collections import deque

def interleave(q):
    n = len(q)
    if n % 2 != 0:
        print("Queue length must be even!")
        return
    half = n // 2
    first_half = deque()
    for _ in range(half):
        first_half.append(q.popleft())

    while first_half:
        q.append(first_half.popleft())
        q.append(q.popleft())
    return q


# Example
q = deque([4, 7, 11, 20, 5, 9])
print("Original Queue:", list(q))
print("Interleaved Queue:", list(interleave(q)))
