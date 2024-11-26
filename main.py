from printerqueue import PrinterQueue
from printerjob import PrinterJob
import random

def main():
  controller = ""
  # Generated Jobs with random Priority
  printer = PrinterQueue([PrinterJob(random.randint(1, 10), "If you can dream it, you can do it - Walt Disney", "disney"), 
                               PrinterJob(random.randint(1, 10), "You will face many defeats in life, but never let yourself be defeated - Maya Angelou", "mayangelou"), 
                               PrinterJob(random.randint(1, 10), "You must be the change you wish to see in the world - Mahatma Gandhi", "mahatmagandhi"), 
                               PrinterJob(random.randint(1, 10), "If you are going through hell, keep going - Winston Churchill", "winston"), 
                               PrinterJob(random.randint(1, 10), "The only way to do great work is to love what you do - Steve Jobs", "steve"), 
                               PrinterJob(random.randint(1, 10), "Spread love everywhere you go. Let no one ever come to you without leaving happier - Mother Teresa", "motherteresa"), 
                               PrinterJob(random.randint(1, 10), "The greatest glory in living lies not in never falling, but in rising every time we fall - Nelson Mandela", "nelson"),])
  printer.listjobs()

  # Main Menu
  while controller != 0:
    controller = ""
    print("1. Print Job\n2. Print All Jobs\n3. Add Job\n4. List Jobs\n5. Remove Job\n0. Exit")
    controller = int(input())
    if controller == 1:
      printer.printJob()
    elif controller == 2:
      if len(printer.jobs) == 0:
        print("No Jobs Found")
      while len(printer.jobs) != 0:
        printer.printJob()
    elif controller == 3:
      printer.add(PrinterJob(int(input("Enter the priority of the Job: ")), input("Enter a Job: "), input("Enter the name of the Job: ")))
    elif controller == 4:
      printer.listjobs()
    elif controller == 5:
      printer.removebyname(input("Enter the name of the job to remove: "))
    elif controller != 0:
      print("Invalid Input")
  
  # Will print remaining Jobs before exiting if there are any
  if len(printer.jobs) != 0:
    print("Printing Rest of Jobs...")
    for items in printer.jobs:
      print(items.printJob())
    print("All Jobs Printed!")
  print("Goodbye!")
  

if __name__ == "__main__":
  main()
