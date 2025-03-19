import os
import yaml
from CanvasAPIWrapper import CanvasAPI

class CanvasBatchManager:
    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.api_token = api_token
        self.headers = { "Authorization": f"Bearer {api_token}" }

        self.CanvasAPI = CanvasAPI(base_url, api_token)

    @staticmethod
    def generate_assignment_template_file(assignment, output_path):
        """
        Generates a template file for an assignment.

        args:
            assignment (dict): The assignment object
            output_path: The path to save the template file

        ret:
            str: The path to the template file
        """
        # Build the yaml template file object
        template = {
            "assignment_name": assignment["name"],
            "assignment_id": assignment["id"],
            "course_id": assignment["course_id"],
            "rubric": [
                {
                    "description": "Criteria 1",
                    "points": 10,
                    "extra_credit": False # optional field
                },
                {
                    "description": "Criteria 2",
                    "points": 10
                }
            ],
            "late_policy": { # optional field
                "deduction": 10, # 10% of the obtained grade (e.g. 10% of 36/40 = 32.4/40) or flat decrease, min 0
                "deduction_type": 'flat', # flat, percentage
                "granularity": 'ceil', # truncate, round, ceil, floor
                "deduction_interval": "hour", # hour, day
                "min_interval": 0,
                "max_interval": 72,
            },
            "notes": [ # optional field
                "Note 1",
                "Note 2"
            ],
            "end_note": "End Note" # optional field
        }

        # Create the yaml template file
        with open(output_path, "w") as f:
            yaml.dump(template, f, default_flow_style=False, sort_keys=False)
