Prerequisites
-------------

Before you install and configure the my_service service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``my_tempest_tests`` database:

     .. code-block:: none

        CREATE DATABASE my_tempest_tests;

   * Grant proper access to the ``my_tempest_tests`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON my_tempest_tests.* TO 'my_tempest_tests'@'localhost' \
          IDENTIFIED BY 'MY_TEMPEST_TESTS_DBPASS';
        GRANT ALL PRIVILEGES ON my_tempest_tests.* TO 'my_tempest_tests'@'%' \
          IDENTIFIED BY 'MY_TEMPEST_TESTS_DBPASS';

     Replace ``MY_TEMPEST_TESTS_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``my_tempest_tests`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt my_tempest_tests

   * Add the ``admin`` role to the ``my_tempest_tests`` user:

     .. code-block:: console

        $ openstack role add --project service --user my_tempest_tests admin

   * Create the my_tempest_tests service entities:

     .. code-block:: console

        $ openstack service create --name my_tempest_tests --description "my_service" my_service

#. Create the my_service service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        my_service public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        my_service internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        my_service admin http://controller:XXXX/vY/%\(tenant_id\)s
