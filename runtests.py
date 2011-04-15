# -*- coding:  utf-8 -*-

import unittest
import os.path
from proxy_storage import FileProxyStorage, Proxy, BaseProxyStorage, StringProxyStorage


class StringProxyStorageTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def teadDown(self):
        pass

    def test_storage(self):
        proxies_string = """
        184.77.156.193:8085
        122.225.19.181:3128
        173.243.84.66:8080
        88.202.61.114:80
        41.234.205.213:8080
        187.111.192.4:8080
        121.52.156.82:8080
        173.243.84.66:8080
        88.202.61.114:80
        92.114.82.118:8080
        117.203.48.79:8090
        184.77.156.193:8085
        80.108.94.196:8123
        182.163.78.42:8080
        71.7.133.28:8085
        95.56.229.190:3128
        115.249.32.201:8080
        98.243.21.210:18645
        76.125.181.129:23269
        98.216.80.12:1603
        83.138.50.6:5190
        80.72.229.188:8080
        85.233.83.186:3128
        """
        
        storage = StringProxyStorage(proxies_string)

        self.assertTrue(isinstance(storage, StringProxyStorage))
        storage.load_proxies()
        self.assertEquals(len(storage), 23)
        for proxy in storage:
            self.assertTrue(isinstance(proxy, Proxy))


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "proxies_list.txt"))
        
    def tearDown(self):
        pass

    def test_storage(self):
        storage = FileProxyStorage(self.filename)

        self.assertTrue(isinstance(storage, FileProxyStorage))
        storage.load_proxies()
        self.assertEquals(storage._filename, self.filename)
        self.assertEquals(len(storage), 56)
        for proxy in storage:
            self.assertTrue(isinstance(proxy, Proxy))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(StringProxyStorageTestCase))
    suite.addTest(unittest.makeSuite(FileStorageTestCase))
    return suite
    

if __name__ == '__main__':
    unittest.main(defaultTest = "suite")
