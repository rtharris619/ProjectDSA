# Write a function, combine_intervals, that takes in a list of intervals as an argument. 
# Each interval is a tuple containing a pair of numbers representing a start and end time. 
# Your function should combine overlapping intervals and return a list containing the combined intervals

# For example:
# Given two intervals:
# (1, 4) and (3, 7)
# The intervals overlap and
# should be combined into:
# (1, 7)
# You may return the combined intervals in any order.

# You can assume that the input list contains at least one interval and all intervals are valid with start < end.

# Method:
# Sort by start time of the intervals.
# [ (1,4), (3,7), (8,13), (12,15), (13,14) ]
# Check subsequent intervals for overlap and append if it's not included, otherwise check if you can extend current interval.

def combine_intervals_old(intervals):
    res = []
    intervals = sorted(intervals)
    last = intervals[0]
    res.append(last)

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= last[1]:
            if interval[1] > last[1]:
                res[-1] = (last[0], interval[1])
            else:
                res[-1] = last
        else:
            res.append(interval)
        last = res[-1]

    return res

# Cleaner code and removed unneccessary variable
def combine_intervals(intervals):
    intervals = sorted(intervals, key=lambda interval:interval[0])
    res = [intervals[0]]

    for current_interval in intervals[1:]:
        current_start, current_end = current_interval
        last_start, last_end = res[-1]
        if current_start <= last_end:
            if current_end > last_end:
                res[-1] = (last_start, current_end)
        else:
            res.append(current_interval)

    return res

def driver():
    intervals = [
        (1, 4),
        (12, 15),
        (3, 7),
        (8, 13),
        (13, 14)
    ]
    res = combine_intervals(intervals) # -> [ (1, 7), (8, 15) ]
    print(res)

    intervals = [
        (3, 7),
        (5, 8),
        (1, 5),
    ]
    res = combine_intervals(intervals) # -> [ (1, 8) ]
    print(res)

    intervals = [
        (3, 7),
        (10, 13),
        (5, 8),
        (27, 31),
        (1, 5),
        (12, 16),
        (20, 22),
    ]
    res = combine_intervals(intervals) # -> [ (1, 8), (10, 16), (20, 22), (27, 31) ]
    print(res)

    intervals = [
        (64, 70),
        (50, 55),
        (62, 65),
        (12, 50),
        (72, 300000),
    ]
    res = combine_intervals(intervals) # -> [ (12, 55), (62, 70), (72, 300000) ]
    print(res)