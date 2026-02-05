#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
from datetime import datetime, timedelta


class Task:
    def __init__(self, name: str, priority: int, run_at: datetime):
        self.name = name
        self.priority = priority
        self.run_at = run_at

    def __lt__(self, other):
        # avval vaqt, keyin priority
        if self.run_at == other.run_at:
            return self.priority < other.priority
        return self.run_at < other.run_at


class TaskScheduler:
    def __init__(self):
        self.queue = []

    def add_task(self, task: Task):
        heapq.heappush(self.queue, task)

    def run(self):
        now = datetime.now()

        while self.queue and self.queue[0].run_at <= now:
            task = heapq.heappop(self.queue)
            self.execute(task)

    def execute(self, task: Task):
        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] "
            f"Running task: {task.name} (priority {task.priority})"
        )


# ===== TEST =====
scheduler = TaskScheduler()

scheduler.add_task(
    Task("Backup", 2, datetime.now() + timedelta(seconds=1))
)
scheduler.add_task(
    Task("Email Sender", 1, datetime.now() + timedelta(seconds=1))
)
scheduler.add_task(
    Task("Cleanup", 3, datetime.now())
)

scheduler.run()
