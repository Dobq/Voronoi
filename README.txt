[Please turn on line wrapping.]

Welcome to Voronoi diagram generator.

Using this python code You are able to generate Voronoi diagrams through simple dialog box.

----INSTRUCTIONS----

Size - enter natural number n, generated graphics will be a n by n square of pixels; default is 500.

Cells - enter natural number, it is amount of cells to be generated; default is 100.

Colors - enter three colors in RGB ([r,g,b]) format, cells will be of randomly generated colors that are convex combinations of given colors. There is nice default pattern. 

Choose metric - 'Euclidean m.' stands for euclidean metric and 'Taxicab m.' stands for taxicab metric. Button of choosen metric is darker with white text, while other one is brighter with black text. Default metric is euclidean one.

Show points - this option allows You to show 'centers' of cells. Button is darker with white text when option is turned on, and brighter with black text in other case. By default this option is turned off.

Generate! - this button generates graphics following given instructions, generated graphics will be placed in folder where Voronoi.py file is stored.

----COMMENTS----

This program is probably not super-well optimalized currently: I implemented no known 'wise' algorithm to do the main job (like Fortune's algorithm for example) yet (current algorithm is quite naive), although I paid attention to avoid time-ineffective lines in most of the code. I do not recommend to enter big numbers in Size (>1000) and Cells (>400) boxes.

Strings of 8 random digits in names of generated .pngs are generated purely randomly and it is possible (10^(-8) chance) that generated file will overwrite old one if string is the same.

I noticed that whole program works fine even when in given [r,g,b] colors, numbers r, g, and b are any integers, not necessarily in [0,255] range (it seems to give some 'wilder' color patterns, I am going to look at the code in close future to find what is going on in this case), quite nice bug.








