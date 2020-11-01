import datetime
def current_time():
    '''
    Provide current time
    '''
    current = datetime.datetime.now()
    return current
    
if __name__ == "__main__":
    print(current_time())