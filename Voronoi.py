# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:01:55 2022

@author: dell
"""

#imports
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
from PIL import Image
from numpy import zeros,uint8
import random as ra
from string import digits

#setting some default values
metric=0
points=0

#setting some constants
wwidth=12
#phi=1.618034 #golden ratio, unused but nice
rho=1.324718 #plastic ratio

#main part
def voronoi():

    #what to do, assuming input is correct
    try:

##############################################################################        

        #getting input from GUI
        pxl=int(size_entry.get())
        n=int(cells_entry.get())
        colors=[color_0_entry.get().strip('][').split(','),color_1_entry.get().strip('][').split(','),color_2_entry.get().strip('][').split(',')]
        #spooky line above - among other things - transforms '[x,y,z]' to ['x','y','z']
        #(something.get() output is a string)

        #function that creates random convex combinations of given colors
        def mix(arg):
            w=[(1-ra.random())**rho for i in arg] #random weights
            ww=sum(w)
            col=[]
            #getting values of R, G and B
            for i in range(3):
                val=0
                #getting value of R, G or B
                for j in range(len(arg)):
                    val=val+int(arg[j][i])*(w[j]/ww)
                col.append(val)
            return col
        #**rho is here for subtle cosmetical purposes (the bigger value of rho is, the smaller probability of getting "average" color is)

        #creating list of random colors, one color for each cell
        COLLIST=[mix(colors) for i in range(n)]
        #if "Show points" option is active, colors used for coloring points are added
        if points==1:
            COLLIST=COLLIST+[[0,0,0],[220,215,128]]

##############################################################################

        #function counting distances of points of form (X[i],Y[i]) from point (x,y)
        def dists(x,y,X,Y):
            #euclidean metric case (square root omitted)
            if metric==0:
                D=[(x-X[i])**2+(y-Y[i])**2 for i in range(n)]
            #taxicab metric case
            else:
                D=[abs(x-X[i])+abs(y-Y[i]) for i in range(n)]
            return D

        #function returning index of closest point of the form (X[i],Y[i])
        if points==0:
            def cloind(x,y,X,Y):
                D=dists(x,y,X,Y)              
                return D.index(min(D))
        #when "Show points" option is active, if distance to the point is very small, we're denoting it
        else:
            def cloind(x,y,X,Y):
                D=dists(x,y,X,Y)              
                mind=min(D)
                if mind>=2:
                    return D.index(mind)
                elif not mind==0:
                    return n
                else:
                    return n+1

##############################################################################

        #function transforming list of lists of [R,G,B]s to the array (needed to use Image.fromarray())
        def arrayRGB(L):
            l=len(L) #(works for squares, what is our case)
            data=zeros((l,l,3),dtype=uint8)
            for i in range(l):
                for j in range(l):
                    data[i,j]=COLLIST[L[i][j]]
            return data

##############################################################################

        #function creating .png
        def graf(M):
            cod=''.join(ra.choices(digits,k=8))
            img=Image.fromarray(arrayRGB(M),'RGB')
            print(cod) #print digits of new .png
            img.save('voronoi_diag_'+cod+'.png')

##############################################################################

        #randomly set coordinates of points
        X=[ra.randint(0, pxl-1) for i in range(n)]
        Y=[ra.randint(0, pxl-1) for i in range(n)]

        #calculate color of each pixel
        M=[[cloind(i,j,X,Y) for j in range(pxl)] for i in range(pxl)]

        #make .png
        graf(M)

##############################################################################

    #what to do, assuming input is wrong
    except:
        tkinter.messagebox.showinfo('Error','Wrong input')

##############################################################################

#GUI

#function controlling colors of buttons according to chosen metric
def metric_color():
    if metric==0:
        euclidean_button.config(bg='#14555F',fg='#FFFFFF')
        taxicab_button.config(bg='#B38099',fg='#000000')
    else:
        euclidean_button.config(bg='#8AAAAF',fg='#000000')
        taxicab_button.config(bg='#660033',fg='#FFFFFF')

#function setting value of "metric" variable and calling to set colors of buttons
def metric_i(m):
    global metric
    metric=m
    metric_color()

#function controlling colors of buttons according to "Show points" option
def points_color():
    if points==0:
        points_button.config(bg='#DCD780',fg='#000000')
    else:
        points_button.config(bg='#B8AE00',fg='#FFFFFF')

#function changing value of "points" variable and calling to change colors of button
def points_i():
    global points
    points=1-points
    points_color()

#new window
window=tk.Tk()
window.title('Voronoi diagram generator')
frame=tk.Frame(master=window,bg="black",padx=10)
frame.option_add('*font','lucida 20 bold')
frame.pack()

#title label
name_label=tk.Label(frame,text='Voronoi diagram generator',width=24)
name_label.grid(row=0,column=0,columnspan=2,ipady=2,pady=2,padx=5)
name_label.config(bg='#DCD780')

#size label
size_label=tk.Label(frame,text='Size:',width=wwidth-1)
size_label.grid(row=1,column=0,columnspan=1,ipady=2,pady=2,padx=5)
#size entry
size_entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=wwidth)
size_entry.insert(0,string='500')
size_entry.grid(row=1,column=1,columnspan=1,ipady=2,pady=2,padx=5)

#cells label
cells_label=tk.Label(frame,text='Cells:',width=wwidth-1)
cells_label.grid(row=2,column=0,columnspan=1,ipady=2,pady=2,padx=5)
#cells entry
cells_entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=wwidth)
cells_entry.insert(0,string='100')
cells_entry.grid(row=2,column=1,columnspan=1,ipady=2,pady=2,padx=5)

#labels and entries of colors

color_0_label=tk.Label(frame,text='Color 0:',width=wwidth-1)
color_0_label.grid(row=3,column=0,columnspan=1,ipady=2,pady=2,padx=5)
color_0_entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=wwidth)
color_0_entry.insert(0,string='[255,255,255]')
color_0_entry.grid(row=3,column=1,columnspan=1,ipady=2,pady=2,padx=5)

color_1_label=tk.Label(frame,text='Color 1:',width=wwidth-1)
color_1_label.grid(row=4,column=0,columnspan=1,ipady=2,pady=2,padx=5)
color_1_entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=wwidth)
color_1_entry.insert(0,string='[20,85,95]')
color_1_entry.grid(row=4,column=1,columnspan=1,ipady=2,pady=2,padx=5)

color_2_label=tk.Label(frame,text='Color 2:',width=wwidth-1)
color_2_label.grid(row=5,column=0,columnspan=1,ipady=2,pady=2,padx=5)
color_2_entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=wwidth)
color_2_entry.insert(0,string='[102,0,51]')
color_2_entry.grid(row=5,column=1,columnspan=1,ipady=2,pady=2,padx=5)

#buttons allowing to set metric
euclidean_button=tk.Button(frame,text='Euclidean m.',width=wwidth-1,command=lambda: metric_i(0))
taxicab_button=tk.Button(frame,text='Taxicab m.',width=wwidth-1,command=lambda: metric_i(1))
euclidean_button.grid(row=6,column=0,columnspan=1,ipady=2,pady=2,padx=5)
taxicab_button.grid(row=6,column=1,columnspan=1,ipady=2,pady=2,padx=5)
euclidean_button.config(bg='#14555F',fg='#FFFFFF')
taxicab_button.config(bg='#B38099')

#button allowing to set "Show points" option
points_button=tk.Button(frame,text='Show points',width=wwidth-1,command=lambda: points_i())
points_button.grid(row=7,column=0,columnspan=1,ipady=2,pady=2,padx=5)
points_button.config(bg='#DCD780')

#button allowing to launch program
generate_button=tk.Button(frame, text='Generate!', width=wwidth-1, command=lambda: voronoi(),activebackground='#B8AE00',activeforeground='#FFFFFF')
generate_button.grid(row=7,column=1,columnspan=1,ipady=2,pady=2,padx=5)
generate_button.config(bg='#DCD780')

window.mainloop()
