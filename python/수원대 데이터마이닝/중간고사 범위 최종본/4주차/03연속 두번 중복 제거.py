def remove_dups(s):
    stack=[s[0]]
    for idx in range(1, len(s)):
        if len(stack)==0:
            stack.append(s[idx])
            break

        if s[idx]==stack[-1]:
            stack.pop()
        else:
            stack.append(s[idx])
    return "".join(map(str, stack))
    pass
    

print(remove_dups("caaa"))
print(remove_dups("accab"))
print(remove_dups("baccaaac"))