def stack_sort_cherez_temp_stack(lst):
    temporary = []
    while lst:
        current = lst.pop()
        while temporary != Null and temporary[-1] < current:
            lst.append(temporary.pop())
        temporary.append(current)
    while temporary:
        lst.append(temporary.pop())