class admin:
    def __init__(self,nombre,apellido,username,password):
        self.nombre=nombre
        self.apellido=apellido
        self.username=username
        self.password=password

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def setNombre(self,nombre):
        self.nombre=nombre
    
    def setApellido(self,apellido):
        self.apellido=apellido

    def setUsername(self,username):
        self.username=username

    def setPassword(self,password):
        self.password=password