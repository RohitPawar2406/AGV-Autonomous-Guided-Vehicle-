#!/usr/bin/env python
# coding: utf-8

# In[1]:


import asyncio
import websockets


# In[2]:


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"
    #greeting ="Hello Rohit!!!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 3001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


# In[ ]:




