def stack_sort_cherez_temp_stack(start_stack):
    if (start_stack == []):
        return 0
    temporary = []
    while start_stack:
        current = start_stack.pop()
        while (temporary != None and temporary[-1] < current):
            start_stack.append(temporary.pop())
        temporary.append(current)
    while temporary != None:
        start_stack.append(temporary.pop())
print(stack_sort_cherez_temp_stack([]))