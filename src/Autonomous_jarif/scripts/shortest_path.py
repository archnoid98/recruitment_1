import heapq

def solution(array, start, goal):
        
        directions=[(1,0),(-1,0),(0,1),(0,-1)]   # downward , upward , right , left

        open_set=[] #priority_queue array
        heapq.heappush(open_set,(0,start))
        came_from={} #dictionary of the current node and it's origin
        cost_so_far={start:0} #dictionary of the node and it's cost

        while open_set:
            current_cost, current_node = heapq.heappop(open_set)


            if current_node==goal:
                    path=[]
                    while current_node in came_from: #current_node =(0,0)
                        path.append(current_node)

                        current_node=came_from[current_node]

                    path.reverse()
                    return path



            for direction in directions:
                    next_node=(current_node[0]+direction[0],current_node[1]+direction[1]) #touple
 
                    if 0<=next_node[0]<len(array) and 0<=next_node[1]<len(array[0]) and array[next_node[0]][next_node[1]]!=1:

                        new_cost=cost_so_far[current_node]+1

                        if next_node not in cost_so_far or cost_so_far[next_node]>new_cost:
                            cost_so_far[next_node]=new_cost
                            heapq.heappush(open_set,(new_cost,next_node))
                            came_from[next_node]=current_node
    
 
 
map_array = [
    [0, 0, 0, 0, 0],
    [2, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 3],
]
 
 
start_position = (1, 0)
goal_position = (4, 4)
 
path = solution(map_array, start_position, goal_position)
 
if path:
    print("Optimal Path:", path)
else:
    print("No path found.")