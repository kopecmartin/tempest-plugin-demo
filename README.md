# tempest-plugin-demo

## About
This repository is part of a technical presentation ([slides](TODO)).
It contains quick overview of Tempest, python-tempestconf and describes steps
how to create a simple Tempest plugin.

## A simple Tempest plugin

### Create a plugin structure
Create a [structure](https://docs.openstack.org/tempest/latest/plugin.html#plugin-cookiecutter)
using [cookiecutter](https://github.com/openstack-dev/cookiecutter).
In this step I hit an issue where cookiecutter failed with a `JSON decoding error`.
I needed to edit 2 of the cookiecutter's source files, the full output and
diffs of the changes can be
[seen here](https://github.com/kopecmartin/tempest-plugin-demo/blob/master/doc/LOGS/cookiecutter_debug.md).

A short output of cookiecutter:
```
# pip install cookiecutter
$ cookiecutter https://git.openstack.org/openstack-dev/cookiecutter.git
You've downloaded /home/centos/.cookiecutters/cookiecutter before. Is it okay to delete and re-download it? [yes]: no
Do you want to re-use the existing version? [yes]: yes
module_name [replace with the name of the python module]: my_tempest_tests
service [replace with the service it implements]: my_service
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
The full output of the cookiecutter can be
[seen here](https://github.com/kopecmartin/tempest-plugin-demo/blob/master/doc/LOGS/cookiecutter_success.md)


### Plugin Class
We need to create a plugin class, in order to provide tempest all required
information for running our plugin. To simplify this, tempest provides an
abstract class that should be used as the parent for our plugin.

Let's create a `my_tempest_tests/plugin.py`, which will contain the following:
```
from tempest.test_discover import plugins

class MyPlugin(plugins.TempestPlugin):
```
Then we need to define all mandatory methods in the abstract class.
[Here is the list](https://docs.openstack.org/tempest/latest/plugin.html#abstract-plugin-class)
of them.



## Source
Information about creating a plugin were taken from the
[latest official tempest documentation](https://docs.openstack.org/tempest/latest/plugin.html)
