# tempest-plugin-demo

## About
This repository is a part of a technical presentation ([slides](TODO)).
It contains a quick overview of Tempest, python-tempestconf and describes steps
how to create a simple Tempest plugin.

### Content
1. [Create a plguin structure](#create-a-plugin-structure)
2. [Entry point](#entry-point)
3. [Installing a plugin](#installing-a-plugin)

    [Globally](#globally)
    [In a virtual environment](#in-a-virtual-environment)

4. [Generating a sample tempest.conf](#generating-a-sample-tempest.conf)
5. [Plugin options](#plugin-options)
6. [Plugin class](#plugin-class)

    [get_opt_lists](#get_opt_lists)
    [register_opts](#register_opts)
    [load_tests](#load_tests)
    [get_service_clients](#get_service_clients)


## Create a plugin structure
Create a [structure](https://docs.openstack.org/tempest/latest/plugin.html#plugin-cookiecutter)
using [cookiecutter](https://github.com/openstack-dev/cookiecutter).

```console
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


## Entry point
In order to let Tempest find our plugin an entry point needs to be created.
The following example shows a structure of an entry point entry in `setup.cfg`
file:
```python
[entry_points]
tempest.test_plugins =
    plugin_name = module.path:PluginClass
```

In case of this presentation, the following needs to be added to `setup.cfg`
```python
[entry_points]
tempest.test_plugins =
    my_tempest_tests = my_tempest_tests.plugin:MyTempestPlugin
```

## Installing a plugin
After an entry point was added it's good to check that Tempest is able to
discover the plugin. How can we do that? Simply, let's install the plugin and
list all available plugins via Tempest.

### Globally:
Note: Tempest and pip with setuptools are globally installed too.
```console
$ cd tempest-plugin-demo
$ sudo pip install -e .
$ tempest list-plugins  # verify that Tempest discovers the plugin
+------------------+-----------------------------------------+
|       Name       |                EntryPoint               |
+------------------+-----------------------------------------+
| my_tempest_tests | my_tempest_tests.plugin:MyTempestPlugin |
+------------------+-----------------------------------------+
```

### In a virtual environment:
Note: Tempest is installed in a venv together with pip and setuptools.
```console
(tempest)$ pip install -e /home/$USER/path/to/tempest-plugin-demo
(tempest)$ tempest list-plugins  # verify that Tempest discovers the plugin
+------------------+-----------------------------------------+
|       Name       |                EntryPoint               |
+------------------+-----------------------------------------+
| my_tempest_tests | my_tempest_tests.plugin:MyTempestPlugin |
+------------------+-----------------------------------------+
```

The plugin was successfully discovered by Tempest. Now, when we're sure that
Tempest is able to discover the plugin, we need to add some logic in it, see
below.


## Generating a sample tempest.conf
I'm gonna use this later to verify, that `get_opt_lists` and `register_opts`
methods are defined properly.

### In a vritual environment:
Prepare a virtual environment via tox and source it
```console
$ cd tempest
$ tox -egenconfig
$ source .tox/genconfig/bin/activate
```
Don't forget to install your (and others if wanted) plugin(s). For information
on how to do it, check the [Installing a plugin](#installing-a-plguin) section.
Verify that all wanted plugins are installed:
```console
(genconfig)$ tempest list-plugins
```
Now run the tox command again
```console
(genconfig)$ tox -egenconfig
```
Or run `oslo-config-generator` directly, if you check `tox.ini` file you'll see
it's the same command tox uses.
```console
$ oslo-config-generator --config-file tempest/cmd/config-generator.tempest.conf
```
Now a sample `tempest.conf` was created under `./etc/` directory called
`tempest.conf.sample`.


## Plugin options
Under plugin directory, which is in this case, `my_tempest_tests` directory, we
need to define a `config.py`.

First, we need to import **cfg from tempest.config module**, which is one of the
stable APIs Tempest provides,
[see here](https://docs.openstack.org/tempest/latest/plugin.html#stable-tempest-apis-plugins-may-use).
```python
from tempest.config import cfg
```
The whole `config.py` can be seen [here](TODO).

### Options and option group
Let's create an option group called `my_service_group`:
```python
my_service_group = cfg.OptGroup(name="my-service",
                                title="My service options")
```
The example above shows how an option group can be created. It's name is
`my-service` and it's a section name in a `tempest.conf` file.

When we have a group, let's create also a few options which will be part of
that group (they are just defined here, in register_opts method we'll make sure
they will be part of the group we want).
```python
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


## Plugin Class
We need to create a plugin class, in order to provide Tempest all required
information for running our plugin. To simplify this, Tempest provides an
abstract class that should be used as the parent for our plugin [].

Let's create a `my_tempest_tests/plugin.py` file, which will contain the
following:
```python
# import Tempest's API for plugins
from tempest.test_discover import plugins
# import config.py we have defined in the previous step
from my_tempest_tests import config as my_config


# the class which provides the necessary information to run the plugin
class MyTempestPlugin(plugins.TempestPlugin):
    pass
```
Then we need to define the all mandatory methods in the abstract class.
[Here is the list](https://docs.openstack.org/tempest/latest/plugin.html#abstract-plugin-class)
of them. Init `plugin.py` with declarations of the methods can be found
[here](TODO).


### get_opt_lists
This method defines configuration options for our plugin, the options, which
will be read from tempest.conf during the execution and also will be used for
sample config generation. For generating a sample tempest.conf, see
[Generating a sample tempest.conf](#generating-a-sample-tempest.conf) section.

What we're going to return a list of tuples where each tuple contains
name of our option group and a list of the options which belong to that group.
So there will be as many tuples as option groups we defined.
Plus, if want to have service option included in a sample tempest.conf, we may
define another tuple. In the example below it's the last tuple, where we
say that we want to have our `my_config.service_option` included in the
`service_available` group - which is a group registered already by Tempest.

```python
def get_opt_lists(self):
    return [
        (my_config.my_service_group.name, my_config.MyServiceGroup),
        (my_config.my_service_features_group.name,
        my_config.MyServiceFeaturesGroup),
        ('service_available', [my_config.service_option])
    ]
```

### register_opts
The method registers our options defined in config.py which are the same ones
`get_opt_lists` returns . This method also allows us to set any additional
configuration options.

In the example below I first register my `service_option` option under
already registered by Tempest group called `service_available`.

Then I register one of my groups defined in the `config.py` and options which
should belong to that group. And then the same for the other groups accordingly.
```python
def register_opts(self, conf):
    # don't register service_available group, it's done so by Tempest
    conf.register_opt(my_config.service_option,
                      group='service_available')

    # registering one of my option groups
    conf.register_group(my_config.my_service_group)
    # registering options which I want to have under that group
    conf.register_opts(my_config.MyServiceGroup,
                       my_config.my_service_group)

    # registering the other group I have defined in config.py
    conf.register_group(my_config.my_service_feature_group)
    # registering the options I want to have under that group
    conf.register_opts(my_config.MyServiceFeaturesGroup,
                       my_config.my_service_feature_group)
```

By additional configuration is meant for example that you may add a logic here
which chooses the default values for some of the options under certain
circumstances, like:
```python
if certain_circumstances:
    conf.set_default(
        "name_of_option_i_want_to_set_value_to",
        value,
        group="name_of_the_group_the_option_is"
    )
```

**Note:** When we have defined both `get_opt_lists` and `register_opts`, it's
recommended to generate a sample tempest.conf, if it is successfully
generated, we probably defined everything well.


### load_tests
This method defines a path to plugin’s tests. Thanks to this Tempest knows
where to find our plugin tests.

It returns a tuple with the first value being the test_dir and the second
being the top_level, for example:
```python
def load_tests(self):
    base_path = os.path.split(os.path.dirname(
        os.path.abspath(__file__)))[0]
    test_dir = "my_tempest_tests/tests"
    full_test_dir = os.path.join(base_path, test_dir)

    return full_test_dir, base_path
```

To verify our tests can be discovered, let's try listing them:
```console
(tempest)$ ostestr -l
```

If there are any problems, try to create a workspace with `--debug` argument
enabled, it may be helpful for showing a more clear tracebacks.
```console
(tempest)$ tempest init --debug <name of a workspace>
(tempest)$ cat tempest.log
```

### get_service_clients
This method is optional. If your plugin implements a service client you may
use this method for its automatic registration.

```python
def get_service_clients(self):
    pass
```












































## Source
Information about creating a plugin were taken from the
[latest official tempest documentation](https://docs.openstack.org/tempest/latest/plugin.html)
