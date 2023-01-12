import time
from locust import HttpUser, TaskSet, task, constant, LoadTestShape

class UserBehavior(TaskSet):
    def on_start(self):
        pass
    
    @task(1)
    def index(self):
        """
        self.client.get("/product/0PUK6V6EV0")
        self.client.post("/cart", {
            'product_id': "0PUK6V6EV0",
            'quantity': 1})
        self.client.post("/cart/checkout", {
            'email': 'someone@example.com',
            'street_address': '1600 Amphitheatre Parkway',
            'zip_code': '94043',
            'city': 'Mountain View',
            'state': 'CA',
            'country': 'United States',
            'credit_card_number': '4432-8015-6152-0454',
            'credit_card_expiration_month': '1',
            'credit_card_expiration_year': '2039',
            'credit_card_cvv': '672',
        })
        """
        self.client.get("/cart/checkout")

class WebsiteUser(HttpUser):
    tasks = {UserBehavior}
    wait_time = constant(1)