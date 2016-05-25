#!/usr/bin/env python

import subprocess
from charmhelpers.core.hookenv import resource_get
from charms.reactive import when
from charms.reactive import when_not
from charms.reactive import set_state


@when_not('resources-example.fetched')
def fetch_resources_example():
    """ Fetch the resource from Juju."""
    print('Fetching resource with resource_get(name="software")'')
    path = resource_get(name='software')
    print(path)
    subprocess.check_call(['sha1sum', path])
    set_state('resources-example.fetched')
