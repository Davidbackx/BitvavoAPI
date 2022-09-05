from datetime import datetime
import time
def main_func(func):
    def wrapper(*args, **kwargs):
        print("fetching your data")
        return func(*args, **kwargs)
        
    return wrapper
def timer(func):
    def time_wrapper(*args, **kwargs):
        print("we are timing this function")
        x = datetime.now()
        func(*args, **kwargs)
        time.sleep(10)
        return datetime.now()-x
    return time_wrapper

@main_func
@timer
def overview(apikey,secret_key):
    return (f"your data with the corresponding keys api_key: {apikey} and secret key: {secret_key} has been processed")

print(overview("apikey1245","secretkey124681354"))