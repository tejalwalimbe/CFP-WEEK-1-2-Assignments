#StopWatch program
import time
class Stopwatch:
    start= input ("press Enter to start the timer")
    print ("The timer has started")
    begin = time.time() #starts the timer
    endtimer = input("press enter to stop the timer")
    end = time.time()
    elapsed = end - begin
    elapsed = int(elapsed)
    print("The time elapsed is",elapsed,"seconds")