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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from matched_filter import matched_filter

class qa_matched_filter (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data = (0,1,2,3,0,3,2,1)
        expected_result = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        src = blocks.vector_source_f (src_data)
        mf = matched_filter(2)
        snk = blocks.vector_sink_c()
        self.tb.connect(src,mf)
        self.tb.connect(mf,snk)
        self.tb.run()
        result_data = snk.data()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)

if __name__ == '__main__':
    gr_unittest.run(qa_matched_filter, "qa_matched_filter.xml")
