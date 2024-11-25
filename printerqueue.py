
class PrinterQueue:
    jobs = []
    def __init__(self, sourcecollection):
        for items in sourcecollection:
            self.add(items)

    # Addes a job to the queue based off priority using Binary Search
    def add(self, job):
        low = 0
        high = len(self.jobs)
        mid = (high) // 2
        while low <= high:
            if self.jobs[mid].priority == job.priority:
                self.jobs.insert(mid, job)
                break
            elif self.jobs[mid].priority < job.priority:
                low = mid + 1
            else:
                high = mid - 1
        if low > high:
            self.jobs.insert(len(self.jobs) -1, job)
    # Prints the first job in the queue and removes it
    def printJob(self):
        print(self.jobs[0])
        self.jobs.pop(0)