#"""Writes out a course to the folder structure required for SCORM packaging.

#Writes #out a course to the folder structure required to make a SCORM package of the lectures.

    #lecture_01
        #assets/
        #lecture_1.1.md
        #lecture_1.2.md
        #lecture_1.3.md
        #lecture_1.4.md

#Calls the SCORM packaging script to create a SCORM package for each lecture.

#Also writes out all copy for easy (manual) upload to Moodle (note that ideally we could package all this material
#so that OU could automate the upload to Moodle).

#"""

from os.path import exists
from os import mkdir
from typing import Dict, Union, Any
import requests

from get_block import get_lecture_block
from get_course import get_course
from get_lecture import get_lecture


def extract_images(document: str, destination_folder: str):
    #"""Extract all images from a markdown document, document to assets subfolder and replace with local references

    #Iterates through each line in a markdown document.
    #Extracts all ![img](url) references, downloads the image and saves it to the assets.
    #Then replaces the original reference with a local reference.

    #Arguments
    #----------
        #document (str): The markdown document to extract #images from
    #"""
    for line in document.split('\n'):
        if line.startswith('!['):
            url = line.split('(')[1].split(')')[0]
            filename = url.split('/')[-1]
            print(f"Downloading {url} to {destination_folder}/{filename}")
            try:
                image = requests.get(url, allow_redirects=True)
                if image.status_code == 200:
                    document = document.replace(url, f"assets/{filename}")
                    with open(f"{destination_folder}/{filename}", 'wb') as f:
                        f.write(image.content)
                else:
                    print(f"Error downloading {url}")
            except Exception as e:
                print(f"Error downloading {url}: {e}")
    return document


def main(course_id: int, destination_folder: str) -> bool:

    success = True

    if not exists(destination_folder):
        mkdir(destination_folder)

    course = get_course(course_id)
    lecture_id: list = [x['id'] for x in course['data']['attributes']['Lectures']['data']]
    lectures = [get_lecture(x) for x in lecture_id]
    for lecture in lectures:
        lecture_path = f"{destination_folder}/lecture_{lecture['data']['id']}"
        assets_path = f"{lecture_path}/assets"

        if not exists(lecture_path):
            mkdir(lecture_path)
        if not exists(assets_path):
            mkdir(assets_path)

        blocks = [get_lecture_block(x['id']) for x in lecture['data']['attributes']['Blocks']['data']]
        for block in blocks:
            block_path = f"{lecture_path}/{block['data']['id']}"
            with open(f"{block_path}.md", 'w') as f:
                document = extract_images(block['data']['attributes']['Document'], assets_path)
                f.write(document)

    return success


if __name__ == "__main__":
    success = main(2, "course_2")
    print(success)