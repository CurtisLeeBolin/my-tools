#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  avtc.py
#
#  Copyright 2013 Curtis Lee Bolin <curtlee2002@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os, shlex, subprocess, time, datetime, re

class AvtcCommon:
	fileType=['avi', 'flv', 'mov', 'mp4', 'mpeg', 'mpg', 'ogg', 'ogm',
		'ogv', 'wmv', 'm2ts', 'mkv', 'rmvb', 'rm', '3gp', 'm4a', '3g2',
		'mj2', 'asf', 'divx', 'vob']

	def checkFileType(self, fileExtension):
		fileExtension = fileExtension[1:].lower()
		result = False
		for ext in self.fileType:
			if (ext == fileExtension):
				result = True
				break
		return result

	def runSubprocess(self, args):
		p = subprocess.Popen(shlex.split(args), stderr=subprocess.PIPE)
		stdoutData, stderrData = p.communicate()
		stderrData = stderrData.decode()
		return stderrData


if __name__ == '__main__':
	avtc = AvtcCommon()
	cwd = os.getcwd()
	fileList = os.listdir(cwd)
	fileList.sort()
	for f in fileList:
		if os.path.isfile(f):
			fileName, fileExtension = os.path.splitext(f)
			if avtc.checkFileType(fileExtension):
				args = 'mkvpropedit --set title="{}" {}'.format(fileName, os.path.abspath(f).__repr__())
				stderrData = avtc.runSubprocess(args)
				print('Re-Titled {}\n'.format(fileName))
