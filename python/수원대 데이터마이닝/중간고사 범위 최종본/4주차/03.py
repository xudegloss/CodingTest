def remove_dups(s):
    stack=[s[0]]
    for idx in range(1, len(s)):
        if stack:
            if stack[-1]==s[idx]:
                stack.pop()
            else:
                stack.append(s[idx])
        else:
            stack.append(s[idx])

    return "".join(list(map(str, stack)))

print(remove_dups("caaa"))
print(remove_dups("accab"))
print(remove_dups("baccaaac"))