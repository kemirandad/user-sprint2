from typing import  Dict, Optional
from pydantic import BaseModel, EmailStr

class usuario_data(BaseModel):
    id: Optional[int] = 0
    username: str
    usersurname: str
    userdocument: int
    usermail: EmailStr
    userphone: int 
    
""" class usuario_data(BaseModel):
    username: str
    usersurname: str
    userdocument: int
    usermail: EmailStr
    userphone: int  """
    
    
generador = {"id":0}

user_database = Dict[str, usuario_data]

user_database = {
    1082976: usuario_data(**{"id":0,
                            "username":"kenny",
                            "usersurname":"miranda",
                            "userdocument":1082976,
                            "usermail":"k@k.com",
                            "userphone":589963})
}

def get_user(document_user: int):
    if document_user in user_database.keys():
        return user_database[document_user]
    else:
        return None
    
def create_user(new_user: usuario_data):
    if  new_user.userdocument in user_database.keys():
        return None
    else:
        generador["id"] = generador["id"] + 1
        new_user.id = generador["id"]
        user_database[new_user.userdocument] = new_user
        return new_user
