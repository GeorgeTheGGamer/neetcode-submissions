class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Output list of list is graphs

        visited = set()
        time = 0
        fresh_count = 0
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        queue = deque()
        rows, cols = len(grid), len(grid[0])

        # Add all the rotten fruit to the queue, then take the minimum depth of it
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
                    # Keep the count of fresh till they are all gone
                elif grid[i][j] == 1:
                    fresh_count += 1
 
        while queue and fresh_count > 0:
            queue_len = len(queue)
            for _ in range(queue_len):
                curr_i, curr_j = queue.popleft()
                for direction in directions:
                    next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == 1 and (next_i,next_j) not in visited:
                        visited.add((next_i, next_j))
                        queue.append((next_i, next_j))
                        fresh_count -= 1
            
            time += 1
        

        if fresh_count == 0:
            return time
        else:
            return -1
        