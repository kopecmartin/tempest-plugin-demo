Prerequisites
-------------

Before you install and configure the service service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``tempest_tests`` database:

     .. code-block:: none

        CREATE DATABASE tempest_tests;

   * Grant proper access to the ``tempest_tests`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON tempest_tests.* TO 'tempest_tests'@'localhost' \
          IDENTIFIED BY 'TEMPEST_TESTS_DBPASS';
        GRANT ALL PRIVILEGES ON tempest_tests.* TO 'tempest_tests'@'%' \
          IDENTIFIED BY 'TEMPEST_TESTS_DBPASS';

     Replace ``TEMPEST_TESTS_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``tempest_tests`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt tempest_tests

   * Add the ``admin`` role to the ``tempest_tests`` user:

     .. code-block:: console

        $ openstack role add --project service --user tempest_tests admin

   * Create the tempest_tests service entities:

     .. code-block:: console

        $ openstack service create --name tempest_tests --description "service" service

#. Create the service service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        service public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        service internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        service admin http://controller:XXXX/vY/%\(tenant_id\)s
