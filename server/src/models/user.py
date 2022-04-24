from uuid import uuid4

class User:
  def __init__(self,id: str,name: str, password: str, telephone: str) -> None:
      self.id = id
      self.name = name
      self.password = password
      self.telephone = telephone
      if not self.id:
        self.id = uuid4()
