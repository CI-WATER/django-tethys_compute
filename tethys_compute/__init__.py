import os

default_app_config = 'tethys_compute.apps.TethysComputeConfig'

TETHYSCLUSTER_CFG_DIR = os.path.join(os.path.expanduser('~'), '.tethyscluster')
TETHYSCLUSTER_CFG_FILE = os.path.join(TETHYSCLUSTER_CFG_DIR, 'config')
TETHYSCLUSTER_TETHYS_CFG_FILE = os.path.join(TETHYSCLUSTER_CFG_DIR, 'tethys_config')

TETHYSCLUSTER_CONFIG_TEMPLATE = """
[global]
DEFAULT_TEMPLATE=default_cluster
INCLUDE=~/.tethyscluster/tethys_config

[key tethys_key]
KEY_LOCATION=~/Documents/_MyDocuments/CI-Water/starcluster-east.pem

[cluster default_cluster]
KEYNAME = tethys_key
CLUSTER_SIZE = 1
CLUSTER_SHELL = bash
NODE_IMAGE_ID = ami-92ef8cfa
NODE_INSTANCE_TYPE = t2.micro
PLUGINS = condor

[plugin condor]
SETUP_CLASS = tethyscluster.plugins.condor.CondorPlugin
"""

TETHYSCLUSTER_TETHYS_CONFIG_TEMPLATE = """
[aws info]
AWS_ACCESS_KEY_ID=%(aws_access_key_id)s
AWS_SECRET_ACCESS_KEY=%(aws_secret_access_key)s
AWS_USER_ID=%(aws_user_id)s

[key starcluster-east]
KEY_LOCATION=%(key_location)s
"""

with open(TETHYSCLUSTER_CFG_FILE, 'w') as config_file:
    config_file.write(TETHYSCLUSTER_CONFIG_TEMPLATE)
