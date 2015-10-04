# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 21:05:56 2015

@author: rwb27
"""

from nplab.instrument import Instrument
from nplab.utils.gui import qt, qtgui
import traits, traitsui
from traits.api import HasTraits, Property, Instance, Float, String, Button
import traitsui
from traitsui.api import View, Item, HGroup, VGroup

class InstrumentA(Instrument):
    def get_qt_ui(self):
        l = qtgui.QLabel()
        l.setText("InstrumentA Interface")
        return l
    def __del__(self):
        print "deleted"
        
class InstrumentB(Instrument, HasTraits):
    description = String("Description...")
    traits_view = View(Item(name="description"))
    
if __name__ == "__main__":
    a = InstrumentA()
    b = InstrumentB()