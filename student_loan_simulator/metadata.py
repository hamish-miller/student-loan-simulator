"""
Functions for creating/saving metadata with the results.
"""

import datetime
import json
import os

OUTPUT_FILE = "metadata.json"

def save_metadata(output_dir):
    metadata = {}

    _add_date_and_time(metadata)

    output_path = os.path.join(output_dir, OUTPUT_FILE)

    with open(output_path, 'w') as f:
        json.dump(metadata, f)


def _add_date_and_time(metadata):
    now = datetime.datetime.now()

    metadata["date"] = now.strftime("%Y-%m-%d")
    metadata["time"] = now.strftime("%H-%M-%S")
