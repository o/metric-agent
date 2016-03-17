=============
metricd-agent
=============

.. image:: https://travis-ci.org/o/metric-agent.svg?branch=master
    :target: https://travis-ci.org/o/metric-agent

metricd is agent for collecting and sending metrics. Currently collects information about system and sends as JSON via HTTP. In the future more reporters (e.g statsd, graphite, riemann, influxdb) and collectors (e.g. metricd-nginx, metricd-haproxy, metricd-mysql, metricd-redis) will be available.

Installation
============

pip is easiest way to install metricd. 

**Dependencies**

* python 2.7, >=3.3 (tested with version 2.7, 3.3, 3.4, 3.5)
* Python development tools and libraries (called python-dev or devel)
* pip

**Installing dependencies**

Ubuntu / Debian::

    $ sudo apt-get install python-dev gcc
    
RedHat / CentOS::

    $ sudo yum install python-devel gcc

OSX

You need to install `Xcode <https://developer.apple.com/xcode/download/>`__

**Installing pip**

Ubuntu / Debian::

    $ sudo apt-get install python-pip

RedHat / CentOS::

    $ sudo yum install python-pip # from EPEL repository


Any platform::

    $ curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $ sudo python get-pip.py

**Installing package**::

    $ sudo pip install metricd

**Upgrading**::

    $ sudo pip install metricd --upgrade

**Uninstalling**::

    $ sudo pip uninstall metricd

Running
=======

The following command prints metrics to console::

    metricd console
    
If you want to send metrics with HTTP POST as JSON::

    $ metricd http --url http://localhost:3000/collect
    
    ## with extra headers
    
    $ metricd http --url http://localhost:3000/collect --headers X-Foo=Bar --headers X-Access-Token=jaezei9G

License
=======

The MIT License (MIT), Copyright (c) 2016 Osman Ungur
