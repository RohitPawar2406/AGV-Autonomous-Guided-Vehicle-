#!/usr/bin/env python
# coding: utf-8

# In[1]:


import asyncio
import websockets

async def hello():
    uri = "ws://localhost:3001"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())


# In[ ]:



