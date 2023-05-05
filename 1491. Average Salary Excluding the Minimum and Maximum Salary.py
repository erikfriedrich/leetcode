# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def average(self, salary: List[int]) -> float:
        
        # take sum of all salaries minus highest and lowest salary, then divide by the remaining number of salaries to get average excluding min and max
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)
