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
            'dependencies': [],
            'implementations': {
                'cpu': node_degree,
                'gpu': node_degree
            }
        },
        'node-degree-normalized': {
            'dependencies': ['node-degree-default'],
            'implementations': {
                'cpu': normalise_min_max,
                'gpu': normalise_min_max
            }
        }
    },
    'shortest-path-lengths': {
        'shortest-path-lengths-default': {
            'dependencies': [],
            'implementations': {
                'cpu': shortest_path_length,
                'gpu': shortest_path_length
            }
        }
    },
    'average-shortest-path-length': {
        'average-shortest-path-length-default': {
            'dependencies': ['shortest-path-lengths-default'],
            'implementations': {
                'cpu': average_shortest_path_length,
                'gpu': average_shortest_path_length
            }
        },
        'average-shortest-path-length-normalized': {
            'dependencies': ['average-shortest-path-length-default'],
            'implementations': {
                'cpu': normalise_max_min,
                'gpu': normalise_max_min
            }
        }
    },
    'eccentricity': {
        'eccentricity-default': {
            'dependencies': ['shortest-path-lengths-default'],
            'implementations': {
                'cpu': eccentricity,
                'gpu': eccentricity
            }
        },
        'eccentricity-normalized': {
            'dependencies': ['eccentricity-default'],
            'implementations': {
                'cpu': normalise_max_min,
                'gpu': normalise_max_min
            }
        }
    },

    'betweenness-centrality': {
        'betweenness-centrality-default': {
            'dependencies': [],
            'implementations': {
                'cpu': betweenness_centrality,
                'gpu': betweenness_centrality
            }
        },
        'betweenness-centrality-normalized': {
            'dependencies': ['betweenness-centrality-default'],
            'implementations': {
                'cpu': normalise_min_max,
                'gpu': normalise_min_max
            }
        }
    },
    'average-neighbour-degree': {
        'average-neighbour-degree-default': {
            'dependencies': [],
            'implementations': {
                'cpu': average_neighbour_degree_default,
                'gpu': average_neighbour_degree_default
            }
        },
        'average-neighbour-degree-corrected': {
            'dependencies': [],
            'implementations': {
                'cpu': average_neighbour_degree_corrected,
                'gpu': average_neighbour_degree_corrected
            }
        },
        'average-neighbour-degree-corrected-and-normalized': {
            'dependencies': ['average-neighbour-degree-corrected'],
            'implementations': {
                'cpu': normalise_min_max,
                'gpu': normalise_min_max
            }
        }
    },
    'iterated-average-neighbour-degree': {
        'iterated-average-neighbour-degree-default': {
            'dependencies': ['shortest-path-lengths-default'],
            'implementations': {
                'cpu': iterated_average_neighbour_degree_default,
                'gpu': iterated_average_neighbour_degree_default
            }
        },
        'iterated-average-neighbour-degree-corrected': {
            'dependencies': ['shortest-path-lengths-default'],
            'implementations': {
                'cpu': iterated_average_neighbour_degree_corrected,
                'gpu': iterated_average_neighbour_degree_corrected
            }
        },
        'iterated-average-neighbour-degree-corrected-and-normalized': {
            'dependencies': ['iterated-average-neighbour-degree-corrected'],
            'implementations': {
                'cpu': normalise_min_max,
                'gpu': normalise_min_max
            }
        }
    },
    'local-clustering-coefficients': {
        'local-clustering-coefficients-default': {
            'dependencies': [],
            'implementations': {
                'cpu': local_clustering_coefficient_default,
                'gpu': local_clustering_coefficient_default
            }
        },
        'local-clustering-coefficients-corrected': {
            'dependencies': ['local-clustering-coefficients-default'],
            'implementations': {
                'cpu': local_clustering_coefficient_corrected,
                'gpu': local_clustering_coefficient_corrected
            }
        },
        'local-clustering-coefficients-corrected-and-normalized': {
            'dependencies': ['local-clustering-coefficients-corrected'],
            'implementations': {
                'cpu': normalise_min_max,
                'gpu': normalise_min_max
            }
        }
    },
    'unified-risk-score': {
        'unified-risk-score-default': {
            'dependencies': [
                'node-degree-normalized',
                'average-neighbour-degree-corrected-and-normalized',
                'iterated-average-neighbour-degree-corrected-and-normalized',
                'betweenness-centrality-normalized',
                'eccentricity-normalized',
                'average-shortest-path-length-normalized'
            ],
            'implementations': {
                'cpu': unified_risk_score,
                'gpu': unified_risk_score
            }
        }
    },
    'connectivity-risk-classification': {
        'connectivity-risk-classification-default': {
            'dependencies': ['unified-risk-score-default'],
            'implementations': {
                'cpu': connectivity_risk_classification,
                'gpu': connectivity_risk_classification
            }
        }
    },
    'average-node-degree': {
        'average-node-degree-default': {
            'dependencies': [],
            'implementations': {
                'cpu': average_node_degree,
                'gpu': average_node_degree
            }
        }
    },
    'graph-diameter': {
        'graph-diameter-default': {
            'dependencies': [],
            'implementations': {
                'cpu': graph_diameter
            }
        }
    },
    'layout-position-circular': {
        'layout-position-circular-default': {
            'dependencies': [],
            'implementations': {
                'cpu': circular_layout
            }
        }
    },
    'layout-position-spring': {
        'layout-position-spring-default': {
            'dependencies': [],
            'implementations': {
                'cpu': spring_layout
            }
        }
    },
    'layout-position-spectral': {
        'layout-position-spectral-default': {
            'dependencies': [],
            'implementations': {
                'cpu': spectral_layout
            }
        }
    },
    'layout-position-random': {
        'layout-position-random-default': {
            'dependencies': [],
            'implementations': {
                'cpu': random_layout
            }
        }
    },
    'layout-position-shell': {
        'layout-position-shell-default': {
            'dependencies': [],
            'implementations': {
                'cpu': shell_layout
            }
        }
    },
    'edge-betweenness-centrality': {
        'edge-betweenness-centrality-default': {
            'dependencies': [],
            'implementations': {
                'cpu': edge_betweenness_centrality,
                'gpu': edge_betweenness_centrality
            }
        }
    }
}
