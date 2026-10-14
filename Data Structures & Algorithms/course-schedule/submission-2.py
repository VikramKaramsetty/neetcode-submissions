class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}
        for i in range(len(prerequisites)):
            courseMap[prerequisites[i][0]].append(prerequisites[i][1])
        visited = set()
        def dfs(num):
            if(courseMap[num] == []): return True
            if(num in visited): return False

            visited.add(num)
            for i in courseMap.get(num):
                val = dfs(i)
                if not val: return False
            courseMap[num] = []
            visited.remove(num)
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True
