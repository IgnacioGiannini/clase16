class Cliente:
    def __init__(self, n, e, c, d):
        self.nombre = n
        self.edad = e
        self.direccion = d
        self.correo = c

    def comprar(self, producto):
        print(f"{self.nombre} compro {producto}.")

    def enviar_correo(self, mensaje):
        print(f"Correo enviado a {self.nombre}: {mensaje}")

    def __str__(self):
        return f"Cliente: {self.nombre}"