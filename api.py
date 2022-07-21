from fastapi import FastAPI
from faker import Faker

app = FastAPI()

@app.get("/users")
def users_list():
    """ Lista de usuarios fake """
    data = []

    faker = Faker()
    for i in range(11):
        profile = None
        profile = faker.simple_profile()

        data.append(profile)

    return data