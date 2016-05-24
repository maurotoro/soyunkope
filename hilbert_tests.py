# -*- coding: utf-8 -*-
"""
Created on Thu May 19 22:27:26 2016
    Code from scipy.signal docs,
    should help to understand instantaneus phase
        https://github.com/maurotoro/soyunkope
@author: soyunkope
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp

duration = 1.0
fs = 400.0
samples = int(fs*duration)
t = np.arange(samples) / fs

signal = chirp(t, 20.0, t[-1], 100.0)
signal *= (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t))
signal = np.sin(2*np.pi*5*t)
analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = np.diff(instantaneous_phase) / (2.0*np.pi) * fs
analytic_phase =  np.arctan2(np.imag(analytic_signal), signal)


# FFT analysis
DFT = np.fft.fft(signal)


fig = plt.figure('Chirp and Hilbert')
ax0 = fig.add_subplot(211)
ax0.plot(t, signal, label='signal')
ax0.plot(t, amplitude_envelope, label='envelope')
ax0.plot(t, (analytic_signal), '--r', label='analytic')
ax0.legend()
ax1 = fig.add_subplot(212, sharex=ax0)
ax1.plot(t, analytic_phase, t, instantaneous_phase)
#ax2 = fig.add_subplot(213)
#ax2.plot(t[1:], instantaneous_frequency )
#ax2.set_xticklabels(np.linspace(0,duration,num=5))
#ax2.set_xlabel("time in seconds")
#ax3 = fig.add_subplot(212)
