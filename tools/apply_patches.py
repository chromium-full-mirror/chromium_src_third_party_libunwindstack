#!/usr/bin/env vpython3
# Copyright 2019 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
'''Applies patches from the patches/ directory onto the src/ directory.'''

import argparse
import os
import subprocess
import sys

_LIBUNWINDSTACK_PATCHES_DIR = os.path.join(
  os.path.dirname(__file__), os.pardir, 'patches')

def Main():
  # Using argparse ensures that we give help/usage commands, even if we
  # don't have any arguments.
  parser = argparse.ArgumentParser(description='''Applies patches from the
      patches/ directory onto the src/ directory.''')
  args = parser.parse_args()

  for filename in os.listdir(_LIBUNWINDSTACK_PATCHES_DIR):
    patch_path = os.path.join(_LIBUNWINDSTACK_PATCHES_DIR, filename)

    with open(patch_path, 'r') as patch_file:
      subprocess.check_call(['patch', '-p1'], stdin=patch_file)

  return 0


if __name__ == '__main__':
  sys.exit(Main())
