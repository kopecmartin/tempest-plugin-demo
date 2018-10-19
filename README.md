# tempest-plugin-demo

## About
This repository is a part of a technical presentation ([slides](TODO)).
It contains a quick overview of Tempest, python-tempestconf and describes steps
how to create a simple Tempest plugin.

## A simple Tempest plugin

### Create a plugin structure
Create a [structure](https://docs.openstack.org/tempest/latest/plugin.html#plugin-cookiecutter)
using [cookiecutter](https://github.com/openstack-dev/cookiecutter).

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
The full output can be
[seen here](https://github.com/kopecmartin/tempest-plugin-demo/blob/master/doc/LOGS/cookiecutter_success.md)


### Entry point
In order to let Tempest find your plugin an entry point needs to be created.
The following example shows a structure of an entry point entry in `setup.cfg`
file:
```
[entry_points]
tempest.test_plugins =
    plugin_name = module.path:PluginClass
```

In case of this presentation, the following needs to be added to `setup.cfg`
```
[entry_points]
tempest.test_plugins =
    my_tempest_tests = my_tempest_tests.plugin:MyTempestPlugin
```

### Installing a plugin
After an entry point was added it's good to check that Tempest is able to
discover the plugin. How can we do that? Simply, let's install the plugin and
list all available plugins via Tempest.

#### Globally:
Note: Tempest and pip with setuptools are globally installed too.
```
$ cd tempest-plugin-demo
$ sudo pip install -e .
$ tempest list-plugins  # verify that Tempest discovers the plugin
+------------------+-----------------------------------------+
|       Name       |                EntryPoint               |
+------------------+-----------------------------------------+
| my_tempest_tests | my_tempest_tests.plugin:MyTempestPlugin |
+------------------+-----------------------------------------+
```

#### In a virtual environment:
Note: Tempest is installed in a venv together with pip and setuptools.
```
(tempest) $ pip install -e /home/$USER/path/to/tempest-plugin-demo
(tempest) $ tempest list-plugins  # verify that Tempest discovers the plugin
+------------------+-----------------------------------------+
|       Name       |                EntryPoint               |
+------------------+-----------------------------------------+
| my_tempest_tests | my_tempest_tests.plugin:MyTempestPlugin |
+------------------+-----------------------------------------+
```

The plugin was successfully discovered by Tempest. Now, when we're sure that
Tempest is able to discover the plugin, we need to add some logic in it, see
below.

### Plugin options
Under plugin directory, which is in this case, my_tempest_tests directory, we
need to define a `config.py`.

First, we need to import cfg from tempest.config module, which is one of the
stable APIs Tempest provides,
[see here](https://docs.openstack.org/tempest/latest/plugin.html#stable-tempest-apis-plugins-may-use)
```
from tempest.config import cfg
```
The whole `config.py` can be seen [here](TODO)

#### Options and option group
Let's create an option group called `my_service_group`:
```
my_service_group = cfg.OptGroup(name="my-service",
                                title="My service options")
```
The example above shows how an option group can be created. It's name is
`my-service` and it's a section name in a `tempest.conf` file.

When we have a group, let's create also a few options which will be part of
that group.
```
MyServiceGroup = [
    cfg.StrOpt("catalog_type",
               default="share",
               help="Catalog type of the Share service."),
    cfg.StrOpt('endpoint_type',
               default='publicURL',
               choices=['public', 'admin', 'internal',
                        'publicURL', 'adminURL', 'internalURL'],
               help="The endpoint type to use for the share service.")
]
```
In the previous example we've defined only string options, but other options
of a different types can be created, like:
- BoolOpt - boolean type option
- IntOpt  - integer type option
- FloatOpt - float type option
- ListOpt - option of a list type
- DictOpt - option of a dict type
and others. Tempest inherits type definitions of the options from
[oslo.config](https://github.com/openstack/oslo.config/tree/master/oslo_config)
so the all definitions can be found
[here](https://github.com/openstack/oslo.config/blob/master/oslo_config/cfg.py)


### Plugin Class
We need to create a plugin class, in order to provide Tempest all required
information for running our plugin. To simplify this, Tempest provides an
abstract class that should be used as the parent for our plugin [].

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
