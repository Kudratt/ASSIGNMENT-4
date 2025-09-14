from collections import deque

def first_non_repeating(stream):
    q = deque()
    freq = {}
    for ch in stream:
        freq[ch] = freq.get(ch, 0) + 1
        q.append(ch)

        while q and freq[q[0]] > 1:
            q.popleft()

        if q:
            print(q[0], end=" ")
        else:
            print(-1, end=" ")

# Example
s = "aabc"
print("Input:", s)
print("Output:", end=" ")
first_non_repeating(s)
