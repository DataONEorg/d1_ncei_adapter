#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('..')

if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pasta_gmn_adapter.settings")

  from django.core.management import execute_from_command_line

  execute_from_command_line(sys.argv)