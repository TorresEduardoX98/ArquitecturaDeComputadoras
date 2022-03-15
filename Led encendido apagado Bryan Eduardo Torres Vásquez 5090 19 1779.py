import pyfirmata
 
puerto = 'COM3'
pin = (5)
 
print("ARDUINO CONECTADO")
tarjeta = pyfirmata.Arduino(puerto)
while True:
    print("LED ENCENDIDO")
    tarjeta.digital[pin].write(1)
    tarjeta.pass_time(0.5)
    print("LED APAGADO")
    tarjeta.digital[pin].write(0)
    tarjeta.pass_time(0.5)
tarjeta.exit()