from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def print_schedule(self):
        sorted_tasks = sorted(self.tasks, key=lambda t: t.due_date)
        now = datetime.now()
        for t in sorted_tasks:
            status = "Overdue" if t.due_date < now else "Pending"
            print(f"Task: {t.name}, Due: {t.due_date.strftime('%Y-%m-%d')}, Priority: {t.priority}, Status: {status}")

scheduler = TaskScheduler()
scheduler.add_task(Task("Finish report", "2026-02-01", "High"))
scheduler.add_task(Task("Pay bills", "2026-12-31", "Medium"))
scheduler.print_schedule()
