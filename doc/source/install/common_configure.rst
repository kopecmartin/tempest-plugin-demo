2. Edit the ``/etc/tempest_tests/tempest_tests.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://tempest_tests:TEMPEST_TESTS_DBPASS@controller/tempest_tests
