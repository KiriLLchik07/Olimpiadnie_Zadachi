def find_longest_ring(starting_ring, remaining_rings):
    possible_next_rings = [ring for ring in remaining_rings if ring[0] == starting_ring[-1][-1]]

    if len(possible_next_rings) == 0:
        if starting_ring[0][0] == starting_ring[-1][-1]:
            return len(starting_ring), starting_ring
        else:
            return -1, []

    ring_variants = []
    for next_ring in possible_next_rings:
        ring_variants.append(
            find_longest_ring(starting_ring + [next_ring], [ring for ring in remaining_rings if next_ring != ring]))

    return max(ring_variants, key=lambda x: x[0])

def main():
    ring_lengths = []
    with open("input_s1_03.txt") as file:
        file_lines = [line.strip() for line in file.readlines()]

        while file_lines:
            rings_dict = {
                ring: find_longest_ring([ring], [other_ring for other_ring in file_lines if ring != other_ring]) for
                ring in file_lines}
            max_ring = rings_dict[max(rings_dict, key=lambda x: rings_dict[x][0])]
            file_lines = [ring for ring in file_lines if ring not in max_ring[1]]
            ring_lengths.append(max_ring[0])

    print(len(ring_lengths))
    for length in ring_lengths:
        print(length)

if __name__ == "__main__":
    main()
