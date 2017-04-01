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

class soqpsk_demod(gr.basic_block):
    """
    docstring for block soqpsk_demod
    """

    # constant variables

    # Detection filter coefficients
    DF = (  0.010378066969709,
       0.023688987704657,
       0.009767134822858,
      -0.027017804469398,
      -0.089762303133391,
      -0.110346523809347,
      -0.051853991233850,
       0.154921158891652,
       0.568943123186263,
       0.792392871766106,
       0.792392871766106,
       0.568943123186263,
       0.154921158891652,
      -0.051853991233850,
      -0.110346523809347,
      -0.089762303133391,
      -0.027017804469398,
       0.009767134822858,
       0.023688987704657,
       0.010378066969709)

    #
    S4Di = numpy.zeros((18,),dtype=numpy.float32)
    S4Dq = numpy.zeros((18,),dtype=numpy.float32)


    def __init__(self, test):
        gr.basic_block.__init__(self,
            name="soqpsk_demod",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])
        self.set_history(1) # setting history to 1, means 0 history
        self.S4Di = numpy.zeros((18,),dtype=numpy.float32)
        self.S4Dq = numpy.zeros((18,),dtype=numpy.float32)



    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = 2*noutput_items #we get 2 samples per symbol
        # print "input items required: ", ninput_items_required[0]

    def general_work(self, input_items, output_items):
        print "input items: ",len(input_items[0])," output items",len(output_items[0])
        in0 = input_items[0]
        out = output_items[0]
        # print input_items[0]

        x = 0
        y = 0
        samples_per_buffer = 2
        for sample_idx in range(0,len(out)*2-2,2):
            # get the next two samples
            ri1 = numpy.real(in0[sample_idx+1]);
            rq1 = numpy.imag(in0[sample_idx+1]);
            ri = numpy.real(in0[sample_idx]);
            rq = numpy.imag(in0[sample_idx]);

            if sample_idx<=3:
                print "real values: ",ri," ",ri1
                print "imag values: ",rq," ",rq1
                print "array: ",self.S4Di
            # compute detection filter outputs
            x = self.DF[0] * (ri1 + self.S4Di[17]) \
                + self.DF[1] * (ri + self.S4Di[16]) \
                +self.DF[2] * (self.S4Di[0] + self.S4Di[15]) \
                +self.DF[3] * (self.S4Di[1] + self.S4Di[14]) \
                +self.DF[4] * (self.S4Di[2] + self.S4Di[13]) \
                +self.DF[5] * (self.S4Di[3] + self.S4Di[12]) \
                +self.DF[6] * (self.S4Di[4] + self.S4Di[11]) \
                +self.DF[7] * (self.S4Di[5] + self.S4Di[10]) \
                +self.DF[8] * (self.S4Di[6] + self.S4Di[9]) \
                +self.DF[9] * (self.S4Di[7] + self.S4Di[8])

            y =self.DF[0] * (rq1 + self.S4Dq[17]) \
                +self.DF[1] * (rq + self.S4Dq[16]) \
                +self.DF[2] * (self.S4Dq[0] + self.S4Dq[15]) \
                +self.DF[3] * (self.S4Dq[1] + self.S4Dq[14]) \
                +self.DF[4] * (self.S4Dq[2] + self.S4Dq[13]) \
                +self.DF[5] * (self.S4Dq[3] + self.S4Dq[12]) \
                +self.DF[6] * (self.S4Dq[4] + self.S4Dq[11]) \
                +self.DF[7] * (self.S4Dq[5] + self.S4Dq[10]) \
                +self.DF[8] * (self.S4Dq[6] + self.S4Dq[9]) \
                +self.DF[9] * (self.S4Dq[7] + self.S4Dq[8])

            out[sample_idx] = x+1j*y

            # if sample_idx==0:
                # print "sample is data type: ",type(sample)
            #     print "output is data type: ",type(out[0])
            #     print "input is data type: ",type(in0[0])
            # print "sample: ",numpy.real(out[sample_idx])," ",numpy.imag(out[sample_idx]), " made from x: ",x," and y: ",y
                # print "legit sample ",sample_idx,": ",out[sample_idx]

            #update the states
            self.S4Di[17] = self.S4Di[15];
            self.S4Di[16] = self.S4Di[14];
            self.S4Di[15] = self.S4Di[13];
            self.S4Di[14] = self.S4Di[12];
            self.S4Di[13] = self.S4Di[11];
            self.S4Di[12] = self.S4Di[10];
            self.S4Di[11] = self.S4Di[9];
            self.S4Di[10] = self.S4Di[8];
            self.S4Di[9] = self.S4Di[7];
            self.S4Di[8] = self.S4Di[6];
            self.S4Di[7] = self.S4Di[5];
            self.S4Di[6] = self.S4Di[4];
            self.S4Di[5] = self.S4Di[3];
            self.S4Di[4] = self.S4Di[2];
            self.S4Di[3] = self.S4Di[1];
            self.S4Di[2] = self.S4Di[0];
            self.S4Di[1] = ri;
            self.S4Di[0] = ri1;

            self.S4Dq[17] = self.S4Dq[15];
            self.S4Dq[16] = self.S4Dq[14];
            self.S4Dq[15] = self.S4Dq[13];
            self.S4Dq[14] = self.S4Dq[12];
            self.S4Dq[13] = self.S4Dq[11];
            self.S4Dq[12] = self.S4Dq[10];
            self.S4Dq[11] = self.S4Dq[9];
            self.S4Dq[10] = self.S4Dq[8];
            self.S4Dq[9] = self.S4Dq[7];
            self.S4Dq[8] = self.S4Dq[6];
            self.S4Dq[7] = self.S4Dq[5];
            self.S4Dq[6] = self.S4Dq[4];
            self.S4Dq[5] = self.S4Dq[3];
            self.S4Dq[4] = self.S4Dq[2];
            self.S4Dq[3] = self.S4Dq[1];
            self.S4Dq[2] = self.S4Dq[0];
            self.S4Dq[1] = rq;
            self.S4Dq[0] = rq1;





        print "out: ",out
        output_items[0][:] = out
        self.consume_each(len(output_items[0]))
        return len(output_items[0])
