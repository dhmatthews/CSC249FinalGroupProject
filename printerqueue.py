from printerjob import PrinterJob

class PrinterQueue:
    jobs = []
    def __init__(self, sourcecollection):
        for items in sourcecollection:
            self.add(items)

    # Addes a job to the queue based off priority using Binary Search
    def add(self, job):
        # Checks if job name is already in use despite capitalization
        for items in self.jobs:
            if items.name.lower() == job.name.lower():
                print('Job Name Already in use!')
                return
        print('Adding Job With Name: ' + job.name + '...')
        # Use of Binary Search to find where to add the job in the Queue
        if len(self.jobs) == 0:
            self.jobs.append(job)
        else:
            low = 0
            high = len(self.jobs) - 1
            while low <= high:
                mid = (low + high) // 2
                if self.jobs[mid].priority < job.priority:
                    low = mid + 1
                else:
                    high = mid - 1
            self.jobs.insert(low, job)

    # Prints the first job in the queue and removes it
    def printJob(self):
        print('Printing....')
        print(self.jobs[0].printJob())
        self.jobs.remove(self.jobs[0])
    
    # Removes a job using the name of the Job
    def removebyname(self, name):
        print('Removing Job With Name: ' + name + '...')
        for items in self.jobs:
            if items.name.lower() == name.lower():
                self.jobs.remove(items)
                return
        print('Job Not Found')
    
    # Lists all jobs currently in the queue
    def listjobs(self):
        if len(self.jobs) == 0:
            print('No Jobs Found')
        else:
            print('Listing Current Jobs...')
            for items in self.jobs:
                print("Name of Print Job: " + items.name + ", Priority: " + str(items.priority))
    