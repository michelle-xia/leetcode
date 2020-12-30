from collections import defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
        in_degrees = defaultdict(set)
        out_degrees = defaultdict(set)
        for course, pre in prerequisites:
            in_degrees[course].add(pre)
            out_degrees[pre].add(course)
            
        courses_taken = 0  
        course_order = []
        in_degree_zeros = []
        for i in range(numCourses):
            if not in_degrees[i]:
                in_degree_zeros.append(i)
                courses_taken += 1
                course_order.append(i)
              
        while in_degree_zeros:
            course_taken = in_degree_zeros.pop()
            for course_to_take in out_degrees[course_taken]:          
                in_degrees[course_to_take].remove(course_taken)
                if not in_degrees[course_to_take]:
                    courses_taken += 1
                    course_order.append(course_to_take)
                    in_degree_zeros.append(course_to_take)

        if numCourses == courses_taken:
            return course_order
        else:
            return []
            
        
        