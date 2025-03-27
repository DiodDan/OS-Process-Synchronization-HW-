# Process Synchronization Simulation

### Table of Contents

- [Project Structure](#project-structure)
- [Part 1: Job Generator](#part-1-job-generator)
- [Part 2: Task Implementation](#part-2-task-implementation)
    - [Task 1: Without Synchronization](#task-1-without-synchronization)
    - [Task 2: With Synchronization](#task-2-with-synchronization)
- [Testing and Results](#testing-and-results)
- [How to Run the Code](#how-to-run-the-code)
- [Comparative Analysis](#comparative-analysis)
- [References](#references)

---

## Project Structure

This submission includes:

- [job_generator.py](./src/job_generator.py): Python script for Part 1, generating random print and scan jobs for each user.
- [structures.py](./src/structures.py): Python script defining the data structures.
- [non_synchronized.py](./src/non_synchronized.py): Python script for Task 1, executing jobs without synchronization.
- [synchronized_mutex.py](./src/synchronized_mutex.py): Python script for Task 2, using mutexes for synchronization.
- [synchronized_semaphore.py](./src/synchronized_semaphore.py): Python script for Task 2, using semaphores for synchronization.
- [synchronized_peterson.py](./src/synchronized_peterson.py): Python script for Task 2, using Peterson’s solution for mutual
  exclusion.

---

## Part 1: Job Generator

### Jobs are randomly generated for each user.

here is sample of the job generator output:

Example:

```
0) User P1: JobType.PRINT Job, 41 pages, Arrival Time: 4s
1) User P1: JobType.PRINT Job, 13 pages, Arrival Time: 6s
2) User P1: JobType.SCAN Job, 28 pages, Arrival Time: 10s
3) User P1: JobType.PRINT Job, 15 pages, Arrival Time: 11s
4) User P1: JobType.PRINT Job, 19 pages, Arrival Time: 14s
```

---

## Part 2: Task Implementation

### Task 1: Without Synchronization

- In this implementation, jobs are executed without any synchronization, allowing multiple users to access the same resources
  simultaneously.
- **Expected Issues:** Race conditions and deadlocks are likely, as jobs compete for resources without controlled access.
- **Output Format:** Each job’s progress is logged page-by-page, with inconsistencies observed due to concurrent access.

Example:

```
Scaner(total: 0) is processing page 20 of job User P3: JobType.SCAN Job, 20 pages, Arrival Time: 1s
Scaner(total: 1) is processing page 19 of job User P3: JobType.SCAN Job, 19 pages, Arrival Time: 1s
Scaner(total: 2) is processing page 18 of job User P3: JobType.SCAN Job, 18 pages, Arrival Time: 1s
Scaner(total: 3) is processing page 17 of job User P3: JobType.SCAN Job, 17 pages, Arrival Time: 1s
Scaner(total: 4) is processing page 16 of job User P3: JobType.SCAN Job, 16 pages, Arrival Time: 1s
Scaner(total: 5) is processing page 15 of job User P3: JobType.SCAN Job, 15 pages, Arrival Time: 1s
Scaner(total: 6) is processing page 14 of job User P3: JobType.SCAN Job, 14 pages, Arrival Time: 1s
Scaner(total: 7) is processing page 13 of job User P3: JobType.SCAN Job, 13 pages, Arrival Time: 1s
Scaner(total: 8) is processing page 12 of job User P3: JobType.SCAN Job, 12 pages, Arrival Time: 1s
Scaner(total: 9) is processing page 11 of job User P3: JobType.SCAN Job, 11 pages, Arrival Time: 1s
Printer(total: 0) is processing page 27 of job User P5: JobType.PRINT Job, 27 pages, Arrival Time: 2s
Scaner(total: 10) is processing page 10 of job User P3: JobType.SCAN Job, 10 pages, Arrival Time: 1s
Printer(total: 1) is processing page 26 of job User P5: JobType.PRINT Job, 26 pages, Arrival Time: 2s
Scaner(total: 11) is processing page 9 of job User P3: JobType.SCAN Job, 9 pages, Arrival Time: 1s
Printer(total: 2) is processing page 25 of job User P5: JobType.PRINT Job, 25 pages, Arrival Time: 2s
Scaner(total: 12) is processing page 8 of job User P3: JobType.SCAN Job, 8 pages, Arrival Time: 1s
Printer(total: 3) is processing page 24 of job User P5: JobType.PRINT Job, 24 pages, Arrival Time: 2s
Scaner(total: 13) is processing page 7 of job User P3: JobType.SCAN Job, 7 pages, Arrival Time: 1s
Printer(total: 4) is processing page 23 of job User P5: JobType.PRINT Job, 23 pages, Arrival Time: 2s
Scaner(total: 14) is processing page 6 of job User P3: JobType.SCAN Job, 6 pages, Arrival Time: 1s
Printer(total: 5) is processing page 22 of job User P5: JobType.PRINT Job, 22 pages, Arrival Time: 2s
Scaner(total: 15) is processing page 5 of job User P3: JobType.SCAN Job, 5 pages, Arrival Time: 1s
Printer(total: 6) is processing page 21 of job User P5: JobType.PRINT Job, 21 pages, Arrival Time: 2s
Scaner(total: 16) is processing page 4 of job User P3: JobType.SCAN Job, 4 pages, Arrival Time: 1s
Printer(total: 7) is processing page 20 of job User P5: JobType.PRINT Job, 20 pages, Arrival Time: 2s
Scaner(total: 17) is processing page 3 of job User P3: JobType.SCAN Job, 3 pages, Arrival Time: 1s
Printer(total: 8) is processing page 19 of job User P5: JobType.PRINT Job, 19 pages, Arrival Time: 2s
Scaner(total: 18) is processing page 2 of job User P3: JobType.SCAN Job, 2 pages, Arrival Time: 1s
```

### Task 2: With Synchronization

This version uses synchronization mechanisms to manage access to shared resources.

- **Mutexes:** Used to ensure exclusive access to the printer and scanner.
- **Semaphores:** Control job scheduling to prioritize jobs waiting for resources.
- **Peterson’s Solution:** Demonstrates another mutual exclusion approach for the printer.

---

## How to Run the Code 

simply copy code from github and run any file from solutions. Use python 3.12^

---

## Comparative Analysis

The comparative analysis in the report discusses:

- **Mutexes:** Suitable for exclusive access, effectively preventing data inconsistencies.
- **Semaphores:** Useful for controlled job switching, reducing resource contention.
- **Peterson’s Solution:** Demonstrates mutual exclusion for two processes accessing the same resource.
- **Performance and Accuracy:** Measured by completion times and log consistency, showing how synchronization mechanisms improve
  resource management.

---