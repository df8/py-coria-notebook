from coria_lib.coria_aspl_eccentricity import average_shortest_path_length, eccentricity, graph_diameter
from coria_lib.coria_betweenness_centrality import betweenness_centrality, edge_betweenness_centrality
from coria_lib.coria_clustering_coefficient import local_clustering_coefficient_corrected, local_clustering_coefficient_default
from coria_lib.coria_layout_position import circular_layout, spring_layout, shell_layout, random_layout, spectral_layout
from coria_lib.coria_node_degree import node_degree, average_node_degree
from coria_lib.coria_normalise import normalise_min_max, normalise_max_min
from coria_lib.coria_average_neighbour_degree import average_neighbour_degree_default, average_neighbour_degree_corrected, iterated_average_neighbour_degree_default, iterated_average_neighbour_degree_corrected
from coria_lib.coria_risk_score import unified_risk_score, connectivity_risk_classification
from coria_lib.coria_shortest_path import shortest_path_length

#
# This tree covers the following logical layers, where a parent can have multiple children
#
# Metric Algorithm {}
#     Metric Algorithm Variant {}
#         Dependencies [] # List of Metric Algorithm Variants
#         Metric Algorithm Implementation {}
#

CORIA_METRIC_TREE = {
    'node-degree': {
        'node-degree-default': {
            'cpu': node_degree,
            'gpu': node_degree
        },
        'node-degree-normalized': {
            'cpu': normalise_min_max,
            'gpu': normalise_min_max
        }
    },
    'shortest-path-lengths': {
        'shortest-path-lengths-default': {
            'cpu': shortest_path_length,
            'gpu': shortest_path_length
        }
    },
    'average-shortest-path-length': {
        'average-shortest-path-length-default': {
            'cpu': average_shortest_path_length,
            'gpu': average_shortest_path_length
        },
        'average-shortest-path-length-normalized': {
            'cpu': normalise_max_min,
            'gpu': normalise_max_min
        }
    },
    'eccentricity': {
        'eccentricity-default': {
            'cpu': eccentricity,
            'gpu': eccentricity

        },
        'eccentricity-normalized': {
            'cpu': normalise_max_min,
            'gpu': normalise_max_min
        }
    },
    'betweenness-centrality': {
        'betweenness-centrality-default': {
            'cpu': betweenness_centrality,
            'gpu': betweenness_centrality
        },
        'betweenness-centrality-normalized': {
            'cpu': normalise_min_max,
            'gpu': normalise_min_max
        }
    },
    'average-neighbour-degree': {
        'average-neighbour-degree-default': {
            'cpu': average_neighbour_degree_default,
            'gpu': average_neighbour_degree_default
        },
        'average-neighbour-degree-corrected': {
            'cpu': average_neighbour_degree_corrected,
            'gpu': average_neighbour_degree_corrected

        },
        'average-neighbour-degree-corrected-and-normalized': {
            'cpu': normalise_min_max,
            'gpu': normalise_min_max
        }
    },
    'iterated-average-neighbour-degree': {
        'iterated-average-neighbour-degree-default': {
            'cpu': iterated_average_neighbour_degree_default,
            'gpu': iterated_average_neighbour_degree_default
        }
        ,
        'iterated-average-neighbour-degree-corrected': {
            'cpu': iterated_average_neighbour_degree_corrected,
            'gpu': iterated_average_neighbour_degree_corrected
        },
        'iterated-average-neighbour-degree-corrected-and-normalized': {
            'cpu': normalise_min_max,
            'gpu': normalise_min_max
        }
    },
    'local-clustering-coefficients': {
        'local-clustering-coefficients-default': {
            'cpu': local_clustering_coefficient_default,
            'gpu': local_clustering_coefficient_default
        },
        'local-clustering-coefficients-corrected': {
            'cpu': local_clustering_coefficient_corrected,
            'gpu': local_clustering_coefficient_corrected
        },
        'local-clustering-coefficients-corrected-and-normalized': {
            'cpu': normalise_min_max,
            'gpu': normalise_min_max
        }
    },
    'unified-risk-score': {
        'unified-risk-score-default': {
            'cpu': unified_risk_score,
            'gpu': unified_risk_score
        }
    },
    'connectivity-risk-classification': {
        'connectivity-risk-classification-default': {
            'cpu': connectivity_risk_classification,
            'gpu': connectivity_risk_classification
        }
    },
    'average-node-degree': {
        'average-node-degree-default': {
            'cpu': average_node_degree,
            'gpu': average_node_degree
        }
    },
    'graph-diameter': {
        'graph-diameter-default': {
            'cpu': graph_diameter
        }
    },
    'layout-position-circular': {
        'layout-position-circular-default': {
            'cpu': circular_layout
        }
    },
    'layout-position-spring': {
        'layout-position-spring-default': {
            'cpu': spring_layout
        }
    },
    'layout-position-spectral': {
        'layout-position-spectral-default': {
            'cpu': spectral_layout
        }
    },
    'layout-position-random': {
        'layout-position-random-default': {
            'cpu': random_layout
        }
    },
    'layout-position-shell': {
        'layout-position-shell-default': {
            'cpu': shell_layout
        }
    },
    'edge-betweenness-centrality': {
        'edge-betweenness-centrality-default': {
            'cpu': edge_betweenness_centrality,
            'gpu': edge_betweenness_centrality
        }
    }
}

CORIA_METRIC_DEPENDENCIES = {
    'node-degree-default': [],
    'node-degree-normalized': ['node-degree-default'],
    'shortest-path-lengths-default': [],
    'average-shortest-path-length-default': ['shortest-path-lengths-default'],
    'average-shortest-path-length-normalized': ['average-shortest-path-length-default'],
    'eccentricity-default': ['shortest-path-lengths-default'],
    'eccentricity-normalized': ['eccentricity-default'],
    'betweenness-centrality-default': [],
    'betweenness-centrality-normalized': ['betweenness-centrality-default'],
    'average-neighbour-degree-default': ['node-degree-default'],
    'average-neighbour-degree-corrected': ['node-degree-default'],
    'average-neighbour-degree-corrected-and-normalized': ['average-neighbour-degree-corrected'],
    'iterated-average-neighbour-degree-default': ['node-degree-default', 'shortest-path-lengths-default'],
    'iterated-average-neighbour-degree-corrected': ['node-degree-default', 'shortest-path-lengths-default'],
    'iterated-average-neighbour-degree-corrected-and-normalized': ['iterated-average-neighbour-degree-corrected'],
    'local-clustering-coefficients-default': [],
    'local-clustering-coefficients-corrected': ['local-clustering-coefficients-default'],
    'local-clustering-coefficients-corrected-and-normalized': ['local-clustering-coefficients-corrected'],
    'unified-risk-score-default': [
        'node-degree-normalized',
        'average-neighbour-degree-corrected-and-normalized',
        'iterated-average-neighbour-degree-corrected-and-normalized',
        'betweenness-centrality-normalized',
        'eccentricity-normalized',
        'average-shortest-path-length-normalized'
    ],
    'connectivity-risk-classification-default': ['unified-risk-score-default'],
    'average-node-degree-default': [],
    'graph-diameter-default': [],
    'layout-position-circular-default': [],
    'layout-position-spring-default': [],
    'layout-position-spectral-default': [],
    'layout-position-random-default': [],
    'layout-position-shell-default': [],
    'edge-betweenness-centrality-default': [],
}
