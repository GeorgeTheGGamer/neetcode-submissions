class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = defaultdict(list)

        for crs, pres in prerequisites:
            preMap[crs].append(pres)
    
        visited = set()

        def traverse(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            

            visited.add(crs)

            # Check every dependency, if ever false return false up stream
            for dependency in preMap[crs]:
                if not(traverse(dependency)):
                    return False
                
            # Backtrack from that choice
            visited.remove(crs)
            preMap[crs] = []                # None of our paths resulted in false
            return True
            

        for crs in range(numCourses):
            if not(traverse(crs)):
                return False

        return True
                



        