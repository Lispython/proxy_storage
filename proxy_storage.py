# -*- coding:  utf-8 -*-

import re
from random import choice

from cStringIO import StringIO


socket_re=re.compile(
                r'((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))'
                r'(?:(?:\s+)|(?:\s*:\s*)|(?:[\W|\w\S]+?))(\d{1,5})'
                )

class ImplementationError(Exception):
    pass


class Proxy(object):
    """Proxy address object
    """

    def __init__(self, ip, port):
        """Proxy address init method

        Arguments:
        - `address`:
        """
        self._ip = ip
        self._port = port

    def __str__(self):
        """Print method for proxy

        Arguments:
        - `self`:
        """
        return " %s:%s" % (self._ip, self._port)


class BaseProxyStorage(object):
    """Base proxy storage
    """

    def __init__(self):
        """
        """
        self._proxies = []

    def __len__(self):
        """Project list length
        
        Arguments:
        - `self`:
        """
        return len(self._proxies)

    def __iter__(self):
        """Storage as iterable object
        
        Arguments:
        - `self`:
        """
        for proxy in self._proxies:
            yield proxy


    def load_proxies(self):
        """Load proxies method
        
        Arguments:
        - `self`:
        """
        raise ImplementationError

    
    def get_random(self):
        """

        Arguments:
        - `self`:
        """
        if self._proxies is []:
            self.load_proxies()
        return choice(self._proxies)

    def add_proxy(self, proxy):
        """Add proxy to list
        
        Arguments:
        - `self`:
        - `proxy`: proxy object
        """
        self._proxies.append(proxy)
        

class StringProxyStorage(BaseProxyStorage):
    """StringProxyStorage
    """
    
    def __init__(self, string):
        """String Proxy Storage
        
        Arguments:
        - `string`:
        """
        self._string = StringIO(string)
        super(StringProxyStorage, self).__init__()
        

    def load_proxies(self):
        """Load proxies from string
        
        Arguments:
        - `self`:
        """
        proxies = socket_re.findall(self._string.read())
        for proxy in proxies:
            self._proxies.append(Proxy(proxy[0], proxy[1]))


class FileProxyStorage(BaseProxyStorage):
    """File proxy storage
    """

    def __init__(self, filename):
        """File proxy storage init method

        Arguments:
        - `filename`:
        """
        self._filename = filename
        super(FileProxyStorage, self).__init__()


    def load_proxies(self):
        """Load proxies from file
        
        Arguments:
        - `self`:
        """
        with open(self._filename) as f:
            for line in f:
                proxy = Proxy(*line.split(":"))
                self._proxies.append(proxy)
        

