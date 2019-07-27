from heapq import heappush, heappop, heapify
from collections import namedtuple, Counter

class Task(object):
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq
        
    def __lt__(self, other):
        # Intended to use python's min heap as a max heap
        return self.freq > other.freq

# TODO: Fix - Missing an edge case (Off by 1 error on leetcode)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get number of tasks
        num_tasks = len(tasks)
        
        # Get cool down time
        cool_down_time = n
        
        # Get idle cycles
        idle_cycles = 0
    
        # Get count of tasks        O(n)
        tasks = Counter(tasks)
        
        # Use a max heap to keep track of the task remaining
        # by frequency.             O(nlogn)
        remaining_tasks = [Task(name, freq) for name, freq in tasks.items()]  
        heapify(remaining_tasks)
        
        # Keep track of the tasks that are in cool down
        cool_down_tasks = {} # name, cool_down
       
        popped_tasks = []
        
        while popped_tasks or remaining_tasks:
            # Decrease the cool down time
            still_cooling_tasks = {}
            for task in cool_down_tasks:
                cool_down_tasks[task] -= 1
                if cool_down_tasks[task] >= 0:
                    still_cooling_tasks[task] = cool_down_tasks[task]
            cool_down_tasks = still_cooling_tasks
            
            # Add all popped tasks back to remaining task
            popped_tasks = Counter(popped_tasks)
            for name, freq in popped_tasks.items():
                heappush(remaining_tasks, Task(name, freq))
            popped_tasks = []
            
            # Pop from the max heap until we find a task
            # that is not being cooled down
            while remaining_tasks:
                next_task = heappop(remaining_tasks)
                if next_task.name in cool_down_tasks:
                    popped_tasks.append(next_task.name)
                    if next_task.freq > 1:
                        heappush(remaining_tasks, Task(next_task.name, next_task.freq-1))
                else:
                    cool_down_tasks[next_task.name] = cool_down_time
                    print(next_task.name, end=' ')
                    if next_task.freq > 1:
                        heappush(remaining_tasks, Task(next_task.name, next_task.freq-1))
                    break
    
            # If heap becomes empty we have to use an idle cycle
            # -> increment counter.
            if len(remaining_tasks) == 0 and len(popped_tasks) > 0:
                print('idle', end=' ')
                idle_cycles += 1
        print()
        return num_tasks + idle_cycles
