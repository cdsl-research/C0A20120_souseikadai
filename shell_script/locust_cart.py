import time
from locust import HttpUser, TaskSet, task, constant, LoadTestShape

class UserBehavior(TaskSet):
    def on_start(self):
        pass
    
    @task(1)
    def index(self):
        self.client.get("/cart")

class WebsiteUser(HttpUser):
    tasks = {UserBehavior}
    wait_time = constant(1)