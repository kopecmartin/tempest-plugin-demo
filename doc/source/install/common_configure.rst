2. Edit the ``/etc/my_tempest_tests/my_tempest_tests.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://my_tempest_tests:MY_TEMPEST_TESTS_DBPASS@controller/my_tempest_tests
