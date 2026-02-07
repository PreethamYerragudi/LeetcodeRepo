# Problem 735: Asteroid Collision
# Difficulty: Medium
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i, a in enumerate(asteroids):
            destroyed = False
            while stack and (stack[-1] * a < 0) and a < 0:
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                elif abs(stack[-1]) > abs(a):
                    destroyed = True
                    break
                else:
                    stack.pop()
                    destroyed = True
                    break
            if not destroyed:
                stack.append(a)
        return stack
                    