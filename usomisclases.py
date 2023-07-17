from mi_paquete.cliente import Cliente

#clientes
cliente1 = Cliente("ana", 18, "Calle 123, Ciudad", "ana@ejemplo.com")
cliente2 = Cliente("nacho", 19, "Avenida 456, Ciudad", "nacho@ejemplo.com")

print(cliente1.nombre)# Imprimirá "ana"
print(cliente2.edad)# Imprimirá 19

cliente1.comprar("telefono")# Imprimirá "ana compro telefono."
cliente2.enviar_correo("Hola nacho. ¡Gracias por tu compra!")