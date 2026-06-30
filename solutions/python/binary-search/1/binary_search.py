def find(search_list, value):
    search_list.sort()
    if value in search_list:
        return search_list.index(value)
    raise ValueError('value not in array')