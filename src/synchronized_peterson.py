import threading
import time

from src.config import page_process_time
from src.job_generator import JobGenerator
from src.structures import Job, Worker, JobType

job_generator = JobGenerator(users=["P1", "P2", "P3", "P4", "P5"])

printer = Worker("Printer")
scanner = Worker("Scanner")

jobs = job_generator.generate_jobs(5)

flag = [False, False]
turn = 0

def peterson_lock(process_id):
    global flag, turn
    other = 1 - process_id
    flag[process_id] = True
    turn = other
    while flag[other] and turn == other:
        pass

def peterson_unlock(process_id):
    global flag
    flag[process_id] = False

def process_user_jobs(user_jobs: list[Job], process_id: int) -> None:
    start_time = time.time()
    for job in user_jobs:
        if job.arrival_time > time.time() - start_time:
            time.sleep(job.arrival_time - time.time() + start_time)
        while job.length > 0:
            if job.job_type == JobType.PRINT:
                peterson_lock(process_id)
                printer.process_job_page(job)
                peterson_unlock(process_id)
            else:
                scanner.process_job_page(job)
            time.sleep(page_process_time)

for i, user_jobs_ in enumerate(jobs):
    threading.Thread(target=process_user_jobs, args=(user_jobs_, i % 2)).start()