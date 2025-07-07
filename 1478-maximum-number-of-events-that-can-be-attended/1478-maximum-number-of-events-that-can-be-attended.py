import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()

        heap = []
        day = 1
        attended = 0
        i = 0

        while i < n or heap:

            # this loop for the current day adds all 
            #   started events end times in the heap
            while i < n and day >= events[i][0]:
                heapq.heappush(heap, events[i][1])
                i += 1

            # This loop pops from the heap greedily the
            # events with closest end date and attends 
            # the first one it finds. If all the events are 
            # poped and they all ended before the current day,
            # no event is attended for that day
            while heap:
                end_date = heapq.heappop(heap)
                if end_date >= day:
                    attended += 1
                    break
            
            # increment the day
            day += 1
        
        return attended