"""
Writing Asynchronous code is a powerful way to create apps that run in parallel making our code run more efficient,
but it's important to understand why we do it and how code runs normally
"""
import asyncio.tasks
import time

"""
Take for example a Scenario with creating a web app that calls on an API to generate parts of our page, heres what it would
look like if we did it one by one
"""

def downloadPage(url, component):
    print(f"getting web page component:{component} from {url}")
    time.sleep(2) # simulate a Input output delay of pulling the asset
    print(f"instantiating webpage component{component} from {url}")

def start():
    """
    using time.sleep we pause fully to demonstrate the difference between async and sync
    :return:
    """

    downloadPage("https://www.vli.com/weather", "humidity dial")
    downloadPage("https://www.vli.com/weather", "temperature dial")

"""
by running start what would occur is humidity dial would need to complete instatiation before we could 
move on to getting our temprature dial. Doing this for 100 components would be a waste of time
Lets instead implement this code with python library asyncio to make it more efficient
"""

async def downloadComponent(url, component):
    print(f"getting web page component: {component} from {url}")
    await asyncio.sleep(2) # simulate a Input output delay of pulling the asset
    print(f"instantiating webpage component: {component} from {url}")
async def startWithAsync():
    """
    This time using asyncio.sleep which simulates an asynchronous pause
    :return:
    """
    task1 = asyncio.tasks.create_task(downloadComponent("https://www.vli.com/weather", "humidity dial"))
    task2 = asyncio.tasks.create_task(downloadComponent("https://www.vli.com/weather", "temperature dial"))

    await task1
    await task2

"""
running startwithAsync() you will see that we begin the instantiation process for each componenet instead of 1 at a time
"""