#!/usr/bin/env python
import tkinter as tk
#from SwipeDown.SwipeDown.Inject import sql, css
#from SwipeDown.SwipeDown.Parameter import httpPollute
#from SwipeDown.SwipeDown.Disrupt.Deny import deface
from SwipeDown.SwipeDown.Scan import google_scrape as webscrape
#from SwipeDown.SwipeDown.Persist import pingClient as pc, pingServer as ps
import SwipeDown.SwipeDown.swipedown as sd

class UI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, padx=20, pady=40)
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        headerLabel = tk.Label(self, text='SwipeDown Options:')
        headerLabel.grid()

        SwipeDown = tk.LabelFrame(self, name='options')
        scrape = tk.Button(self, text='Web Scrape', command='webscrape')

        SwipeDown.grid()

        quitButton = tk.Button(self, text="Quit", command=self.quit)
        quitButton.grid()

ui = UI()
ui.master.title('SwipeDown')
ui.mainloop()