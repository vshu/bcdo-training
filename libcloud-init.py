#!/usr/bin/env python

import os
import re

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

Driver = get_driver(Provider.EC2)

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY', None)
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY', None)
assert AWS_ACCESS_KEY is not None
assert AWS_SECRET_KEY is not None

conn = Driver(AWS_ACCESS_KEY, AWS_SECRET_KEY)
