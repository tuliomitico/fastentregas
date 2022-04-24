from datetime import datetime as DateTime

class Delivery:
  def __init__(
    self,
    code: str,
    hour: DateTime,
    address: str,
    telephone: str,
    name: str,
    date: str
  ):
    self.code = code
    self.hour = hour
    self.address = address
    self.telephone = telephone
    self.name = name
    self.date = date
