def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        index = 0
        hamming_distance = 0
        for letter in strand_a:
            if letter != strand_b[index]:
                hamming_distance += 1
                index += 1
            else:
                index += 1
        return hamming_distance
    raise ValueError("Strands must be of equal length.")
    #pass
