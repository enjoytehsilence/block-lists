#!/usr/bin/env python
from fileinput import input
for y in sorted([x.strip().split('.')[::-1] for x in input()]): print '.'.join(y[::-1])
