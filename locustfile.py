from locust import HttpUser, constant, task
import os

theSecret = os.environ.get('SECRET_KEY')
baseURL = "https://http.cat"
fivehundo = "/500"
twohundo ="/200"


class MyReqRes(HttpUser):
    host = baseURL
    wait_time = constant(1) # Waits 1 second until the next request

    @task
    def get_500(self):
        res = self.client.request(
            method='GET',
            url=fivehundo
        )
        print(res.status_code)
        print(theSecret)

    @task
    def get_200(self):
        res = self.client.request(
            method='GET',
            url=twohundo
        )
        print(res.status_code)


