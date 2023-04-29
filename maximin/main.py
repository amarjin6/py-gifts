import sys
import matplotlib.pyplot as plt
from random import randint
from typing import List, Any

from point import Point
from cluster import Cluster

MAX_AXIS_VALUE = 100
POINT_COUNT = 20000


def remove_points_from_clusters(clusters: List[Cluster]) -> None:
    """
    Remove points from cluster
    :param clusters: List of clusters e.g. Cluster C(center=Point A, points=[Point A, Point B, Point C])
    :return: None
    """
    for cluster in clusters:
        cluster.points = []


def assign_points_to_cluster(points: List[Point], clusters: List[Cluster]) -> None:
    """
    Assign points to the nearest cluster
    :param points: List of points on the plot e.g. Point A(x=100, y=100)
    :param clusters: List of clusters e.g. Cluster C(center=Point A, points=[Point A, Point B, Point C])
    :return: None
    """
    for point in points:
        min_distance = sys.maxsize
        cluster_index = -1
        for i in range(len(clusters)):
            dist = point.calc_distance(clusters[i].center)
            if dist < min_distance:
                min_distance = dist
                cluster_index = i

        point.cluster_index = cluster_index
        clusters[cluster_index].points.append(point)


def find_max_distance(clusters: List[Cluster]) -> tuple[int | Any, int | Any]:
    """
    Find max distant point from cluster centers
    :param clusters: List of clusters e.g. Cluster C(center=Point A, points=[Point A, Point B, Point C])
    :return: Point on the plot e.g. Point A(x=100, y=100) with max distance
    """
    max_dist = 0
    point = 0
    for cluster in clusters:
        max_cluster_dist = 0
        cluster_point = cluster.center
        for cp in cluster.points:
            dist = cp.calc_distance(cluster.center)
            if dist > max_cluster_dist:
                max_cluster_dist = dist
                cluster_point = cp

        if max_cluster_dist > max_dist:
            max_dist = max_cluster_dist
            point = cluster_point

    return point, max_dist


def get_mean_distance(clusters: List[Cluster]) -> int:
    """
    Calculate mean distance between cluster centers
    :param clusters: List of clusters e.g. Cluster C(center=Point A, points=[Point A, Point B, Point C])
    :return: Mean of cluster's distances
    """
    distances = []
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            dist = clusters[i].center.calc_distance(clusters[j].center)
            distances.append(dist)

    return sum(distances) / len(distances)


def add_cluster_points_to_plot(cluster_points: List[Point]) -> None:
    """
    Displays cluster points on the plot
    :param cluster_points: List of points on the plot e.g. Point A(x=100, y=100)
    :return: None
    """
    x_coordinates = [p.x for p in cluster_points]
    y_coordinates = [p.y for p in cluster_points]
    plt.scatter(x_coordinates, y_coordinates)


def display_all_clusters(clusters: List[Cluster]) -> None:
    """
    Displays on the plot all clusters with centers
    :param clusters: List of clusters e.g. Cluster C(center=Point A, points=[Point A, Point B, Point C])
    :return: None
    """
    cluster_center_points = []
    for cluster in clusters:
        cluster_center_points.append(cluster.center)
        add_cluster_points_to_plot(cluster.points)

    add_cluster_points_to_plot(cluster_center_points)
    plt.show()


def initialize_cluster(points: List[Point]) -> List[Cluster]:
    """
    Initialize List of clusters with 2 entities
    :param points: List of points on the plot e.g. Point A(x=100, y=100)
    :return: List of clusters e.g. Cluster C(center=Point A, points=[Point A, Point B, Point C])
    """
    clusters = [Cluster(points[randint(0, POINT_COUNT)])]

    max_dist = 0
    point = points[0]
    for p in points:
        dist = p.calc_distance(clusters[0].center)
        if dist > max_dist:
            max_dist = dist
            point = p

    clusters.append(Cluster(point))

    return clusters


def maximin(points: List[Point]) -> None:
    """
    Implementation of MaxiMin self-learning algorithm
    :param points: A List of points on the plot e.g. Point A(x=100, y=100)
    :return: None
    """
    clusters = initialize_cluster(points)
    is_new_cluster = True

    while is_new_cluster:
        is_new_cluster = False
        remove_points_from_clusters(clusters)
        assign_points_to_cluster(points, clusters)
        point, max_dist = find_max_distance(clusters)

        if max_dist > 0.5 * get_mean_distance(clusters):
            clusters.append(Cluster(point))
            is_new_cluster = True

    display_all_clusters(clusters)


if __name__ == '__main__':
    target_points = [Point(randint(0, MAX_AXIS_VALUE), randint(0, MAX_AXIS_VALUE)) for _ in range(POINT_COUNT)]
    maximin(target_points)
