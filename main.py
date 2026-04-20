import threading
import queue
import time

class Worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            task = self.queue.get()
            if task is None:
                break
            task()
            self.queue.task_done()

class WorkerSystem:
    def __init__(self, num_workers):
        self.queue = queue.Queue()
        self.workers = []
        for _ in range(num_workers):
            worker = Worker(self.queue)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)

    def submit_task(self, task):
        self.queue.put(task)

    def shutdown(self):
        for _ in range(len(self.workers)):
            self.queue.put(None)
        self.queue.join()

def example_task():
    print("Task is running")
    time.sleep(1)
    print("Task is finished")

if __name__ == "__main__":
    worker_system = WorkerSystem(5)
    for _ in range(10):
        worker_system.submit_task(example_task)
    worker_system.shutdown()
```

Kodda quyidagilar mavjud:

*   Worker klassi: bu klass threadni amalga oshiradi. U quyidagilar bilan ishlaydi:
    *   Queue dan task olib keladi
    *   Taskni amalga oshiradi
    *   Taskni amalga oshirgandan keyin queuega taskni amalga oshirganligini bildiradi
*   WorkerSystem klassi: bu klass workerlarni boshqaradi. U quyidagilar bilan ishlaydi:
    *   Workerlarni yaratadi
    *   Workerlarni ishga tushiradi
    *   Tasklarni queuega qo'yadi
    *   Workerlarni to'xtatadi
*   example_task funktsiyasi: bu funktsiya worker tomonidan amalga oshiriladigan taskdir. U quyidagilar bilan ishlaydi:
    *   Taskni amalga oshiradi
    *   Taskni amalga oshirgandan keyin print qiladi
