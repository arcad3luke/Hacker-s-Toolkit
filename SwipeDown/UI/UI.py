#!/usr/bin/env python

import tkinter as tk
from SwipeDown.SwipeDown.Inject import sql, css
from SwipeDown.SwipeDown.Parameter import httpPollute
from SwipeDown.SwipeDown.Disrupt.Deny import deface
from SwipeDown.SwipeDown.Scan import google_scrape as webscrape

class UI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, padx=150, pady=150)
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        # Initialize the Menu
        SwipeDown = tk.LabelFrame(self, name='options')
        headerLabel = tk.Label(self, text='SwipeDown Options:')
        headerLabel.grid()

        SwipeDown.grid()

        # Web Scrape Option
        ScrapeLabel = tk.Label(self, name='_Web Scrape', text='Web Scraper')
        ScrapeLabel.grid()
        scrape = tk.Button(self, text='Google Scrape', command=f'{webscrape}')

        while scrape:
            tk.LabelFrame(self, name='_Scrape Log', text='Scrape Log')
        tk.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        scrape.grid()

        # Sql Injection
        sqlLabel = tk.Label(self, name='_Nmap Label', text='Nmap Scan')
        sqlLabel.grid()
        sqlButton = tk.Button(self, text='Scan', command=f'{sql}')

        while sqlButton:
            tk.LabelFrame(self, name='_SQL Log', text='SQL Log')
            tk.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        sqlButton.grid()

        # HTTP Parameter Pollution
        httpPolluteLabel = tk.Label(self, name='_Nmap Label', text='Nmap Scan')
        httpPolluteLabel.grid()
        httpPolluteButton = tk.Button(self, text='HTTP Parameter Pollution Test', command=f'{httpPollute}')

        while httpPolluteButton:
            tk.LabelFrame(self, name='_Pollution Log', text='Parameter Pollution Log')
            tk.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        httpPolluteButton.grid()

        # CSS Injection
        cssLabel = tk.Label(self, name='_Nmap Label', text='Nmap Scan')
        cssLabel.grid()
        cssButton = tk.Button(self, text='Scan', command=f'{css}')

        while cssButton:
            tk.LabelFrame(self, name='_CSS Log', text='CSS Injection Log')
            tk.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        cssButton.grid()

        # Deface
        defaceLabel = tk.Label(self, name='_Nmap Label', text='Nmap Scan')
        defaceLabel.grid()
        defaceButton = tk.Button(self, text='Deface', command=f'{deface}')

        while defaceButton:
            tk.LabelFrame(self, name='_Deface Log', text='Deface Log')
            tk.Button(self, text="Back", command=f'{self.tk_focusPrev()}')

        defaceButton.grid()

        quitButton = tk.Button(self, text="Quit", command=self.quit)
        quitButton.grid()

ui = UI()
ui.master.title('SwipeDown')
ui.mainloop()