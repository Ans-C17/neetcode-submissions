class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses) }
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited = set()
        def dfs(currCourse):
            if currCourse in visited:
                return False
            if preMap[currCourse] == []: # the course can be finished if it ended up empty
                return True
            
            visited.add(currCourse)
            for prereq in preMap[currCourse]:
                if dfs(prereq) == False: 
                    return False
            
            visited.remove(currCourse) # 1->2->4 & 3->4 if 1,2,4 marked as visited then 4 is marked making 3 say its wrong without a cycle
            preMap[currCourse] = [] # memoization
            return True # o/w None would be returned making the if dfs(prereq) check to be False

        for course in range(numCourses): # so a disconnected graph is considered 
            if dfs(course) == False:
                return False
        
        return True