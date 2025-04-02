class persona:
    def __init__(self,carlos):
        self.nombre = "Carlos"
        self.apellidos = "Lopez"
        self.edad = "23"
        self.dni = "000x"
    def __str__(self):
        return " Nombre: " + str(self.nombre) + " Apellidos: " + str(self.apellidos) + " Edad: "+ str(self.edad) + " DNI: " + str(self.dni)
    """
    def __init__(self,luis):
        self.nombre = "Luis"
        self.apellidos = "Fonsi"
        self.edad = "32"
        self.dni = "0009999x"
    def __str__(self):
        return " Nombre: " + str(self.nombre) + " Apellidos: " + str(self.apellidos) + " Edad: "+ str(self.edad) + " DNI: " + str(self.dni)
    """
carlos = persona("carlos")
#luis = persona("fonsi")
print(carlos)
#print(luis)
