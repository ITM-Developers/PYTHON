'''
 ___ _____ __  __       ____                 _
|_ _|_   _|  \/  |     |  _ \  _____   _____| | ___  _ __   ___ _ __ ___
 | |  | | | |\/| |_____| | | |/ _ \ \ / / _ \ |/ _ \| '_ \ / _ \ '__/ __|
 | |  | | | |  | |_____| |_| |  __/\ V /  __/ | (_) | |_) |  __/ |  \__ \
|___| |_| |_|  |_|     |____/ \___| \_/ \___|_|\___/| .__/ \___|_|  |___/
                                                    |_|
                https://www.facebook.com/ITMDevelopers

Descripcion: Realize un programa que haga la suma de la secuencia 
1+(1/2)+(1/3)+(1/4)+(1/5) .... hasta llegar al (1/100)               
'''

contador = 2
suma = 1
while contador <= 100:
    contador += 1
    suma += 1 / contador

print("Suma: ", suma)