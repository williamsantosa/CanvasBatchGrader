import requests
import tomllib
from cbg import CanvasBatchGrader

# Example usage
if __name__ == "__main__":
    # Configuration

    # Open and parse a TOML file
    with open("config.toml", "rb") as f:  # Note: must open in binary mode
        config = tomllib.load(f)

    base_url = config["canvas"]["base_url"]
    api_token = config["canvas"]["api_token"]
    course_id = config["canvas"]["courses"]["course_id"]
    
    # Create a CanvasBatchGrader instance
    cbg = CanvasBatchGrader(base_url, api_token)
    print(cbg.get_courses(), "\n", "-"*20)
    print(cbg.get_course_assignments(course_id), "\n", "-"*20)
    print(cbg.get_users(course_id), "\n", "-"*20)

    # response = requests.get(
    #     "https://canvas.instructure.com/api/v1/courses",
    #     headers={"Authorization": f"Bearer {api_token}"}
    # )
    # response.raise_for_status()
    # print(response.json())

    # try:
    #     assignment_analytics = get_course_assignment_analytics(base_url, api_token, course_id)
    #     print(f"Successfully retrieved assignment analytics for coupipe {course_id}")
    #     print(assignment_analytics)
    # except requests.exceptions.HTTPError as err:
    #     print(f"HTTP Error: {err}")
    # except requests.exceptions.RequestException as err:
    #     print(f"Error making request: {err}")