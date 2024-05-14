#!/usr/bin/env python
# coding: utf-8

# In[4]:


bird_lib={}
def sighting(bird,param2=1):
    if bird in bird_lib:
        bird_lib[bird] +=param2
    else:
        bird_lib[bird] =param2
        
sighting("robin",2)  


# In[41]:


bird_lib={}
def multiple_sightings(*args):
    for i in range(0, len(args), 2):
        bird = args[i]
        num_sightings = args[i + 1]
        if bird in bird_lib:
            bird_lib[bird] += num_sightings
        else:
            bird_lib[bird] = num_sightings
    return bird_lib  


# In[52]:


multiple_sightings("robin",1,"bluejay",4)


# In[48]:


bird_lib={}
def add_kw_observations(*args, **kwargs):
    bird_lib = {}  
    if args:
        for bird in args:
            if bird in bird_lib:
                bird_lib[bird] += 1
            else:
                bird_lib[bird] = 1

    for bird, num_sightings in kwargs.items():
        if bird in bird_lib:
            bird_lib[bird] += num_sightings
        else:
            bird_lib[bird] = num_sightings

    return bird_lib


# In[49]:


add_kw_observations("robin",sparrow=3,hawk=1)


# In[ ]:




