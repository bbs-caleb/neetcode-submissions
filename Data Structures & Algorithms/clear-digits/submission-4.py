class Solution:
    def clearDigits(self, s: str) -> str:
        stack_letters = []

        for e in s:
            if e.isalpha():
                stack_letters.append(e)
            if e.isdigit() and stack_letters:
                stack_letters.pop()
        return "".join(stack_letters)