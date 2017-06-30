# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.person import Person
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_conn_port_get(self):
        """
        Test case for conn_port_get

        
        """
        query_string = [('port', 1.2)]
        response = self.client.open('/conn_port',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
