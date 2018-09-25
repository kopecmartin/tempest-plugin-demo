# Copyright goes here

from tempest.test_discover import plugins

from my_tempest_tests import config as my_config


class MyTempestPlugin(plugins.TempestPlugin):
    """Provides basic hooks for MyTempestPlugin plugin.

    To provide tempest the necessary information to run the plugin.
    """

    def get_opt_lists(self, conf):
        """Get a list of options for sample config generation

        :return option_list: A list of tuples with the group name and options
                             in that group.
        :rtype: list

        Example::
            from tempest.config import cfg
            # Config options are defined in a config.py module
            service_option = cfg.BoolOpt(
                "my_service", default=True,
                help="Whether or not my service is available")

            my_service_group = cfg.OptGroup(name="my-service",
                                            title="My service options")
            my_service_features_group = cfg.OptGroup(
                name="my-service-features",
                title="My service available features")

            MyServiceGroup = [<list of options>]
            MyServiceFeaturesGroup = [<list of options>]

            # Plugin is implemented in a plugin.py module
            from my_plugin import config as my_config

            return [
                (my_config.my_service_group.name,
                 my_config.MyServiceGroup),
                (my_config.my_service_features_group.name,
                 my_config.MyServiceFeaturesGroup)
            ]
        """
        return [
            (my_config.my_service_group, my_config.MyServiceGroup),
            (my_config.my_service_features_group,
             my_config.MyServiceFeaturesGroup),
        ]

    def register_opts(self, conf):
        """Add additional configuration options to tempest.

        This method will be run for the plugin during the register_opts()
        function in tempest.config.

        :param ConfigOpts conf: The conf object that can be used to register
            additional options on.

        Example::

            # Config options are defined in a config.py module
            service_option = cfg.BoolOpt(
                "my_service",
                default=True,
                help="Whether or not my service is available")

            # Note: as long as the group is listed in get_opt_lists,
            # it will be possible to access its optins in the plugin code
            # via ("-" in the group name are replaces with "_"):
            #     CONF.my_service.<option_name>
            my_service_group = cfg.OptGroup(name="my-service",
                                            title="My service options")

            MyServiceGroup = [<list of options>]
            # (...) More groups and options...

            # Plugin is implemented in a plugin.py module
            from my_plugin import config as my_config

            def register_opts(self, conf):
                conf.register_opt(my_config.service_option,
                                  group='service_available')
                conf.register_group(my_config.my_service_group)
                conf.register_opts(my_config.MyServiceGroup,
                                   my_config.my_service_group)

                conf.register_group(my_config.my_service_feature_group)
                conf.register_opts(my_config.MyServiceFeaturesGroup,
                                   my_config.my_service_feature_group)
        """
        conf.register_opt(my_config.service_option,
                          group='service_available')

        conf.register_group(my_config.my_service_group)
        conf.register_opts(my_config.MyServiceGroup,
                           my_config.my_service_group)

        conf.register_group(my_config.my_service_feature_group)
        conf.register_opts(my_config.MyServiceFeaturesGroup,
                           my_config.my_service_feature_group)

    def load_tests(self):
        """Return the information necessary to load the tests in the plugin.

        :return: a tuple with the first value being the test_dir and the second
                 being the top_level
        :rtype: tuple
        """
        base_path = os.path.split(os.path.dirname(
            os.path.abspath(__file__)))[0]
        test_dir = "my_tempest_tests/tests"
        full_test_dir = os.path.join(base_path, test_dir)
        return full_test_dir, base_path

    def get_service_clients(self):
        """Get a list of the service clients for registration

        If the plugin implements service clients for one or more APIs, it
        may return their details by this method for automatic registration
        in any ServiceClients object instantiated by tests.
        The default implementation returns an empty list.

        :returns: Each element of the list represents the service client for an
          API. Each dict must define all parameters required for the invocation
          of `service_clients.ServiceClients.register_service_client_module`.
        :rtype: list of dictionaries

        Example implementation with one service client::

            def get_service_clients(self):
                # Example implementation with one service client
                myservice_config = config.service_client_config('myservice')
                params = {
                    'name': 'myservice',
                    'service_version': 'myservice',
                    'module_path': 'myservice_tempest_tests.services',
                    'client_names': ['API1Client', 'API2Client'],
                }
                params.update(myservice_config)
                return [params]

        Example implementation with two service clients::

            def get_service_clients(self):
                # Example implementation with two service clients
                foo1_config = config.service_client_config('foo')
                params_foo1 = {
                    'name': 'foo_v1',
                    'service_version': 'foo.v1',
                    'module_path': 'bar_tempest_tests.services.foo.v1',
                    'client_names': ['API1Client', 'API2Client'],
                }
                params_foo1.update(foo_config)
                foo2_config = config.service_client_config('foo')
                params_foo2 = {
                    'name': 'foo_v2',
                    'service_version': 'foo.v2',
                    'module_path': 'bar_tempest_tests.services.foo.v2',
                    'client_names': ['API1Client', 'API2Client'],
                }
                params_foo2.update(foo2_config)
                return [params_foo1, params_foo2]
        """
        return []

