# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:45:51 2016

@author: soyunkope
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy


def make_frame_mpl(t):
    ax.figure.set_size_inches(4, 4)
    ax.axis('off')
    ax.set_axis_bgcolor('black')
    ax.view_init(elev=elevation, azim=start_ang+delta_ang*t)
    return mplfig_to_npimage(fig)


def make_black_frame(t):
    axB.axis('off')
    return mplfig_to_npimage(figB)

def make_x_frame(t):
    axX.axis('off')
    return mplfig_to_npimage(figX)

fig = plt.figure(figsize=(4, 4), facecolor='black')
ax = fig.add_subplot(111, projection='3d')
                     
figB, axB = plt.subplots(1, figsize=(4, 4), facecolor=(0, 0, 0))

black = np.zeros([3, 3, 3])
axB.imshow(black)
axB.axis('off')

figX, axX = plt.subplots(1, figsize=(4, 4), facecolor=(0, 0, 0))
upD = np.arange(0, 10)
dnD = np.arange(9, -1, -1)
axX.plot(upD, upD, 'w-', upD, dnD, 'w-')
axB.axis('off')

duration = 2
delta_ang = 360/duration
elevation = 20  # Elevation of view
X, Y, Z = axes3d.get_test_data()
ax.plot_surface(X, Y, Z, cmap=cm.jet)

for i in np.arange(0, 360, 90):
    start_ang = i
    animation = mpy.VideoClip(make_frame_mpl, duration=duration)
    fname = "sinc_mpl_"+str(int(i))+".gif"
    animation.write_gif(fname, fps=20)

blackanim = mpy.VideoClip(make_black_frame, duration=duration)
blackanim.write_gif("sinc_mpl_black.gif", fps=20)

xanim = mpy.VideoClip(make_x_frame, duration=duration)
xanim.write_gif("sinc_mpl_x.gif", fps=20)
clip0 = mpy.VideoFileClip("sinc_mpl_0.gif")
clip1 = mpy.VideoFileClip("sinc_mpl_90.gif").rotate(90)
clip2 = mpy.VideoFileClip("sinc_mpl_180.gif").rotate(180)
clip3 = mpy.VideoFileClip("sinc_mpl_270.gif").rotate(-90)
clipB = mpy.VideoFileClip("sinc_mpl_black.gif")
clipX = mpy.VideoFileClip("sinc_mpl_x.gif")
hologram = mpy.clips_array([[clipB, clip2, clipB],
                            [clip3, clipX, clip1],
                            [clipB, clip0, clipB]])

hologram.write_gif("hologram_test_black.gif", fps=20)
