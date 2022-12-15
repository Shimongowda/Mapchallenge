#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda config --prepend channels conda-forge
conda create -n ox --strict-channel-priority osmnx


# In[2]:


conda install -c conda-forge osmnx


# In[3]:


import osmnx as ox


# In[4]:


# To make maps
import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.lines import Line2D

# To add text and a border to the map
from PIL import Image, ImageOps, ImageColor, ImageFont, ImageDraw 


# In[5]:


conda install -c anaconda networkx


# In[6]:


conda install geopandas


# In[7]:


conda install -c anaconda pillow


# In[8]:


print(f"The NetworkX package is version {nx.__version__}")
print(f"The OSMNX package is version {ox.__version__}")
print(f"The Request package is version {requests.__version__}")
print(f"The PIL package is version {PIL.__version__}")


# In[9]:


print(f"The OSMNX package is version {ox.__version__}")


# In[10]:


import osmnx as ox
places = ["bengaluru, Karnataka, India"]

# Get data for places
G = ox.graph_from_place(places, network_type = "all", simplify = True)


# In[17]:


import osmnx as ox

center_point = (12.9716, 77.5946)
G = ox.graph_from_point(center_point, dist=15000, retain_all=True, simplify = True, network_type='all')


# In[18]:


u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)    


# In[19]:


# Lists to store colors and widths 
roadColors = []
roadWidths = []

for item in data:
    if "length" in item.keys():
        if item["length"] <= 100:
            linewidth = 0.10
            color = "#9c5252" 
            
        elif item["length"] > 100 and item["length"] <= 200:
            linewidth = 0.15
            color = "#9c5252"
            
        elif item["length"] > 200 and item["length"] <= 400:
            linewidth = 0.25
            color = "#a8a625"
            
        elif item["length"] > 400 and item["length"] <= 800:
            color = "#bdbdbd"
            linewidth = 0.35
        else:
            color = "#d5d5d5"
            linewidth = 0.45

        if "primary" in item["highway"]:
            linewidth = 0.5
            color = "#ffff"
    else:
        color = "#a6a6a6"
        linewidth = 0.10
            
    roadColors.append(color)
    roadWidths.append(linewidth)


# In[20]:


for item in data:
    if "footway" in item["highway"]:
        color = "#181fb5"
        linewidth = 0.25
    else:
        color = "#a6a6a6"
        linewidth = 0.5
        
    roadWidths.append(linewidth)


# In[30]:


latitude = 12.9716
longitude = 77.5946

#Limit borders 
north = latitude + 0.15
south = latitude - 0.15
east = longitude + 0.15
west = longitude - 0.15

bgcolor = "#061529"

fig, ax = ox.plot_graph(G, node_size=0, bbox = (north, south, east, west),
                        dpi = 300,bgcolor = bgcolor,
                        save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig("madrid.png", dpi=300, bbox_inches='tight', format="png", 
            facecolor=fig.get_facecolor(), transparent=False)


# In[24]:


fig, ax = ox.plot_graph(G, node_size=0, bbox = (north, south, east, west),
                        dpi = 300,bgcolor = bgcolor,
                        save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig("Bangalore.png", dpi=300, bbox_inches='tight', format="png", 
            facecolor=fig.get_facecolor(), transparent=False)


# In[27]:





# In[29]:





# In[ ]:




