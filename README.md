Requirements
===============

* Python 2.0 or greater
* zlib C library 1.2.x or greater

Installation
===============

	python setup.py build
	python setup.py install

Usage
===============

* See test.py for example usage with GeoIP Country
* See test_org.py for example usage with GeoIP ISP and Organization
* See test_city.py for example usage with GeoIP City
* See test_region.py for example usage with GeoIP Region
* See test_netspeed.py for example usage with GeoIP Netspeed
* See test_v6.py for example usage with GeoIP v6 Country Database
* See test_city_acc.py for example usage with GeoIP Confidence and Accuracy Database

Red Hat OpenShift
===============

There are no GeoIP C libraries in OpenShift, so I made this package to simplify installing GeoIP-Python.
Please put the following code into your setup.py in OpenShift:

```python
setup(
	...
	install_requires = [
		...
		'GeoIP-Python>=1.2.7',
	],
	dependency_links = [
		'https://github.com/likema/maxmind-geoip/zipball/openshift#egg=GeoIP-Python-1.2.7'
	],
)
```

License
===============

Copyright (c) 2010 MaxMind LLC

All rights reserved.  This package is free software; it is licensed
under the LGPL.
