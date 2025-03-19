import requests

class CanvasBatchGrader:
    """
    Handles batch grading operations for Canvas LMS.
    """

    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.api_token = api_token
        self.headers = { "Authorization": f"Bearer {api_token}" }

    def get_courses(self):
        """
        Retrieve a list of courses from Canvas LMS.

        ret:
            list: List of course objects
        """
        endpoint = f"{self.base_url}/api/v1/courses"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_course_assignments(self, course_id):
        """
        Gets all assignments within a course.

        args:
            course_id (int, str): The ID of the course to get assignments for

        ret: 
            list: List of assignment objects
        """
        endpoint = f"{self.base_url}/api/v1/courses/{course_id}/assignments"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_users(self, course_id):
        """
        Gets all users within a course.

        args:
            course_id (int, str): The ID of the course to get users for

        ret: 
            list: List of user objects
        """
        endpoint = f"{self.base_url}/api/v1/courses/{course_id}/users"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()