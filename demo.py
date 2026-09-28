import asyncio
import time

def synchronous_task(task_id: int ) -> str:
    time.sleep(3)
    return f"Task {task_id} completed"



def demo_synchronous():
    start = time.time()
    results = []

    for i in range(3):
        results =synchronous_task(i)
        
