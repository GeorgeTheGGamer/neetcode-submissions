class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # Goal is to start DFS from each cell on the edge and mark as not safe
        # Then we clean up at the end

        visited = set()
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        rows, cols = len(board), len(board[0])

        def traverse(i,j):
            if (i,j) in visited:
                return

            board[i][j] = 'T'
            visited.add((i,j))

            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and board[next_i][next_j] == 'O':          
                    traverse(next_i, next_j)
        

        # First we find all the O's that are bordering
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows-1 or j == cols-1) and board[i][j] == 'O':
                    traverse(i,j)


        # Next we change all the # to O and O to X
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                    continue
                if board[i][j] == 'O':
                    board[i][j] = 'X'


            

        