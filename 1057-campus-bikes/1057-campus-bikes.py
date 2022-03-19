class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def find_distance(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])
        
        worker_to_bike_list = []
        pq = []
        
        for worker, worker_loc in enumerate(workers):
            curr_worker_pairs = []
            for bike, bike_loc in enumerate(bikes):
                distance = find_distance(worker_loc, bike_loc)
                curr_worker_pairs.append((distance, worker, bike))
            
            curr_worker_pairs.sort(reverse=True)
            heapq.heappush(pq, curr_worker_pairs.pop())
            worker_to_bike_list.append(curr_worker_pairs)
            
        bike_status = [False] * len(bikes)
        worker_status = [-1] * len(workers)
        
        while pq:
            distance, worker, bike = heapq.heappop(pq)
            
            if not bike_status[bike]:
                bike_status[bike] = True
                worker_status[worker] = bike
            else:
                next_closest_bike = worker_to_bike_list[worker].pop()
                heapq.heappush(pq, next_closest_bike)
        
        return worker_status