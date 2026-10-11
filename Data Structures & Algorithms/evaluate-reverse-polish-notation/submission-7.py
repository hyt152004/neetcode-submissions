class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if number append to stack

        # if arith take out all the values and perform
            # append the result
        stack = []

        for t in tokens:

            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))

        return stack[-1]
            