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
    S4Di = numpy.zeros((18,),dtype=numpy.float64)
    S4Dq = numpy.zeros((18,),dtype=numpy.float64)

    def __init__(self, test):
        gr.basic_block.__init__(self,
            name="soqpsk_demod",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])
        self.set_history(1) # setting history to 1, means 0 history
        self.S4Di = numpy.zeros((18,),dtype=numpy.float64)
        self.S4Dq = numpy.zeros((18,),dtype=numpy.float64)

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items*2

    def general_work(self, input_items, output_items):
        print "input items: ",len(input_items[0])," output items",len(output_items[0])
        in0 = input_items[0]
        out = output_items[0]
        # print input_items[0]

        x = 0
        y = 0
        samples_per_buffer = 2
        print "length of output: ",len(out)
        # print "memory: ",self.S4Di

        output_idx = 0
        for sample_idx in range(0,len(out)*2,2):
            print "index: ",sample_idx
            # get the next two samples

            # if we only have one item to compute, we need to let ri1,rq1=0
            if len(out)<=1:
                ri1=0
                rq1 = 0
            else:
                ri1 = numpy.real(in0[sample_idx+1]);
                rq1 = numpy.imag(in0[sample_idx+1]);
            ri = numpy.real(in0[sample_idx]);
            rq = numpy.imag(in0[sample_idx]);

            # if sample_idx<=3:
                # print "real values: ",ri," ",ri1
                # print "imag values: ",rq," ",rq1
                # print "array: ",self.S4Di
            # compute detection filter outputs

            # no history function

            print "===> S4Di shifting by two: ", self.S4Di
            print "input: ",ri1," , ",ri
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

            # =================================================
            #           history function implementation
            # =================================================

            # x = self.DF[0] * (numpy.real(in0[sample_idx+19]) + numpy.real(in0[sample_idx])) \
            #     + self.DF[1] * (numpy.real(in0[sample_idx+18]) + numpy.real(in0[sample_idx+1])) \
            #     +self.DF[2] * (numpy.real(in0[sample_idx+17]) + numpy.real(in0[sample_idx+2])) \
            #     +self.DF[3] * (numpy.real(in0[sample_idx+16]) + numpy.real(in0[sample_idx+3])) \
            #     +self.DF[4] * (numpy.real(in0[sample_idx+15]) + numpy.real(in0[sample_idx+4])) \
            #     +self.DF[5] * (numpy.real(in0[sample_idx+14]) + numpy.real(in0[sample_idx+5])) \
            #     +self.DF[6] * (numpy.real(in0[sample_idx+13]) + numpy.real(in0[sample_idx+6])) \
            #     +self.DF[7] * (numpy.real(in0[sample_idx+12]) + numpy.real(in0[sample_idx+7])) \
            #     +self.DF[8] * (numpy.real(in0[sample_idx+11]) + numpy.real(in0[sample_idx+8])) \
            #     +self.DF[9] * (numpy.real(in0[sample_idx+10]) + numpy.real(in0[sample_idx+9]))
            #
            # y = self.DF[0] * (numpy.imag(in0[sample_idx+19]) + numpy.imag(in0[sample_idx])) \
            #     + self.DF[1] * (numpy.imag(in0[sample_idx+18]) + numpy.imag(in0[sample_idx+1])) \
            #     +self.DF[2] * (numpy.imag(in0[sample_idx+17]) + numpy.imag(in0[sample_idx+2])) \
            #     +self.DF[3] * (numpy.imag(in0[sample_idx+16]) + numpy.imag(in0[sample_idx+3])) \
            #     +self.DF[4] * (numpy.imag(in0[sample_idx+15]) + numpy.imag(in0[sample_idx+4])) \
            #     +self.DF[5] * (numpy.imag(in0[sample_idx+14]) + numpy.imag(in0[sample_idx+5])) \
            #     +self.DF[6] * (numpy.imag(in0[sample_idx+13]) + numpy.imag(in0[sample_idx+6])) \
            #     +self.DF[7] * (numpy.imag(in0[sample_idx+12]) + numpy.imag(in0[sample_idx+7])) \
            #     +self.DF[8] * (numpy.imag(in0[sample_idx+11]) + numpy.imag(in0[sample_idx+8])) \
            #     +self.DF[9] * (numpy.imag(in0[sample_idx+10]) + numpy.imag(in0[sample_idx+9]))

            # =================================================
            #                   Testing MF
            # =================================================
            # out[output_idx] = x+1j*y
            # output_idx = output_idx+1



            # =================================================
            #          Phase and Timing error correction
            # =================================================



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
