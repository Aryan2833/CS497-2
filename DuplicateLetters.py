def removeDuplicateLetters(s):
    stack = []

    letter_count = {char: s.count(char) for char in s}

    in_stack = set()

    for char in s:
        letter_count[char] -= 1

        if char in in_stack:
            continue

        while stack and char < stack[-1] and letter_count[stack[-1]] > 0:
            in_stack.remove(stack.pop())

        stack.append(char)

        in_stack.add(char)

    return ''.join(stack)


s1 = "bcabc"
result1 = removeDuplicateLetters(s1)
print(result1)

s2 = "cbacdcbc"
result2 = removeDuplicateLetters(s2)
print(result2)