"""Get a lecture block from the Climate Compatible Curriculum

Writes a markdown file with the contents of the lecture block to the current directory

>>> python get_block.py

"""
import requests
from typing import Dict, Union, Any
from json import loads, dumps

def get_lecture_block(id: str):
    """Retrieves the contents of a lecture block from the teaching kit website

    Arguments
    ---------
        id (str): The id of the lecture block to retrieve
    """
    url = f"https://teachingkit.climatecompatiblegrowth.com/api/blocks/{id}"
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
    block = get_lecture_block(5)
    attributes = block['data']['attributes']

    print(f"Attributes: {attributes.keys()}")

    print(f"Version number: {attributes['versionNumber']}")
    print(f"Version: {[x['id'] for x in attributes['versions']['data']]}")

    print(f"Published at: {attributes['publishedAt']}")

    lectures = [x['attributes'] for x in attributes['Lectures']['data']]
    for lecture in lectures:
        print(f"This block is part of lecture '{lecture['Title']}'")

    authors = [x['attributes'] for x in attributes['Authors']['data']]

    print("This lecture block was written by:")
    for author in authors:
        print(f"{author['FirstName']} {author['LastName']} {author['Email']} {author['ORCID']}")

    keywords = [x['attributes'] for x in attributes['Keywords']['data']]

    print(f"Keywords: {keywords}")

    slides = attributes['Slides']
    print(f"There are {len(slides)} slides in this lecture block. The slides have titles:")
    for slide in slides:
        print(f"  {slide['Title']}")

    title = attributes['Title']
    print(title)

    block_id = block['data']['id']
    document = attributes['Document']
    with open(f"lecture_block_{block_id}.md", 'w') as markdown_file:
        markdown_file.write(document)

