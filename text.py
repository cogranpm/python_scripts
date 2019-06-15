#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  text.py
#  
#  Copyright 2019 Paul Martin <paulm@localhost.localdomain>
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

import string

def main(args):
	stringstuff()
	
def stringstuff():
	s = 'The quick brown fox jumped over the lazy brown dog.'
	print (string.capwords(s))	
	templates()
	
def templates():
	#---------------templates-----------------
	#this is a map
	values = {"iamakey":"iamavalue"}
	t = string.Template("""
	Here is some stuff: $iamakey
	""")
	print (t.substitute(values))
	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
