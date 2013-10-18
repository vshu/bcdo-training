#!/usr/bin/env python

import os
import re

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

from pprint import pprint

ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY', None)
SECRET_KEY = os.environ.get('AWS_SECRET_KEY', None)
assert ACCESS_KEY is not None
assert SECRET_KEY is not None

driver = get_driver(Provider.EC2_US_WEST)
conn = driver(ACCESS_KEY, SECRET_KEY)

SIZE_ID = 't1.micro'
KEYPAIR_NAME = 'Ubuntu1'
SECURITY_GROUP_NAMES = 'default'

nodes = conn.list_nodes()
sizes = conn.list_sizes()
images = conn.list_images()

size = [s for s in sizes if s.id == 't1.micro'][0]
image = images[0]

pprint(nodes)
pprint(size)
pprint(image)

#node = conn.create_node(name='test-node-1', image=image, size=size, ex_keyname=KEYPAIR_NAME, ex_securitygroup=SECURITY_GROUP_NAMES)
