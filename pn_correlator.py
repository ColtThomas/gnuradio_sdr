#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
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

class pn_correlator(gr.basic_block):
    """
    docstring for block pn_correlator
    """
    pnLength = 127
    def __init__(self):
        gr.basic_block.__init__(self,
            name="pn_correlator",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])


    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items - self.pnLength - 1
            print "input items required: ",ninput_items_required[i]
            print "output items required: ",noutput_items

    def getPN(self):
        # Generates the maximal-length shift register
        # sequence based on X^7 + X^6 + 1
        # See "Linear Feedback Shift Register" in Wikipedia

        pn = numpy.zeros(127)
        STATE = numpy.zeros(7)
        STATE[0] = 1

        for idx in range(0,126):

            ### generate output
            pn[idx] = STATE[0]

            # update states
            STATE[0] = STATE[1]
            STATE[1] = STATE[2]
            STATE[2] = STATE[3]
            STATE[3] = STATE[4]
            STATE[4] = STATE[5]
            STATE[5] = (STATE[6]+pn[idx])%2 # basically acts as an xor
            STATE[6] = pn[idx]
            # print STATE

        return pn

    # def sum(self,a,b)

    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        pn = self.getPN()
        outputSize = len(in0) + len(pn)-1 # remember pn is a numpy array; get the column count
        out = numpy.zeros(outputSize)

        abits = 2*in0 - 1 # converts 0 -> -1, 1 -> +1
        apn = 2*pn-1
        # perform an autocorrelation of the input bits with the pn sequence

        # print "pn sequence size: ",len(apn[0:len(apn)+len(abits)-(len(abits)+1)-1:1])
        # print "bits size: ",len(abits[len(abits)+1-len(pn)::1])
        for idx in range(0,len(pn)-1): # iterate over 126 before totally overlapping the pn sequence
            out[idx] = sum(numpy.multiply(abits[0:idx:1],pn[len(pn)-idx::1])) # numpy.multiply is equivalent to .* in matlab
        for idx in range(len(pn),len(abits)):
            out[idx] = sum(numpy.multiply(abits[idx-len(pn):idx:1],apn[::1]))
        for idx in range(len(abits)+1,len(abits)+len(pn)-1):
            out[idx-1] = sum(numpy.multiply(abits[idx-len(pn)::1],apn[0:len(apn)+len(abits)-idx:1]))
        # print "out: ",out
        # for idx in range(0,len(pn)-2):
        #     out[idx] = sum(numpy.multiply(abits(0,idx),pn(end-idx,end)));
        # for idx in range(len(pn)-1,len(bits)):
        #     out[idx] = sum(numpy.multiply(abits(idx-len(pn)+1,idx),apn));
        # for idx in range(len(bits),len(bits)+len(pn)-2):
        #     out[idx] = sum(numpy.multiply(abits(idx-len(pn)+1,end),apn(1,end+len(abits)-idx)));
        # print "PN sequence: ",self.getPN()

        # out[:] = numpy.convolve(apn[::-1],abits)
        # print out[0:30:1]
        # consume(0, len(input_items[0]))
        print "Size of the output: ",len(out)
        # output_items[0][:] = out
        self.consume_each(len(input_items[0]))
        return len(output_items[0])
