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
import math
from gnuradio import gr

class matched_filter(gr.interp_block):
    """
    docstring for block matched_filter
    """
    energy = 3/(math.sqrt(2))
    factor = 0
    def __init__(self,upsample):
        gr.interp_block.__init__(self,
            name="matched_filter",
            in_sig=[numpy.float32],
            out_sig=[numpy.complex64],
            interp = upsample)
        self.factor = upsample-1 # can you throw an error if is lower than 1?

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = numpy.zeros((self.factor+1)*len(in0),dtype=numpy.complex64)

        # just init both parts of the modulated signal
        inphase = numpy.zeros((self.factor+1)*len(in0))
        quadrature = numpy.zeros((self.factor+1)*len(in0))
        indx = 0 # keeps track for the upsampling
        # print in0
        # print "energy: ",self.energy
        # we are converting a symbol into a modulated signal
        for i in range(0,len(in0)):

            # The lookup table [1 -1 1 -1]*3/sqrt(2)
            #u upsamplimg happens as we increment
            if(in0[i]==0):
                inphase[indx]= 1*self.energy
                quadrature[indx]= 1*self.energy
            elif (in0[i]==1):
                inphase[indx]= -1*self.energy
                quadrature[indx]= 1*self.energy
            elif (in0[i]==2):
                inphase[indx]= 1*self.energy
                quadrature[indx]= -1*self.energy
            elif (in0[i]==3):
                inphase[indx]= -1*self.energy
                quadrature[indx]= -1*self.energy
            else:
                inphase[indx]=0
                quadrature[indx]= 0

            indx = indx+self.factor+1

            # The mixing
        # print "real: ",len(inphase)," imag: ",len(quadrature)," output: ",len(out)," expecting: ",len(output_items[0])
        out.real = inphase
        out.imag = quadrature
        # print out
        output_items[0][:] = out
        return len(output_items[0])
