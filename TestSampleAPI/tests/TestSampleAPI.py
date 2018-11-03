#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import requests
from TestSampleAPI.helper import sampleApiHelper as api

RESPONSE_API = requests.get(url='https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false')
statusCode = RESPONSE_API.status_code
data = RESPONSE_API.json()

class TestApiFunctional:
    """
    This test suite verifies all the functional test cases of an API
    """

    def test_name_in_api(self):
        """ This test case verifies if name is Carbon Credit or not """
        api.verify_name(data)

    def test_relist_in_api(self):
        """ This test case verifies if Can Relist is true or not """
        api.verify_relist(data)

    def test_desc(self):
        """ This test case verfies if promotions which has gallery contains text \'2x larger image\' or not """
        api.verify_description(data)

class TestApiContract:
    """
    This test suite verifies the contract of an API
    """
    def test_api_contract(self):
        """ This test case verifies the contract of the api"""
        api.verify_contract(data,statusCode)
