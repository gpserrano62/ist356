# this is an example of a re-try loop

from time import sleep

TIMES = 5
BACKOFF = 5

print("Starting the retry loop...")
for attempt in range(TIMES):
    print(f"Attempt {attempt+1} of {TIMES}")
    delay = BACKOFF * attempt
    print(f"Sleeping for {delay} seconds...")
    #sleep(delay)
    for i in range(delay):
        print(f"." , end = "", flush = True)
        sleep(1)
    print("Retrying...")