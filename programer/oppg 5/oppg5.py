import re

with open("C:/Users/roygr/OneDrive - Buskerud fylkeskommune/VG2/Program fag/uke 37 python/programer/oppg 5/EleverVG2IT.txt", "r") as a:
        

    txt = a.readlines()
    for i in range(len(txt)): #for-loop for å finne linjen navnet er på
        navn = re.search("^Blake.*Grutchfield$", txt[i]) #slik at den samler in hele navnet bruker jeg ^ (start) og $ (slutt)
        if navn:
            print(f"{navn.group()} can be found on line {i+1} ")
