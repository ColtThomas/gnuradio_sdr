#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Multipath Sim
# Generated: Fri Oct 20 18:36:17 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from scipy import fftpack
import math
import sip
import sys


class multipath_sim(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multipath Sim")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multipath Sim")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "multipath_sim")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.tap4 = tap4 = 0.6
        self.tap3 = tap3 = 0.6
        self.tap2 = tap2 = 0.5
        self.tap1 = tap1 = 0.25
        self.taps = taps = fftpack.ifftshift(fftpack.ifft([tap3, tap4, 1.0, tap1, tap2]))
        self.sps = sps = 4
        self.samp_rate = samp_rate = 32000
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self._tap4_range = Range(0, 1, 0.01, 0.6, 200)
        self._tap4_win = RangeWidget(self._tap4_range, self.set_tap4, "tap4", "slider", float)
        self.top_grid_layout.addWidget(self._tap4_win, 0,14,1,1)
        self._tap3_range = Range(0, 1, 0.01, 0.6, 200)
        self._tap3_win = RangeWidget(self._tap3_range, self.set_tap3, "tap3", "slider", float)
        self.top_grid_layout.addWidget(self._tap3_win, 0,13,1,1)
        self._tap2_range = Range(0, 1, 0.01, 0.5, 200)
        self._tap2_win = RangeWidget(self._tap2_range, self.set_tap2, "tap2", "slider", float)
        self.top_grid_layout.addWidget(self._tap2_win, 0,12,1,1)
        self._tap1_range = Range(0, 1, 0.01, 0.25, 200)
        self._tap1_win = RangeWidget(self._tap1_range, self.set_tap1, "tap1", "slider", float)
        self.top_grid_layout.addWidget(self._tap1_win, 0,11,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-100, -20)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["Multipath", "AWGN", "", "", "",
                  "", "", "", "", ""]
        widths = [2, 2, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,10)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.0,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(taps),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_freq_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "multipath_sim")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_tap4(self):
        return self.tap4

    def set_tap4(self, tap4):
        self.tap4 = tap4
        self.set_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_tap3(self):
        return self.tap3

    def set_tap3(self, tap3):
        self.tap3 = tap3
        self.set_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_tap2(self):
        return self.tap2

    def set_tap2(self, tap2):
        self.tap2 = tap2
        self.set_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_tap1(self):
        return self.tap1

    def set_tap1(self, tap1):
        self.tap1 = tap1
        self.set_taps(fftpack.ifftshift(fftpack.ifft([self.tap3, self.tap4, 1.0, self.tap1, self.tap2])))

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0.set_taps((self.taps))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity


def main(top_block_cls=multipath_sim, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
