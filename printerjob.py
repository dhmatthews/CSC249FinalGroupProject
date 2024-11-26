class PrinterJob:
    priority = 0
    job = ""
    name = ""

    def __init__(self, priority, job, name):
        self.priority = priority
        self.job = job
        self.name = name
    
    def printJob(self):
        return self.job