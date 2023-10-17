# get_course

The aim of this package is to download a complete course from the Climate Compatible Curriculum
in the format required so as to easily use the [SCORM package](https://github.com/ClimateCompatibleGrowth/scorm_package)
to bundle the material ready for upload to the OpenLearnCreate Moodle instance.

The Climate Compatible Curriculum has an open read-only API available at ``https://teachingkit.climatecompatiblegrowth.com/api``

There are endpoints for blocks, lectures and courses:

    api/blocks/{id}
    api/lectures/{id}
    api/courses/{id}

Use the query parameter `?populate=*` to also download relations. For example, the lectures contained within a course.

To obtain lecture 4 for the English locate, you run the following query:

    https://teachingkit.climatecompatiblegrowth.com/api/lectures/4?locale=en&populate=*

This package uses the requests libary to retrieve the information. We can then parse the JSON payload as a Python dictionary,
and write out the information to markdown files in the required folder structure.

The structure needed is shown in the [Infrastructure Resilience course](https://github.com/ClimateCompatibleGrowth/nismod_teaching_kit)

## User Interface Design

The user should type `python get_course.py <html/scorm/markdown> <id> <destination_folder>`, selecting the id of the course and the destination folder
and the format to convert the material to.

## Remaining development

- [ ] Only return blocks and lectures which are published, and the latest version (normally only the latest version is published, but not necessarily).
  Currently the relations store all blocks, including earlier versions of the same block, that are included in a lecture.
  The same for lectures and courses.
- [ ] We need to re-do the embedding of images in the markdown documents. Images are stored in the media library, but are then uploaded to an amazon server, so these can be downloaded from the urls embedded in the document and then redirected to a local location.
