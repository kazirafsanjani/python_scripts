#!/usr/bin/env python3
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 21:51:07 2022

@author: rafsanjani
"""



import webbrowser

url_france24 = 'https://www.youtube.com/watch?v=jNhh-OLzWlE'
url_meet = 'https://meet.google.com/xfp-ojtc-frj?pli=1&authuser=0'
url_yr_goteborg = 'https://www.yr.no/en/forecast/daily-table/2-2711537/Sweden/V%C3%A4stra%20G%C3%B6taland/Gothenburg%20Municipality/Gothenburg'


#webbrowser.get('firefox').open(url_france24)

import PySimpleGUI as sg

sg.theme('DarkAmber')
font = ('Arial, 20') 
layout = [ [sg.Text('Internet app')] ,
          [sg.Button('France24',font=font)],
          [sg.Button('Meet',font=font)],
          [sg.Button('Weather',font=font)],
          [sg.Button('Exit',font=font)]]

window = sg.Window('Internet browser', layout, margins=(300,250))

while True:
    event, values = window.read()
    if event == 'Exit':
        break
    
    if event == 'France24':
        webbrowser.get('firefox').open(url_france24)
        
    if event == 'Meet':
        webbrowser.get('google-chrome').open(url_meet)
        
    if event == 'Weather':
        webbrowser.get('firefox').open(url_yr_goteborg)
        
window.close()