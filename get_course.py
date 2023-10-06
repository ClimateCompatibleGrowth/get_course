"""Get a course from the Climate Compatible Curriculum

Writes a markdown file with the contents of the course to the current directory

>>> python get_course.py


"""
import requests
from typing import Dict, Union, Any

from get_lecture import get_lecture
from get_block import get_lecture_block


def get_course(id: str):
    """Retrieves the contents of a course from the teaching kit website

    Arguments
    ---------
        id (str): The id of the course to retrieve
    """
    url = f"https://teachingkit.climatecompatiblegrowth.com/api/courses/{id}"
    payload = {'locale': 'en', 'populate': '*'}
    response = requests.get(url, params=payload)

    return response.json()


def print_keys(dict: Union[Dict, Any]):
    if isinstance(dict, Dict):
        for key in dict.keys():
            print(key)
            print_keys(dict[key])
    else:
        pass


if __name__ == "__main__":

    course = get_course(2)
    attributes = course['data']['attributes']
    print(f"Attributes: {attributes.keys()}")

    title = attributes['Title']
    print(f"Course title: {title}")
    

    outcomes = [x['LearningOutcome'] for x in attributes['LearningOutcomes']]
    print(f"Outcomes: {outcomes}")

    lectures = attributes['Lectures']['data']
    for lecture in lectures:
        print(f"This course contains lecture: '{lecture['id']}: {lecture['attributes']['Title']}'")


