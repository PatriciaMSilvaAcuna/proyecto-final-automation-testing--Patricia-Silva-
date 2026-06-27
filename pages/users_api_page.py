import requests

class UsersApi:
    URL_BASE = "https://jsonplaceholder.typicode.com/"


    def get_users(self):
        return requests.get(

            f"{self.URL_BASE}/users"
        )
    
    
    def get_one_user(self,user_id):
        return requests.get(
            f"{self.URL_BASE}/users/{user_id}"


        )
    def create_user(self, name, username, email):
        data = {
        "name": name,
        "username": username,
        "email": email

        }
        return requests.post(
            f"{self.URL_BASE}users",
            json=data
        )
    def delete_user(self,user_id):
        return requests.delete(
             f"{self.URL_BASE}users/{user_id}"
        )