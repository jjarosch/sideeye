Default Configuration
=====================

::

  {
    "wide_format": true,
    "da1_fields": {
      "index": 0,
      "condition": 1,
      "number": 2,
      "time": -1,
      "fixation_start": 8
    },
    "region_fields": {
      "number": 0,
      "condition": 1,
      "boundaries_start": 3,
      "includes_y": false
    },
    "cutoffs": {
      "min": -1,
      "max": -1,
      "include_fixation": false,
      "include_saccades": false
    },
    "region_measures": {
      "skip": {
        "include": true,
        "cutoff": -1,
        "header": "skip"
      },
      "first_pass_regressions_out": {
        "include": true,
        "cutoff": -1,
        "header": "first_pass_regressions_out"
      },
      "first_pass_regressions_in": {
        "include": true,
        "cutoff": -1,
        "header": "first_pass_regressions_in"
      },
      "first_fixation_duration": {
        "include": true,
        "cutoff": -1,
        "header": "first_fixation_duration"
      },
      "single_fixation_duration": {
        "include": true,
        "cutoff": -1,
        "header": "single_fixation_duration"
      },
      "first_pass": {
        "include": true,
        "cutoff": -1,
        "header": "first_pass"
      },
      "go_past": {
        "include": true,
        "cutoff": -1,
        "header": "go_past"
      },
      "total_time": {
        "include": true,
        "cutoff": -1,
        "header": "total_time"
      },
      "right_bounded_time": {
        "include": true,
        "cutoff": -1,
        "header": "right_bounded_time"
      },
      "reread_time": {
        "include": true,
        "cutoff": -1,
        "header": "reread_time"
      },
      "second_pass": {
        "include": true,
        "cutoff": -1,
        "header": "second_pass"
      },
      "spillover_time": {
        "include": true,
        "cutoff": -1,
        "header": "spillover_time"
      },
      "refixation_time": {
        "include": true,
        "cutoff": -1,
        "header": "refixation_time"
      },
      "landing_position": {
        "include": true,
        "cutoff": -1,
        "header": "landing_position"
      },
      "launch_site": {
        "include": true,
        "cutoff": -1,
        "header": "launch_site"
      },
      "first_pass_fixation_count": {
        "include": true,
        "cutoff": -1,
        "header": "first_pass_fixation_count"
      },
      "go_back_time_region": {
        "include": true,
        "cutoff": -1,
        "header": "go_back_time_region"
      },
      "go_back_time_char": {
        "include": true,
        "cutoff": -1,
        "header": "go_back_time_char"
      }
    },
    "trial_measures": {
      "location_first_regression": {
        "include": true,
        "cutoff": -1,
        "header": "location_first_regression"
      },
      "latency_first_regression": {
        "include": true,
        "cutoff": -1,
        "header": "latency_first_regression"
      },
      "fixation_count": {
        "include": true,
        "cutoff": -1,
        "header": "fixation_count"
      },
      "percent_regressions": {
        "include": true,
        "cutoff": -1,
        "header": "percent_regressions"
      },
      "trial_total_time": {
        "include": true,
        "cutoff": -1,
        "header": "trial_total_time"
      },
      "average_forward_saccade": {
        "include": true,
        "cutoff": -1,
        "header": "average_forward_saccade"
      },
      "average_backward_saccade": {
        "include": true,
        "cutoff": -1,
        "header": "average_backward_saccade"
      }
    },
    "region_output": {
      "experiment_name": {
        "include": true,
        "header": "experiment_name"
      },
      "filename": {
        "include": false,
        "header": "filename"
      },
      "date": {
        "include": false,
        "header": "date"
      },
      "trial_id": {
        "include": true,
        "header": "trial_id"
      },
      "trial_total_time": {
        "include": true,
        "header": "trial_total_time"
      },
      "item_id": {
        "include": true,
        "header": "item_id"
      },
      "item_condition": {
        "include": true,
        "header": "item_condition"
      },
      "region_label": {
        "include": false,
        "header": "region_label"
      },
      "region_number": {
        "include": true,
        "header": "region_number"
      },
      "region_text": {
        "include": false,
        "header": "region_text"
      },
      "region_start": {
        "include": false,
        "header": "region_start"
      },
      "region_end": {
        "include": false,
        "header": "region_end"
      }
    },
    "trial_output": {
      "experiment_name": {
        "include": true,
        "header": "experiment_name"
      },
      "filename": {
        "include": false,
        "header": "filename"
      },
      "date": {
        "include": false,
        "header": "date"
      },
      "trial_id": {
        "include": true,
        "header": "trial_id"
      },
      "trial_total_time": {
        "include": true,
        "header": "trial_total_time"
      },
      "item_id": {
        "include": true,
        "header": "item_id"
      },
      "item_condition": {
        "include": true,
        "header": "item_condition"
      }
    },
    "terminal_output": 0
  }
