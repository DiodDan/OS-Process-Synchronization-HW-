from random import choice, randint, shuffle

from src.structures import Job, JobType


class JobGenerator:
    def __init__(self,
                 users: list[str],
                 min_arrival: int = 1,
                 max_arrival: int = 5,
                 min_pages: int = 1,
                 max_pages: int = 50
                 ):
        self.users = users
        self.min_arrival = min_arrival
        self.max_arrival = max_arrival
        self.max_pages = max_pages
        self.min_pages = min_pages

    def _generate_job(self, user: str, prev_arrival: int) -> Job:
        job_type = choice(list(JobType))
        length = randint(self.min_pages, self.max_pages)
        arrival_time = randint(self.min_arrival, self.max_arrival) + prev_arrival
        return Job(user, job_type, length, arrival_time)

    def generate_jobs(self, num_jobs: int) -> list[list[Job]]:
        jobs = []
        for user in self.users:
            user_jobs = []
            for _ in range(num_jobs):
                user_jobs.append(self._generate_job(user, user_jobs[-1].arrival_time if user_jobs else 0))
            jobs.append(user_jobs)
        return jobs