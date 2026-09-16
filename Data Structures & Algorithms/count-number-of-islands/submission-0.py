class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        count = 0

        def traverse(i,j):
            if (i,j) in visited:
                return
            
            # Need to explore the entire island
            visited.add((i,j))
            for direction in directions:
                next_i, next_j = i+direction[0], j+direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == "1":
                    traverse(next_i,next_j)
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == "1":
                    traverse(i,j)
                    count += 1
                    
        return count

            
        
