#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: streams I/Q samples
# Author: Josh Bailey
# GNU Radio version: 3.8.1.0

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import fcdproplus

class FCM_IQ_streamer(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "streams I/Q samples")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 192000

        ##################################################
        # Blocks
        ##################################################
        self.fcdproplus_fcdproplus_0 = fcdproplus.fcdproplus('',1000)
        self.fcdproplus_fcdproplus_0.set_lna(1)
        self.fcdproplus_fcdproplus_0.set_mixer_gain(0)
        self.fcdproplus_fcdproplus_0.set_if_gain(0)
        self.fcdproplus_fcdproplus_0.set_freq_corr(0)
        self.fcdproplus_fcdproplus_0.set_freq(101300)
        self.blocks_tcp_server_sink_0 = blocks.tcp_server_sink(gr.sizeof_char*1, '0.0.0.0', 1234, True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(128)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_float*1, 1)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(128)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_interleave_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_interleave_0, 1))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_tcp_server_sink_0, 0))
        self.connect((self.blocks_interleave_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.fcdproplus_fcdproplus_0, 0), (self.blocks_complex_to_float_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate



def main(top_block_cls=FCM_IQ_streamer, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
