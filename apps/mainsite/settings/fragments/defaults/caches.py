###
#
# Caching
#
###

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': None,
        'KEY_PREFIX': 'wlm_',
        'VERSION': 1,
    }
}