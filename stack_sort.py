def stack_sort_cherez_temp_stack(start_stack):
    temporary = []
    while start_stack:
        current = lst.pop()
        while (temporary != Null and temporary[-1] < current):
            start_stack.append(temporary.pop())
        temporary.append(current)
    while temporary != Null:
        start_stack.append(temporary.pop())