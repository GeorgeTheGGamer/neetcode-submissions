from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def traverse(crs):
            # Bad Case: Cycle detected
            if crs in visited:
                return False
            # Good Case: No dependencies left
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            # Check all dependencies
            for pre in preMap[crs]:
                if not traverse(pre):  # If a cycle is found deeper down, return False immediately
                    return False
            
            visited.remove(crs) # Backtrack
            preMap[crs] = []    # Optimization: clear dependencies so we don't re-check this course later
            return True
        
        # Loop for every single course
        for i in range(numCourses):
            if not traverse(i):  # If any course has a cycle, we can't finish
                return False
        
        return True