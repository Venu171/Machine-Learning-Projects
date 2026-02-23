import asyncio
# Before python 3.5+, we used to concurrent programming.
# Concurrent programming means we used to create 
# multiple threads from CPU to handle the traffic.

# In Asynchronous programming we will have a single thread and 
# can handle the different functions simultaneously.

def hello()->str:
    return "Hello!"

async def hello_world():
    print("Hello World!")

print(hello())#Hello!
# print(hello_world())#<coroutine object hello_world at 0x000001DD75B04BF0>
asyncio.run(hello_world())
