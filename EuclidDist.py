coord1 = [1, 5, 3]
coord2 = [6, 9, 8]

distance_to_calc = [coord1, coord2]

print(len(coord1) != len(coord2))

def euclid_dist_xy(coord1, coord2):
    dist = ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5
    print(dist)
    return dist


def euclid_dist_higher(coord1, coord2):
    if len(coord1) == len(coord2):
        n = len(coord1)
        for i in range (0, n):
            uunsquared = 0 
            unsquared = (coord1[i] - coord2[i]) ** 2
            uunsquared += unsquared 
        dist = (uunsquared) ** 0.5
        print(dist)
        return dist 

    else: 
        print("Invalid")


euclid_dist_higher(coord1, coord2)
