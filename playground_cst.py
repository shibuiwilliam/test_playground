
# coding: utf-8

# In[226]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


# In[227]:


def get_nine_corners(edge=52, space=6):
    xy_dict = {}
    k = 0
    for i in range(3):
        for j in range(3):
            upperleft_x = (space)*(j+1)+(edge)*(j+0)
            upperleft_y = (space)*(i+1)+(edge)*(i+0)
            lowerright_x = (space)*(j+1)+(edge)*(j+1)
            lowerright_y = (space)*(i+1)+(edge)*(i+1)
            xy_dict[k] = ((upperleft_x,upperleft_y), (lowerright_x,lowerright_y))
            k += 1
    return xy_dict


# In[228]:


def draw_canvas(xy_dict, canvas_size=(180,180),  
                filled_with=(255,255,255), outline_color=(0,0,0)):
    canvas = Image.new("RGB", canvas_size, filled_with)
    draw_canvas = ImageDraw.Draw(canvas)
    for _,v in xy_dict.items():
        draw_canvas.rectangle(xy=(v[0], v[1]), 
                              outline=outline_color)
            
    return canvas, draw_canvas


# In[278]:


def draw_circle(canvas, draw_canvas, upperleft_xy, diameter,
                fill_color, outline_color):
    draw_canvas.ellipse(xy=(upperleft_xy, 
                            (upperleft_xy[0]+diameter, upperleft_xy[1]+diameter)),
                        fill=fill_color,
                        outline=outline_color)
    return canvas, draw_canvas


# In[279]:


def draw_circles(canvas, draw_canvas, edge, jpos, ipos,
                 diameter=10, in_space=2, 
                 fill_color=(255,255,255), outline_color=(0,0,0),
                 exclude_eight=False):
    k = 0
    for j in jpos:
        for i in ipos:
            if exclude_eight and k == 8:
                break
            canvas, draw_canvas = draw_circle(canvas, draw_canvas, 
                                              upperleft_xy=(xy_dict[k][0][0]+((i/2)*(edge-diameter)+in_space*(1-i)), 
                                                            xy_dict[k][0][1]+((j/2)*(edge-diameter)+in_space*(1-j))), 
                                              diameter=diameter,
                                              fill_color=fill_color,
                                              outline_color=outline_color)
            k += 1
    return canvas, draw_canvas


# In[280]:


edge_0 = 52
space_0 = 6
xy_dict_0 = get_nine_corners(edge=edge_0, space=space_0)
canvas_0, draw_canvas_0 = draw_canvas(xy_dict_0)
canvas_0, draw_canvas_0 = draw_circles(canvas_0, draw_canvas_0, edge_0,
                                       jpos=range(3), ipos=range(3),
                                       diameter=10, in_space=5, exclude_eight=True)
canvas_0


# In[281]:


edge_0 = 52
space_0 = 6
xy_dict_0 = get_nine_corners(edge=edge_0, space=space_0)
canvas_0, draw_canvas_0 = draw_canvas(xy_dict_0)
canvas_0, draw_canvas_0 = draw_circles(canvas_0, draw_canvas_0, edge_0,
                                       jpos=range(2,-1,-1), ipos=range(2,-1,-1),
                                       diameter=10, in_space=5, exclude_eight=True)
canvas_0


# In[285]:


def draw_ellipse(canvas, draw_canvas, upperleft_xy, diam_x, diam_y,
                fill_color, outline_color):
    draw_canvas.ellipse(xy=(upperleft_xy, 
                            (upperleft_xy[0]+diam_x, upperleft_xy[1]+diam_y)),
                        fill=fill_color,
                        outline=outline_color)
    return canvas, draw_canvas


# In[286]:


def draw_ellipses(canvas, draw_canvas, edge, diam_x, diam_y,
                  jpos, ipos,
                  diameter=10, in_space=2, 
                  fill_color=(255,255,255), outline_color=(0,0,0),
                  exclude_eight=False):
    k = 0
    for j in jpos:
        for i in ipos:
            if exclude_eight and k == 8:
                break
            canvas, draw_canvas = draw_ellipse(canvas, draw_canvas, 
                                              upperleft_xy=(xy_dict[k][0][0]+((i/2)*(edge-diam_x)+in_space*(1-i)), 
                                                            xy_dict[k][0][1]+((j/2)*(edge-diam_y)+in_space*(1-j))), 
                                              diam_x=diam_x, diam_y=diam_y,
                                              fill_color=fill_color,
                                              outline_color=outline_color)
            k += 1
    return canvas, draw_canvas


# In[288]:


edge_0 = 52
space_0 = 6
xy_dict_0 = get_nine_corners(edge=edge_0, space=space_0)
canvas_0, draw_canvas_0 = draw_canvas(xy_dict_0)
canvas_0, draw_canvas_0 = draw_ellipses(canvas_0, draw_canvas_0, edge_0,
                                        diam_x=10, diam_y=20,
                                        jpos=range(2,-1,-1), ipos=range(2,-1,-1),
                                        diameter=10, in_space=5, exclude_eight=True)
canvas_0

