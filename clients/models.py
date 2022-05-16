import uuid


class Client:
    def __init__(self, username, password, name, company, city, email, position, age, uid=None):
        self.username=username
        self.password=password
        self.name=name
        self.company=company
        self.city=city
        self.email=email
        self.position=position
        self.age=age
        self.uid=uid or uuid.uuid4() #uuid4 es el estandar de la industria

    
    def to_dict(self):
        return vars(self)

    
    @staticmethod # es un metodo estatico, y este es un metodo que se puede ejecutar sin necesidad de una instancia de clase
    def schema(): # en este caso vamos a declarar el esquema que nosotros definimos para que se pueda guardar en la base de datos
        return ['username', 'password', 'name', 'company', 'city', 'email', 'position', 'age', 'uid']