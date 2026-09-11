import pyfiglet
import time

ascii1 = pyfiglet.figlet_format("IM VG2 IT!")
ascii2 = pyfiglet.figlet_format("The best place to learn IT!")
ascii3 = pyfiglet.figlet_format("Do you like IT?") #lager de 3 første linjene
print(ascii1)
time.sleep(1)
print(ascii2)
time.sleep(1)
print(ascii3)
answer= input("") #printer linjene med tid imellom og venter på svar
if answer == "yes:" or answer == "Yes" or answer == "YES":
    ascii4 = pyfiglet.figlet_format("Then you should start IT!")
else:
    ascii4 = pyfiglet.figlet_format("Then you should start IT so that you learn to like IT!")
print(ascii4)

