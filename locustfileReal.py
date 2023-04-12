from locust import HttpUser, constant, task

siteKey = "keynum"
qaURL = "http://baseUrl"
params = "?"
query="?queryString"
auth_header = {
    'content-type': 'application/json',
    'Authorization': 'secret ' + siteKey
}


class MyReqRes(HttpUser):
    host = qaURL
    wait_time = constant(1) # Waits 1 second until the next request

    @task
    def get_mainURL(self):
        res = self.client.request(
            method='GET',
            url=params
            headers=auth_header
        )
        print(res.status_code)

    @task
    def get_Query(self):
        res = self.client.request(
            method='GET',
            url=query,
            headers=auth_header
        )
        print(res.status_code)


