========
NameSilo
========

A simple wrapper for the NameSilo API_.

.. _API: https://www.namesilo.com/api_reference.php

Forked with minor updates and code changes from https://github.com/kolanos/namesilo

For the latest updates on this fork see https://github.com/dvrhax/namesilo

Install
--------

To install via pip:

    pip install namesilo

Usage
------

Instantiating the client:

    import namesilo

    # By default the client initializes in sandbox mode
    ns = namesilo.NameSilo('API KEY HERE')

    # Instantitate in live mode
    ns = namesilo.NameSilo('API KEY HERE', live=True)

    # Instantitate in legacy mode - Legacy mode allows you to use the previous operation naming convention by default operations will be called identical to the api reference
    ns = namesilo.NameSilo('API KEY HERE', legacy=True)

    # You can also control batch mode, api version, and response type
    ns = namesilo.NameSilo('API KEY HERE', live=False, batch=False, version='1', responseType='xml')

From here you can call operations like so:

    ns.registerDomain(domain='yourdomain.com', years='1')

	Or in legacy mode

    ns.register_domain(domain='yourdomain.com', years='1')

Operations
----------

This client renames the operations to follow a more consistent convention of
(verb)_(subject). See *namesilo.NAMESILO_OPERATIONS* to seehow these method
names map to their NameSilo counterparts. The goal of this mapping its to make
the API more intuitive.
