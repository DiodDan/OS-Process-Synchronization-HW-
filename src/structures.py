import threading
import time
from enum import Enum

from src.config import page_process_time


class JobType(Enum):
    PRINT = "Print"
    SCAN = "Scan"


class JobLength(Enum):
    SHORT = "Short"
    MEDIUM = "Medium"
    LONG = "Long"

    @staticmethod
    def from_int(length: int) -> "JobLength":
        if length < 6:
            return JobLength.SHORT
        elif length < 16:
            return JobLength.MEDIUM
        else:
            return JobLength.LONG


class Job:
    def __init__(self,
                 user: str,
                 job_type: JobType,
                 length: int,
                 arrival_time: int):
        self.user = user
        self.job_type = job_type
        self.length = length
        self.length_type = JobLength.from_int(length)
        self.arrival_time = arrival_time

    def __repr__(self) -> str:
        return f"User {self.user}: {self.job_type} Job, {self.length} pages, Arrival Time: {self.arrival_time}s"

    def __str__(self) -> str:
        return f"User {self.user}: {self.job_type} Job, {self.length} pages, Arrival Time: {self.arrival_time}s"


def jobs_log(jobs: list[Job]) -> str:
    return "\n".join([str(i) + ") " + str(job) for i, job in enumerate(jobs)])


class Worker:
    def __init__(self, name: str, process_time: float = page_process_time):
        self.name = name
        self.process_time = process_time
        self.last_process_time = time.time()
        self.total_printed = 0

    def process_job_page(self, job: Job) -> None:
        print(f"{self.name}(total: {self.total_printed}) is processing page {job.length} of job {job}")
        self.total_printed += 1
        job.length -= 1

    def __repr__(self) -> str:
        return f"Printer {self.name}"

    def __str__(self) -> str:
        return f"Printer {self.name}"
