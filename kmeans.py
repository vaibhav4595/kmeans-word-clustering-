def get_euclidean_distance(vec1, vec2):
    dist = 0
    for i in xrange(0, len(vec1)):
        dist += (pow((vec1[i] - vec2[i]), 2))
    return dist

def change_centroid_dec(centroid, group, vec, grouplen):
    arr = [0 for i in xrange(0, len(vec))]
    for i in xrange(0, len(vec)):
        new = (grouplen * centroid[group][i]) - vec[i]
        new = float(new) / float(grouplen - 1)
        arr[i] = new
    centroid[group] = arr

def change_centroid_asc(centroid, group, vec, grouplen):
    arr = [0 for i in xrange(0, len(vec))]
    for i in xrange(0, len(vec)):
        new = (grouplen * centroid[group][i]) + vec[i]
        new = float(new) / float(grouplen + 1)
        arr[i] = new
    centroid[group] = arr

def kmeans_cluster(matrix, no_of_groups):

    specified = 25
    centroid = []

    group = {}
    for i in xrange(0, len(matrix)):
        group[i] = -1

    matrix_len = len(matrix)

    grouplen = [1 for i in xrange(0, no_of_groups)]   
    for i in xrange(0, no_of_groups):
        centroid.append(matrix[i])
        group[i] = i

    for i in xrange(0, matrix_len):
        length = float('inf')
        for j in xrange(0, no_of_groups):
            dist = get_euclidean_distance(matrix[i], centroid[j])
            if dist < length:
                length = dist
                new_group = j
        change_centroid_asc(centroid, new_group, matrix[i], grouplen[new_group])
        group[i] = new_group
        grouplen[group[i]] += 1

    iters = 0
    while iters != specified:
        for i in xrange(0, matrix_len):
            new_group = -1
            prev_len = get_euclidean_distance(matrix[i], centroid[group[i]])
            for j in xrange(0, no_of_groups):
                new_len = get_euclidean_distance(matrix[i], centroid[j])
                if new_len < prev_len:
                    prev_len = new_len
                    new_group = j
            if new_group != -1:
                if grouplen[group[i]] > 1:
                    change_centroid_dec(centroid, group[i], matrix[i], grouplen[group[i]])
                    grouplen[group[i]] -= 1
                    change_centroid_asc(centroid, new_group, matrix[i], grouplen[new_group])
                    group[i] = new_group
                    grouplen[group[i]] += 1
        iters += 1
        print iters
    return group, centroid
