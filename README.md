# tempest-plugin-demo

## About
This repository is part of a technical presentation ([slides](TODO)).
It contains quick overview of Tempest, python-tempestconf and describes steps
how to create a simple Tempest plugin.

## <Title>
Create a [structure](https://docs.openstack.org/tempest/latest/plugin.html#plugin-cookiecutter)
using [cookiecutter](https://github.com/openstack-dev/cookiecutter).
In this step I hit an issue where cookiecutter failed with a *JSON decoding error*.
I needed to edit 2 of the cookiecutter's source files, the full output and
diffs of the changes can be [seen here](https://github.com/kopecmartin/tempest-plugin-demo/blob/master/doc/LOGS/cookiecutter_debug.md).

A short output of cookiecutter:
```
(.venv)[master !][centos@mkopec-test tempest-plugin-demo]$ cookiecutter https://git.openstack.org/openstack-dev/cookiecutter.git
You've downloaded /home/centos/.cookiecutters/cookiecutter before. Is it okay to delete and re-download it? [yes]: no
Do you want to re-use the existing version? [yes]: yes
module_name [replace with the name of the python module]: tempest_tests
service [replace with the service it implements]: service
repo_group [openstack]:
repo_name [replace with the name for the git repo]: tempest-plugin-demo
Select bug_tracker:
1 - Launchpad
2 - Storyboard
Choose from 1, 2 [1]: 1
bug_project [replace with the name of the project on Launchpad or the ID from Storyboard]: TODO
project_short_description [OpenStack Boilerplate contains all the boilerplate you need to create an OpenStack package.]:
Initialized empty Git repository in /home/centos/tempest-plugin-demo/.git/
```
The full output can be [seen here](https://github.com/kopecmartin/tempest-plugin-demo/blob/master/doc/LOGS/cookiecutter_success.md)
