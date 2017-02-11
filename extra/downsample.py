#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
from gnuradio import gr

class downsample(gr.decimator_block):
    """
    docstring for block downsample
    """
    factor = 0
    def __init__(self, factor):
        gr.decimator_block.__init__(self,
            name="downsample",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32], decimation=factor)
        self.factor = factor-1

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = numpy.zeros(len(in0)/(self.factor+1))
        # <+signal processing here+>
        indx = 0
        print "processing ",in0
        print "current out vector: ",out
        for i in range(0,len(out)):
            print "index: ",indx," iteration: ",i
            out[i]=in0[indx]
            indx = indx+self.factor+1
        print out

        output_items[0][:] = out
        return len(output_items[0])
