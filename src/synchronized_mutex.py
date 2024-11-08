import threading
import time

from src.config import page_process_time
from src.job_generator import JobGenerator
from src.structures import Job, Worker, JobType

job_generator = JobGenerator(users=["P1", "P2", "P3", "P4", "P5"])

printer = Worker("Printer")
scanner = Worker("Scanner")

jobs = job_generator.generate_jobs(5)

printer_lock = threading.Lock()
scanner_lock = threading.Lock()

def process_user_jobs(user_jobs: list[Job]) -> None:
    start_time = time.time()
    for job in user_jobs:
        if job.arrival_time > time.time() - start_time:
            time.sleep(job.arrival_time - time.time() + start_time)
        while job.length > 0:
            if job.job_type == JobType.PRINT:
                with printer_lock:
                    printer.process_job_page(job)
            else:
                with scanner_lock:
                    scanner.process_job_page(job)
            time.sleep(page_process_time)

for user_jobs_ in jobs:
    threading.Thread(target=process_user_jobs, args=(user_jobs_, )).start()