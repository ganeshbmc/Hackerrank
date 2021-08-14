def matches_played(L):
    return len(L)

def average(L):
    return sum(L)/len(L)

def count_scores(L, T):
    return len([score for score in L if (T[0] <= score < T[1]) ])

def score_ranges(L):
    ranges = [(0, 10), (10, 50), (50, 100), (100, 500)]
    return {T:count_scores(L, T) for T in ranges}

# L stands for list, T stands for tuple

# Test case
import random
l1 = [random.randint(0,500) for i in range(20)]
# print(l1)
print(matches_played(l1))
print(average(l1))
# print(count_scores(l1, (100, 500)))
print(score_ranges(l1))