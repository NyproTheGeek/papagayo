# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.3.5.1 on Tue Apr 19 20:18:14 2005

# Papagayo, a lip-sync tool for use with Lost Marble's Moho
# Copyright (C) 2005 Mike Clifton
# Contact information at http://www.lostmarble.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import wx

# begin wxGlade: dependencies
# end wxGlade

class PronunciationDialog(wx.Dialog):
	def __init__(self, parent, phoneme_set):
		# begin wxGlade: PronunciationDialog.__init__
		kwds["style"] = wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		self.wordLabel = wx.StaticText(self, wx.ID_ANY, _("Break down the word:"), style=wx.ALIGN_CENTER)
		global ID_AI; ID_AI = wx.NewId()
		self.button_3 = wx.Button(self, ID_AI, _("AI"))
		global ID_O; ID_O = wx.NewId()
		self.button_4 = wx.Button(self, ID_O, _("O"))
		global ID_E; ID_E = wx.NewId()
		self.button_5 = wx.Button(self, ID_E, _("E"))
		global ID_U; ID_U = wx.NewId()
		self.button_6 = wx.Button(self, ID_U, _("U"))
		global ID_ETC; ID_ETC = wx.NewId()
		self.button_7 = wx.Button(self, ID_ETC, _("etc"))
		global ID_L; ID_L = wx.NewId()
		self.button_8 = wx.Button(self, ID_L, _("L"))
		global ID_WQ; ID_WQ = wx.NewId()
		self.button_9 = wx.Button(self, ID_WQ, _("WQ"))
		global ID_MBP; ID_MBP = wx.NewId()
		self.button_10 = wx.Button(self, ID_MBP, _("MBP"))
		global ID_FV; ID_FV = wx.NewId()
		self.button_11 = wx.Button(self, ID_FV, _("FV"))
		self.phonemeCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
		self.button_1 = wx.Button(self, wx.ID_OK, _("OK"))
		self.button_2 = wx.Button(self, wx.ID_CANCEL, _("Cancel"))

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

		# Connect event handlers
		for phoneme in phoneme_set:
			if phoneme != 'rest':
				wx.EVT_BUTTON(self, phoneme_ids[phoneme], self.OnPhonemeClick)

	def __set_properties(self):
		# begin wxGlade: PronunciationDialog.__set_properties
		self.SetTitle(_("Unknown Word"))
		self.button_1.SetDefault()
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: PronunciationDialog.__do_layout
		sizer_11 = wx.BoxSizer(wx.VERTICAL)
		sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
		grid_sizer_1 = wx.GridSizer(3, 3, 4, 4)
		sizer_11.Add(self.wordLabel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 4)
		grid_sizer_1.Add(self.button_3, 0, wx.FIXED_MINSIZE, 0)
		grid_sizer_1.Add(self.button_4, 0, wx.FIXED_MINSIZE, 0)
		grid_sizer_1.Add(self.button_5, 0, wx.FIXED_MINSIZE, 0)
		grid_sizer_1.Add(self.button_6, 0, wx.FIXED_MINSIZE, 0)
		grid_sizer_1.Add(self.button_7, 0, wx.FIXED_MINSIZE, 0)
		grid_sizer_1.Add(self.button_8, 0, wx.FIXED_MINSIZE, 0)
		grid_sizer_1.Add(self.button_9, 0, wx.FIXED_MINSIZE, 0)
		grid_sizer_1.Add(self.button_10, 0, wx.FIXED_MINSIZE, 0)
		grid_sizer_1.Add(self.button_11, 0, wx.FIXED_MINSIZE, 0)
		sizer_11.Add(grid_sizer_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)
		sizer_11.Add(self.phonemeCtrl, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 4)
		sizer_12.Add(self.button_1, 0, wx.FIXED_MINSIZE, 0)
		sizer_12.Add((20, 20), 0, wx.FIXED_MINSIZE, 0)
		sizer_12.Add(self.button_2, 0, wx.FIXED_MINSIZE, 0)
		sizer_11.Add(sizer_12, 0, wx.ALIGN_RIGHT | wx.ALL, 4)
		self.SetSizer(sizer_11)
		sizer_11.Fit(self)
		self.Layout()
		self.Centre()
		# end wxGlade

	def AddPhoneme(self, phoneme):
		text = "%s %s" % (self.phonemeCtrl.GetValue().strip(), phoneme)
		self.phonemeCtrl.SetValue(text.strip())

	def OnPhonemeClick(self, event):
		phoneme = event.GetEventObject().GetLabel()
		text = "%s %s" % (self.phonemeCtrl.GetValue().strip(), phoneme)
		self.phonemeCtrl.SetValue(text.strip())

# end of class PronunciationDialog


