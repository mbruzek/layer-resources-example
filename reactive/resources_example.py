from charms.reactive import when, when_not, set_state


@when_not('terms-resources.installed')
def install_terms-resources():

    set_state('terms-resources.installed')
