# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:12:19 2021

@author: Asus
"""

import random
import math
from bokeh.plotting import figure, output_file, show
import collections
import numpy as np 
POINTS_COLOURS = ['turquoise', 'lime', 'dodgerblue', 'fuchsia', 'lightcoral', 'navajowhite']
CLUSTERS_COLOURS = ['teal', 'green', 'blue', 'purple', 'red', 'goldenrod']
SIZE_VECTOR = 10
MIN_LIMIT_POINTS = 1
MAX_LIMIT_POINTS = 30
NUM_VECTORS = 100
NUM_CLUSTERS = 4

def generate_random_vector(numVectors, random_low_number, random_high_number):
    random_vectors = []
    n = int(numVectors/2)
    n2= numVectors-n
    a = np.random.multivariate_normal([10,0], [[3,1], [1,4]], size=[n,])
    b = np.random.multivariate_normal([0,20], [[3,1], [1,4]], size=[n2,])
 
    for i in range(n): 
        vector = [a[i][0],a[i][1]]
        random_vectors.append(vector)
        vector2 = [b[i][0],b[i][1]]
        random_vectors.append(vector2)
    
 
    #random_vectors = []
    #for i in range(numVectors):
    #    random_vectors.append([random.uniform(random_low_number, random_high_number), random.uniform(random_low_number, random_high_number)])

    return random_vectors


def generate_steps_graph(vectors, clusters_vector, step, random_low_number, random_high_number):

    # get x and y values to generate the graph
    x_values = [ vector[0] for vector in vectors[0] ]
    y_values = [ vector[1] for vector in vectors[0] ]

    # output to static HTML file
    output_file(f"step_{step}_graph.html")

    # create a new plot with a title and axis labels
    p = figure(plot_width=400, plot_height=400, x_range = (random_low_number-1, random_high_number+1), y_range = (random_low_number-1, random_high_number+1))

    if step == 0:
        
        # add a circle renderer with a size, color, and alpha
        p.scatter(x_values, y_values, size=SIZE_VECTOR, color='black', alpha=0.5)
    else:

        values_colors = [ POINTS_COLOURS[num_cluster] for num_cluster in vectors[1] ]

        for index_cluster, cluster_vector in enumerate(clusters_vector):
            x_values.append(cluster_vector[0])
            y_values.append(cluster_vector[1])
            values_colors.append(CLUSTERS_COLOURS[index_cluster])

        # add a circle renderer with a size, color, and alpha
        p.scatter(x_values, y_values, size=SIZE_VECTOR, color=values_colors, alpha=0.5)

    # show the results
    show(p)


def clustering_vectors(vectors, clusters_vector):

    clustered_vectors = []
    
    for vector in vectors[0]:
        
        cluster_distance = {
            'min_cluster_distance': -1,
            'index_min_cluster_distance': -1
        }

        for cluster_vestor_index, cluster_vector in enumerate(clusters_vector):

            if cluster_distance['min_cluster_distance'] == -1:
                cluster_distance['min_cluster_distance'] = get_distance_cluster(vector, cluster_vector)
                cluster_distance['index_min_cluster_distance'] = cluster_vestor_index
            else:
                if get_distance_cluster(vector, cluster_vector) < cluster_distance['min_cluster_distance']:
                    cluster_distance['min_cluster_distance'] = get_distance_cluster(vector, cluster_vector)
                    cluster_distance['index_min_cluster_distance'] = cluster_vestor_index

        clustered_vectors.append(cluster_distance['index_min_cluster_distance'])

    return clustered_vectors


def get_distance_cluster(vector, cluster):
    return math.sqrt( (cluster[0] - vector[0])**2 + (cluster[1] - vector[1])**2 )   # raíz( (x2 - x1)**2 + (y2 - y1)**2 )


def calculate_new_clusters_vector(vectors, clusters_vector):

    new_clusters_vector = [] 

    for index_cluster, cluster in enumerate(clusters_vector):

        cluster_vectors = []

        # extract the vectors of that cluster
        for index_vector, vector in enumerate(vectors[0]):
            
            # print(f'{index_cluster} -> {vectors[1][index_vector]}')
            # making a vectors list with the same cluster
            if index_cluster == vectors[1][index_vector]:
                cluster_vectors.append(vector)

        x_cluster_vector = [float(cluster_vector[0]) for cluster_vector in cluster_vectors]
        y_cluster_vector = [float(cluster_vector[1]) for cluster_vector in cluster_vectors]

        if len(cluster_vectors) == 0:
            # calculate the average of vectors in that cluster to get his new coord
            new_cluster_x_coord = random.uniform(1, 10)
            new_cluster_y_coord = random.uniform(1, 10)
            print('random')
        else:
            # calculate the average of vectors in that cluster to get his new coord
            new_cluster_x_coord = sum(x_cluster_vector) / len(cluster_vectors)
            new_cluster_y_coord = sum(y_cluster_vector) / len(cluster_vectors)

        new_clusters_vector.append([new_cluster_x_coord, new_cluster_y_coord])

    return new_clusters_vector


if __name__ == "__main__":
    
    random_vectors = []

    # generate the random vectors
    random_vectors.append(generate_random_vector(NUM_VECTORS, MIN_LIMIT_POINTS, MAX_LIMIT_POINTS))

    # generate the initial plot
    generate_steps_graph(random_vectors, None, 0, MIN_LIMIT_POINTS, MAX_LIMIT_POINTS)

    # generate the clusters for comparing which one is closer to the vectors than the others
    clusters_vector = generate_random_vector(NUM_CLUSTERS, MIN_LIMIT_POINTS, MAX_LIMIT_POINTS)

    # asociate the vector to the closest cluster
    clustered_vectors = clustering_vectors(random_vectors, clusters_vector)

    # set the vector-cluster
    random_vectors.append(clustered_vectors)

    # generate the plot
    generate_steps_graph(random_vectors, clusters_vector, 1, MIN_LIMIT_POINTS, MAX_LIMIT_POINTS)

    for i in range(2, 10):

        # comparing if the centroide is the same for every cluster
        if clusters_vector != calculate_new_clusters_vector(random_vectors, clusters_vector):

            # generate the clusters for comparing which cluster is closer to the vectors
            clusters_vector = calculate_new_clusters_vector(random_vectors, clusters_vector)
        
            # asociate the vector to the closest cluster
            clustered_vectors = clustering_vectors(random_vectors, clusters_vector)

            # set the vector-cluster
            random_vectors[1] = clustered_vectors
        
            # generate the plot
            generate_steps_graph(random_vectors, clusters_vector, i, MIN_LIMIT_POINTS, MAX_LIMIT_POINTS)

        else:
            break