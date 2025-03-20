import tomllib
from CanvasAPIWrapper import CanvasAPI
from CanvasBatchManager import *

# Example usage
if __name__ == "__main__":
    # Configuration

    # Open and parse a TOML file
    with open("config.toml", "rb") as f:  # Note: must open in binary mode
        config = tomllib.load(f)

    base_url = config["canvas"]["base_url"]
    api_token = config["canvas"]["api_token"]
    course_id = config["canvas"]["courses"]["course_id"]
    
    # Create a CanvasAPI object
    cw = CanvasAPI(base_url, api_token)
    # print(cw.get_courses(), "\n", "-"*20)
    # print(cw.get_course_assignments(course_id), "\n", "-"*20)
    # for assignment in cw.get_course_assignments(course_id):
    #     print(assignment["name"], assignment["id"])
    # print("\n", "-"*20)
    # print(cw.get_users(course_id), "\n", "-"*20)
    # print(cw.get_assignment_submissions(course_id, cw.get_course_assignments(course_id)[0]["id"]), "\n", "-"*20)

    template_path = CanvasBatchManager.generate_grading_template_file(cw.get_course_assignments(course_id)[0], "output")
    cbm = CanvasBatchManager(base_url, api_token)
    cbm.generate_submission_grading_files(template_path, "output")

    for item in cw.get_course_assignments(course_id):
        for key, value in item.items():
            print(key, value)
        print("--------------------")