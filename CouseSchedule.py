from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        in_degrees = defaultdict(set)
        out_degrees = defaultdict(set)
        for course, pre in prerequisites:
            out_degrees[course].add(pre)
            in_degrees[pre].add(course)
        
        courses_taken = 0
        in_degree_zero = []
        for i in range(numCourses):
            if not in_degrees[i]:
                courses_taken += 1
                in_degree_zero.append(i)
        
        while in_degree_zero:
            class_taken = in_degree_zero.pop()
            for course_to_take in out_degrees[class_taken]:
                in_degrees[course_to_take].remove(class_taken)
                if not in_degrees[course_to_take]:
                    courses_taken += 1
                    in_degree_zero.append(course_to_take)
                    
        return numCourses == courses_taken