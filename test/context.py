# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Jeaustin Sirias
#
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports
from source import source, channel, modulation

def filepath(rel_path, *filenames):
	path = os.path.dirname(os.path.abspath('context.py'))
	abspath = os.path.join(path, rel_path)
	paths = [abspath + files for files in filenames]
	return paths




