import time
from locust import HttpUser, TaskSet, task, constant

class UserBehavior(TaskSet):
    def on_start(self):
        pass
    
    
    @task(1)
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpUser):
    tasks = {UserBehavior}
    wait_time = constant(1)