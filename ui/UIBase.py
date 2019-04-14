# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class UIFrame
###########################################################################

class UIFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 227,246 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		box_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.text_autoClicker = wx.StaticText( self, wx.ID_ANY, u"AutoClicker", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_autoClicker.Wrap( -1 )
		self.text_autoClicker.SetFont( wx.Font( 14, 74, 90, 92, False, "Verdana" ) )
		
		box_sizer.Add( self.text_autoClicker, 0, wx.ALL, 5 )
		
		delay_module = wx.BoxSizer( wx.HORIZONTAL )
		
		self.delay_text = wx.StaticText( self, wx.ID_ANY, u"Delay:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.delay_text.Wrap( -1 )
		delay_module.Add( self.delay_text, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.input_delay = wx.TextCtrl( self, wx.ID_ANY, u"1000.0", wx.Point( 0,-1 ), wx.Size( 100,-1 ), wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
		self.input_delay.SetMaxLength( 15 ) 
		delay_module.Add( self.input_delay, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		timeunit_choiceChoices = [ u"ms", u"s", u"m", u"h" ]
		self.timeunit_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, timeunit_choiceChoices, 0 )
		self.timeunit_choice.SetSelection( 0 )
		self.timeunit_choice.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.timeunit_choice.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		delay_module.Add( self.timeunit_choice, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		box_sizer.Add( delay_module, 1, wx.EXPAND, 5 )
		
		button_module = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_text = wx.StaticText( self, wx.ID_ANY, u"Button:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_text.Wrap( -1 )
		button_module.Add( self.button_text, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		button_select_choiceChoices = [ u"Left", u"Right", u"Middle" ]
		self.button_select_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, button_select_choiceChoices, 0 )
		self.button_select_choice.SetSelection( 0 )
		button_module.Add( self.button_select_choice, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.check_double = wx.CheckBox( self, wx.ID_ANY, u"Double", wx.DefaultPosition, wx.DefaultSize, 0 )
		button_module.Add( self.check_double, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		box_sizer.Add( button_module, 1, wx.EXPAND, 5 )
		
		buttons_module = wx.GridSizer( 0, 2, 0, 0 )
		
		self.button_start = wx.ToggleButton( self, wx.ID_ANY, u"Active", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttons_module.Add( self.button_start, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.button_exit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttons_module.Add( self.button_exit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.button_edit = wx.Button( self, wx.ID_ANY, u"Hotkeys", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttons_module.Add( self.button_edit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.button_credits = wx.Button( self, wx.ID_ANY, u"Credits", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttons_module.Add( self.button_credits, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		box_sizer.Add( buttons_module, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( box_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.quit_program )
		self.input_delay.Bind( wx.EVT_TEXT, self.time_text_change )
		self.input_delay.Bind( wx.EVT_TEXT_ENTER, self.time_text_enter )
		self.button_start.Bind( wx.EVT_TOGGLEBUTTON, self.enable_clicker )
		self.button_exit.Bind( wx.EVT_BUTTON, self.quit_program )
		self.button_credits.Bind( wx.EVT_BUTTON, self.show_credits )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def quit_program( self, event ):
		event.Skip()
	
	def time_text_change( self, event ):
		event.Skip()
	
	def time_text_enter( self, event ):
		event.Skip()
	
	def enable_clicker( self, event ):
		event.Skip()
	
	
	def show_credits( self, event ):
		event.Skip()
	

###########################################################################
## Class UIHotkeys
###########################################################################

class UIHotkeys ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 165,144 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		box_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.text_hotkeys = wx.StaticText( self, wx.ID_ANY, u"Hotkeys", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_hotkeys.Wrap( -1 )
		self.text_hotkeys.SetFont( wx.Font( 14, 74, 90, 92, False, "Verdana" ) )
		
		box_sizer.Add( self.text_hotkeys, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Toggle on/off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer13.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALIGN_TOP|wx.ALL, 5 )
		
		self.m_toggleBtn7 = wx.ToggleButton( self, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_toggleBtn7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_done = wx.Button( self, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.button_done, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		
		box_sizer.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( box_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_done.Bind( wx.EVT_BUTTON, self.done )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def done( self, event ):
		event.Skip()
	

###########################################################################
## Class UICredits
###########################################################################

class UICredits ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		box_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.credit_credit = wx.StaticText( self, wx.ID_ANY, u"Made by Alve Svarén", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.credit_credit.Wrap( -1 )
		box_sizer.Add( self.credit_credit, 0, wx.ALL, 5 )
		
		self.button_done = wx.Button( self, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		box_sizer.Add( self.button_done, 0, wx.ALL, 5 )
		
		
		self.SetSizer( box_sizer )
		self.Layout()
		box_sizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_done.Bind( wx.EVT_BUTTON, self.close_credits )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close_credits( self, event ):
		event.Skip()
	

