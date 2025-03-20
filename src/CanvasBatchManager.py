import os
import yaml
from CanvasAPIWrapper import CanvasAPI
from CanvasUtils import write_yaml

class CanvasBatchManager:
    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.api_token = api_token
        self.headers = { "Authorization": f"Bearer {api_token}" }

        self.CanvasAPI = CanvasAPI(base_url, api_token)

    @staticmethod
    def generate_grading_template_file(assignment, output_dir):
        """
        Generates a template file for an assignment.

        args:
            assignment (dict): The assignment object
            output_dir: The directory path to save the template file

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
        file_name = f"{assignment['name'].replace(' ', '_').lower()}_{assignment['id']}_template.yaml"
        output_path = os.path.join(output_dir, file_name)
        write_yaml(output_path, template)

        return output_path

    def generate_submission_grading_files(self, grading_template_file, output_dir):
        """
        Generates grading files for all submissions of an assignment.

        args:
            grading_template_file (str): The path to the grading template file
            output_dir (str): The directory path to save the grading files
        """
        # Load the grading template file
        with open(grading_template_file, "r") as f:
            grading_template = yaml.safe_load(f)

        # Get all submissions for the assignment
        submissions = self.CanvasAPI.get_assignment_submissions(grading_template["course_id"], grading_template["assignment_id"])
        
        # Get all users for a course
        users = self.CanvasAPI.get_users(grading_template["course_id"])

        # Create a user dictionary (id -> name)
        user_dict = {user["id"]: user["name"] for user in users}

        # Generate grading files for each submission
        for submission in submissions:
            # Build the grading file object
            grading = {
                "assignment_id": grading_template["assignment_id"],
                "course_id": grading_template["course_id"],
                "user_id": submission["user_id"],
                "user_name": user_dict.get(submission["user_id"], "Unknown"),
                "rubric": grading_template["rubric"],
                "late_policy": grading_template.get("late_policy", None),
                "notes": grading_template.get("notes", None),
                "end_note": grading_template.get("end_note", None)
            }

            # Create the grading file
            file_name = f"{grading['user_name'].replace(' ', '_').lower()}_{grading['user_id']}_grading_asgn{grading['assignment_id']}.yaml"
            output_path = os.path.join(output_dir, file_name)
            write_yaml(output_path, grading)