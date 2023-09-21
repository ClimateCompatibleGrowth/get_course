"""Get a lecture from the Climate Compatible Curriculum

Writes a markdown file with the contents of the lecture to the current directory

>>> python get_lecture.py

"""
import requests
from typing import Dict, Union, Any


def get_lecture(id: str):
    """Retrieves the contents of a lecture from the teaching kit website

    Arguments
    ---------
        id (str): The id of the lecture block to retrieve
    """
    url = f"https://teachingkit.climatecompatiblegrowth.com/api/lectures/{id}"
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

    lecture = get_lecture(2)
    attributes = lecture['data']['attributes']

    print(f"Attributes: {attributes.keys()}")

    print(f"Version number: {attributes['versionNumber']}")
    print(f"Version: {attributes['versions']}")

    blocks = attributes['Blocks']['data']
    # print(blocks)
    for block in blocks:
        print(f"This lecture contains block {block['id']}: '{block['attributes']['Title']}'")

    authors = [x['attributes'] for x in attributes['LectureCreators']['data']]

    print("This lecture lecture was written by:")
    for author in authors:
        print(f"{author['FirstName']} {author['LastName']} {author['Email']} {author['ORCID']}")

    outcomes = [x['LearningOutcome'] for x in attributes['LearningOutcomes']]

    print(f"Outcomes: {outcomes}")

    title = attributes['Title']
    print(title)

    lecture_id = lecture['data']['id']
    document = attributes['Abstract']
    # with open(f"lecture_{lecture_id}.md", 'wt') as markdown_file:
    #     markdown_file.write(f"# {title}\n\n")
    #     markdown_file.write(document)

