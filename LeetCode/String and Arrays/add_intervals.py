# [[1, 5], [6, 12], [14, 15]]
# [3, 6]

# result = [[1, 12]]
# interval_to_merge = [1, 12]
# curr_interval = [14, 15]

# TODO: I am missing an edge case somewhere

def add_interval(intervals, new_interval):
    result = []
    interval_to_merge = new_interval
    for i in range(len(intervals)):
        curr_interval = intervals[i]
        print('to merge', interval_to_merge)
        print('curr', curr_interval)
        if curr_interval[1] < interval_to_merge[0]:
            result.append(curr_interval)
        elif interval_to_merge[1] < curr_interval[0]:
            result.append(interval_to_merge)
            result.append(curr_interval)
        else:
            interval_to_merge = [min(curr_interval[0], interval_to_merge[0]), max(curr_interval[1], interval_to_merge[1])]
        print('to merge', interval_to_merge)
        print('curr', curr_interval)
        print(result)

    result.append(interval_to_merge)
    return result

add_interval([[1, 5], [6, 12], [14, 15]], [3, 6])


def add_interval(intervals, new_interval):
    result = []
    interval_to_merge = new_interval
    merged = False
    for i in range(len(intervals)):
        curr_interval = intervals[i]
        if curr_interval[1] < interval_to_merge[0]:
            result.append(curr_interval)
        elif interval_to_merge[1] < curr_interval[0]:
            result.append(interval_to_merge)
            result.append(curr_interval)
            merged = True
        else:
            interval_to_merge = [min(curr_interval[0], interval_to_merge[0]), max(curr_interval[1], interval_to_merge[1])]
    if not merged:
        result.append(interval_to_merge)
    return result