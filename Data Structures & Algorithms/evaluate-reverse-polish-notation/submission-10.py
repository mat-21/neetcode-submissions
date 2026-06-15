class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for t in tokens:
            if t in operators:
                print(t)
                result = None
                right = int(stack.pop())
                left = int(stack.pop())
                if t == '+':
                    result = left + right
                elif t == '-':
                    result = left - right
                elif t == '*':
                    result = left * right
                elif t == '/':
                    result = int(float(left) / right)

                stack.append(result)
            else:
                stack.append(t)
            print(stack)
        return int(stack.pop())