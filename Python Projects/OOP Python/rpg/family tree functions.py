# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:10:41 2017

@author: Monic
"""

isinstance('a', str)

isinstance(5.2, (int, float))

isinstance(True, int)

issubclass(bool, int)

issubclass(str, int)

issubclass(Theif, Character)

from thieves import Thief

kenneth = Thief(foobar  = "Kenneth")
type(kenneth)

kenneth.__class__.__name__
