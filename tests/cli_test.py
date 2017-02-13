#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kakakaya, Date: Mon Feb 13 20:36:48 2017
from tweetsave import cli, api
from unittest import TestCase, mock
from nose.tools import ok_, eq_, raises

from click.testing import CliRunner


class TestCli(TestCase):
    def test_list(self):
        # setup mock
        api_list = mock.Mock()
        api_list.return_value = [
            {"user": {"screen_name": "user1"}, "text": "text_1"},
            {"user": {"screen_name": "user2"}, "text": "text_2"},
            {"user": {"screen_name": "user3"}, "text": "text_3"},
        ]
        api.stream = api_list   # patch mock

        test_target_id = "some_id"
        runner = CliRunner()
        result = runner.invoke(cli.list, [test_target_id])  # run and output values

        eq_(api_list.call_args[0][0], test_target_id)  # check how it called

        ok_("@user1: text_1" in result.output)  # check output
        eq_(result.exit_code, 0)                # check whether it succeed or not

    def test_save(self):
        api_save = mock.Mock()
        sample_output_url = "https://tweetsave.com/sample_url"
        api_save.return_value = {"status": "OK", "redirect": sample_output_url}
        api.save = api_save     # patch mock

        test_target_id = '1234567890'
        runner = CliRunner()
        result = runner.invoke(cli.save, [test_target_id])

        # ok_(api_save.called)
        eq_(result.exit_code, 0)
        eq_(api_save.call_args[0][0], test_target_id)
        ok_(sample_output_url in result.output)
