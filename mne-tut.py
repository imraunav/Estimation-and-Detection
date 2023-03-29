import mne
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# plt.style.use('dark_background')
from plotly import tools
from plotly.graph_objs import Layout, YAxis, Scatter, Annotation, Annotations, Data, Figure, Marker, Font

filename = "dataset/chb01/chb01_03.edf"
raw= mne.io.read_raw_edf(filename, preload=True)

# print(raw.info)

raw.plot(highpass=20)
plt.show()
