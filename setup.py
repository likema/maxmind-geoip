from distutils.core import setup, Extension
import os

def c_macro_str(v):
	return '"%s"' % v

module1 = Extension('GeoIP',
	sources = [
		'py_GeoIP.c',

		# libGeoIP source
		'libGeoIP/GeoIP.c',
		'libGeoIP/GeoIPCity.c',
		'libGeoIP/regionName.c',
		'libGeoIP/timeZone.c',

		# libGeoIPUpdate source
		'libGeoIP/GeoIPUpdate.c',
		'libGeoIP/md5.c',
	],
	include_dirs = ['libGeoIP'],
	libraries = ['z'],
	define_macros = [
		('PACKAGE_NAME', c_macro_str('GeoIP')),
		('PACKAGE_TARNAME', c_macro_str('GeoIP')),
		('PACKAGE_VERSION', c_macro_str('1.4.8')),
		('PACKAGE_STRING', c_macro_str('1.4.8')),
		('PACKAGE_BUGREPORT', c_macro_str('support@maxmind.com')),
		('PACKAGE_URL', c_macro_str('http://www.maxmind.com/app/c')),
		('STDC_HEADERS', '1'),
		('HAVE_SYS_TYPES_H', '1'),
		('HAVE_SYS_STAT_H', '1'),
		('HAVE_STDLIB_H', '1'),
		('HAVE_STRING_H', '1'),
		('HAVE_MEMORY_H', '1'),
		('HAVE_STRINGS_H', '1'),
		('HAVE_INTTYPES_H', '1'),
		('HAVE_STDINT_H', '1'),
		('HAVE_UNISTD_H', '1'),
		('__EXTENSIONS__', '1'),
		('_ALL_SOURCE', '1'),
		('_GNU_SOURCE', '1'),
		('_POSIX_PTHREAD_SEMANTICS', '1'),
		('_TANDEM_SOURCE', '1'),
		('HAVE_DLFCN_H', '1'),
		('HAVE_USHORT_TYPEDEF', '1'),
		('HAVE_ULONG_TYPEDEF', '1'),
		('HAVE_ZLIB_H', '1'),
		('HAVE_GETTIMEOFDAY', '1'),
		('HAVE_VASPRINTF', '1'),
		('HAVE_VSNPRINTF', '1'),
		('HAVE_VSPRINTF', '1'),
		('HAVE_GETHOSTBYNAME', '1'),
		('HAVE_GETHOSTBYNAME_R', '1'),
		('GETHOSTBYNAME_R_RETURNS_INT', '1'),
		('GEOIPDATADIR', c_macro_str(os.environ["OPENSHIFT_DATA_DIR"])),
	],
)

setup (name = 'GeoIP-Python',
	version = '1.2.7',
	description = 'This is a python wrapper to GeoIP',
	ext_modules = [module1])
