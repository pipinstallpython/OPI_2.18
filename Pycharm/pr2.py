#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

while True:
    key_value = input("Enter the key of the environment variable:")

    try:
        if os.environ[key_value]:
            print(
                "The value of", key_value,
                " is ", os.environ[key_value]
            )
    except KeyError:
        print(key_value, "environment variable is not set")
        sys.exit(1)
