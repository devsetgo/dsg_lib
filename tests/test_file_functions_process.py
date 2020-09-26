# -*- coding: utf-8 -*-

import datetime
import unittest

import pytest
from devsetgo_lib.file_functions import create_sample_files

# from devsetgo_lib.file_functions import get_data_directory_list
from devsetgo_lib.file_functions import open_csv
from devsetgo_lib.file_functions import open_json
from devsetgo_lib.file_functions import open_text

time_str = datetime.datetime.now()


class Test(unittest.TestCase):
    def test_create_sample_files(self):
        filename = "test_sample"
        samplesize = 10
        create_sample_files(filename, samplesize)

        file_named = "test_1.csv"
        result = open_csv(file_named)

        assert len(result) == samplesize - 1

    def test_open_json(self):
        file_named = "test_1.json"
        result = open_json(file_named)
        assert len(result) > 1
        assert isinstance(result, (list, dict))

    def test_open_json_no_file(self):
        file_named = "no_file_name.json"
        with pytest.raises(Exception):
            assert open_json(file_named)

    def test_open_json_exception_not_str(self):
        file_named = ["a", "list"]
        with pytest.raises(Exception):
            assert open_json(file_named)

    def test_open_json_exception_slash_win(self):
        file_named = "\this_is_not_right_json"
        with pytest.raises(Exception):
            assert open_json(file_named)

    def test_open_json_exception_slash_linux(self):
        file_named = "//this_is_not_right_json"
        with pytest.raises(Exception):
            assert open_json(file_named)

    def test_open_csv(self):
        file_named = "test_1.csv"
        result = open_csv(file_named)
        assert len(result) > 1

    def test_open_csv_no_file(self):
        file_named = "no_file_name.csv"
        with pytest.raises(Exception):
            assert open_csv(file_named)

    def test_open_csv_exception_not_str(self):
        file_named = ["a", "list"]
        with pytest.raises(Exception):
            assert open_csv(file_named)

    def test_open_csv_exception_slash_win(self):
        file_named = "\this_is_not_right_csv"
        with pytest.raises(Exception):
            assert open_csv(file_named)

    def test_open_csv_exception_slash_linux(self):
        file_named = "//this_is_not_right_csv"
        with pytest.raises(Exception):
            assert open_csv(file_named)

    def test_open_text(self):
        file_named = "test_1.html"
        result = open_text(file_named)
        assert "Test" in str(result)

    def test_open_txt_no_file(self):
        file_named = "no_file_name.html"
        with pytest.raises(Exception):
            assert open_text(file_named)

    def test_open_txt_exception_not_str(self):
        file_named = ["a", "list"]
        with pytest.raises(Exception):
            assert open_text(file_named)

    def test_open_txt_exception_slash_win(self):
        file_named = "\this_is_not_right_txt"
        with pytest.raises(Exception):
            assert open_text(file_named)

    def test_open_txt_exception_slash_linux(self):
        file_named = "//this_is_not_right_txt"
        with pytest.raises(Exception):
            assert open_text(file_named)