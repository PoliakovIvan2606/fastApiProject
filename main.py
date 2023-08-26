from fastapi import FastAPI
from models import User

app = FastAPI()

@app.post('/{id}/{name}/{last_name}', response_model=User)
def root(id, name, last_name):
    json = {
        'id': id,
        'name': name,
        'last_name': last_name
    }

    user = User(**json)
    return {'id': user.id, 'user': user.name, 'last_name': user.last_name}