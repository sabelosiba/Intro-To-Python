import random
import time

servicesAreUp = True

def getData50():
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'
    

def getData25():
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'


def getData10():
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'
    
def getWithRetry(dataFunc):
    #if dataFunc =='None':
    #    return getWithRetry(dataFunc) # Recursion to call same function with default argument value
    max_tries = 2
    wait_time = .5
    tries = 0
    result = None
    while tries < max_tries:
        try:
            result = dataFunc()
            break
        except Exception as e:
            print('Service not available...')
            servicesAreUp = False
            time.sleep(wait_time)
            tries += 1
            
    servicesAreUp = True # Reset flag after successful request
    if result is None:
        raise ValueError("Failed to retrieve data after %d attempts" % (max_tries))
    else:
        return result
    
    

print(getWithRetry(getData50))