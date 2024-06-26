'''http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
We have discussed a Divide and Conquer based O(nLogn) solution for this 
    problem. In this post, O(n) time solution is discussed. Like the previous 
    post, width of all bars is assumed to be 1 for simplicity. For every bar ‘x’, 
    we calculate the area with ‘x’ as the smallest bar in the rectangle. If we 
    calculate such area for every bar ‘x’ and find the maximum of all areas, 
    our task is done. How to calculate area with ‘x’ as smallest bar? We need 
    to know index of the first smaller (smaller than ‘x’) bar on left of ‘x’ 
    and index of first smaller bar on right of ‘x’. Let us call these indexes 
    as ‘left index’ and ‘right index’ respectively.
We traverse all bars from left to right, maintain a stack of bars. Every bar 
    is pushed to stack once. A bar is popped from stack when a bar of smaller 
    height is seen. When a bar is popped, we calculate the area with the popped 
    bar as smallest bar. How do we get left and right indexes of the popped 
    bar – the current index tells us the ‘right index’ and index of previous 
    item in stack is the ‘left index’. Following is the complete algorithm.

1) Create an empty stack.

2) Start from first bar, and do following for every bar ‘hist[i]’ where ‘i’ 
    varies from 0 to n-1.
……a) If stack is empty or hist[i] is higher than the bar at top of stack, then 
    push ‘i’ to stack.
……b) If this bar is smaller than the top of stack, then keep removing the top of 
    stack while top of the stack is greater. Let the removed bar be hist[tp]. 
    Calculate area of rectangle with hist[tp] as smallest bar. For hist[tp], the 
    ‘left index’ is previous (previous to tp) item in stack and ‘right index’ is 
    ‘i’ (current index).

3) If the stack is not empty, then one by one remove all bars from stack and do 
    step 2.b for every removed bar.
'''


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stk, ans = [], 0
        for i, h in enumerate(heights + [0]):
            while stk and heights[stk[-1]] > h:
                cur = heights[stk.pop()]
                width = i if not stk else i-stk[-1]-1
                ans = max(ans, cur*width)
            stk.append(i)
        return ans
