#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kakakaya, Date: Sat Feb  4 23:49:58 2017
from tweetsave import api
from unittest import TestCase
from nose.tools import ok_, eq_


class TestSave(TestCase):
    def test_save(self):
        result = api.save(827889729659998208)
        ok_(result)
        eq_(result["status"], "OK")

    def test_no_id(self):
        result = api.save(827889729659998209)
        ok_(result)
        eq_(result["errors"], ["Twitter API error (No status found with that ID.)"])


class TestStream(TestCase):
    def test_list(self):
        result = api.stream('XjEtT')
        ok_(result)
        eq_(len(result), 3)
