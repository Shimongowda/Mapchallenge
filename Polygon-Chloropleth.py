#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install plotly


# In[3]:


import json
import numpy as np
import pandas as pd
import plotly.express as px


# In[119]:


import plotly.io as pio
pio.renderers.default = 'browser'
india_states = json.load(open("states_india.geojson", "r"))


# In[105]:


# ------------ loading open Supply Hub data--------
import pandas as pd
facs = pd.read_csv('state_wise_crop_production_v2.csv')


# In[106]:


facs.head()


# In[122]:


state_id_map = {}
for feature in india_states["features"]:
    feature["Id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["Id"]


# In[123]:


facs["Id"] = facs["State"].apply(lambda x: state_id_map[x])


# In[124]:


facs["Cost_of_Cult_per_hect"].plot()


# In[125]:


facs["DensityScale"] = np.log10(facs["Cost_of_Cult_per_hect"])


# In[126]:


facs["DensityScale"].plot()


# In[127]:


fig = px.choropleth(
    facs,
    locations="Id",
    geojson=india_states,
    color="DensityScale",
    hover_name="State",
    hover_data=["Cost_of_Cult_per_hect"],
    title="India Population Density",
)
fig.update_geos(fitbounds="locations", visible=False)
fig.show()


# In[128]:



fig = px.choropleth_mapbox(
    facs,
    locations="Id",
    geojson=india_states,
   color="DensityScale",
    hover_name="State",
    hover_data=["Cost_of_Cult_per_hect"],
    title="India Population Density",
    mapbox_style="carto-positron",
    center={"lat": 24, "lon": 78},
    zoom=3,
    opacity=0.5,
)
fig.show()


# In[ ]:




