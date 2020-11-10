import sys
from time import time_ns

if __name__ == "__main__":
    from coria_lib.coria_config import set_global_settings, coria_imports
    from coria_lib.coria_parse_args import create_args_parser

    options = create_args_parser().parse_args()

    set_global_settings(use_cuda=options.metric[0].endswith("python3-c-cuda--rapids-cugraph"))

    # CORIA components
    coria_imports()

    from coria_lib.coria_dependencies import CORIA_METRIC_TREE
    from coria_lib.coria_helper_functions import log
    from coria_lib.coria_parse_args import parse_input_args
    from coria_lib.coria_results import set_input_dataframe_dict

    set_input_dataframe_dict(parse_input_args(options))

    from coria_lib.coria_parse_args import output_paths
    from coria_lib.coria_results import nmr_column_list_contains, input_dataframe_dict, metric_execution_timestamps, write_output_to_files


    def parse_coria_metric_id(_metric_id):
        parts = _metric_id.split('--', 1)
        indices = [parts[0].rfind('-default'), parts[0].rfind('-corrected-and-normalized'), parts[0].rfind('-corrected'), parts[0].rfind('-normalized')]
        split_index = next(v for i, v in enumerate(indices) if v > -1)  # get the index of the first matching suffix
        return {
            'metric_algorithm': parts[0][0: split_index],
            'metric_variant': parts[0],
            'architecture': 'gpu' if parts[1] == 'python3-c-cuda--rapids-cugraph' else 'cpu'
        }


    def get_spl_dependent_metrics():
        """
Checks all metrics in the computation queue that depend on shortest-path-lengths.
        """
        _spl_dependent_metrics = []
        for _metric_id in options.metric:
            _metric_keys = parse_coria_metric_id(_metric_id)
            if _metric_keys['metric_algorithm'] in CORIA_METRIC_TREE and \
                    _metric_keys['metric_variant'] in CORIA_METRIC_TREE[_metric_keys['metric_algorithm']] and \
                    'shortest-path-lengths-default' in CORIA_METRIC_TREE[_metric_keys['metric_algorithm']][_metric_keys['metric_variant']]['dependencies']:
                _spl_dependent_metrics.append(_metric_keys['metric_variant'])
        return _spl_dependent_metrics


    for metric_id in options.metric:
        metric_keys = parse_coria_metric_id(metric_id)

        if nmr_column_list_contains(metric_keys['metric_variant']):
            log("Skipped execution of " + metric_id + ': Metric has been computed already')

        else:
            log("Starting execution of " + metric_id)
            tstamp_start = time_ns()
            if metric_keys['metric_algorithm'] in CORIA_METRIC_TREE and \
                    metric_keys['metric_variant'] in CORIA_METRIC_TREE[metric_keys['metric_algorithm']] and \
                    metric_keys['architecture'] in CORIA_METRIC_TREE[metric_keys['metric_algorithm']][metric_keys['metric_variant']]['implementations']:

                # CORIA_METRIC_TREE is essentially a dict with function references at its leaves, therefore we can call the function using its reference
                metric_function = CORIA_METRIC_TREE[metric_keys['metric_algorithm']][metric_keys['metric_variant']]['implementations'][metric_keys['architecture']]

                if metric_keys['metric_algorithm'] == "shortest-path-lengths":
                    # Compute only the metrics that were requested through command line parameters to save some execution time.
                    spl_table_requested_for_export = 'shortestpathlength' in output_paths
                    metric_function(input_dataframe_dict, metric_keys['metric_variant'], spl_table_requested_for_export, get_spl_dependent_metrics())

                else:
                    metric_function = CORIA_METRIC_TREE[metric_keys['metric_algorithm']][metric_keys['metric_variant']]['implementations'][metric_keys['architecture']]
                    metric_function(input_dataframe_dict, metric_keys['metric_variant'])

            else:
                sys.exit('Unknown metric: ' + metric_id)

            metric_execution_timestamps[metric_keys['metric_variant']] = (round(tstamp_start / 1e6), round(time_ns() / 1e6))

    log("finished computing")
    write_output_to_files()
