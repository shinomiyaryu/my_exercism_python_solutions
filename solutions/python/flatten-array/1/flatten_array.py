def flatten(iterable):
    flat_array = []
    def nested_lists(new_list):
        for item in new_list:
            if item != None and type(item) != list:
                flat_array.append(item)
            elif type(item) == list:
                nested_lists(item)
    nested_lists(iterable)
  
    return flat_array
    #pass
