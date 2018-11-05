# copyright goes here

from tempest.config import cfg

service_option = cfg.BoolOpt("my_service",
                             default=False,
                             help="Whether or not my_service is expected to be"
                                  " available")

my_service_group = cfg.OptGroup(name="my-service",
                                title="My service options")

my_service_feature_group = cfg.OptGroup(name="my-service-features",
                                        title="My service available features")

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

MyServiceFeaturesGroup = [
    cfg.IntOpt("build_interval",
               default=3,
               help="Time in seconds between share availability checks."),
    cfg.IntOpt("build_timeout",
               default=500,
               help="Timeout in seconds to wait for a share to become"
               "available."),
    cfg.StrOpt('test_ssh_user',
               default='ubuntu',
               help='username used to access the test image.')
]
