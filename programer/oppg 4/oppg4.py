#Jeg føler at denne koden forklarer seg selv ganske bra, den bare tar bilde og lagringsyed og fjerner exif

from PIL import Image

img = Image.open("C:/Users/roygr/OneDrive - Buskerud fylkeskommune/VG2/Program fag/uke 37 python/programer/oppg 4/oppg4.jpg")

outputfold ="C:/Users/roygr/OneDrive - Buskerud fylkeskommune/VG2/Program fag/uke 37 python/programer/oppg 4/non-exif/noexif.jpg"

img.getexif().clear()

img.save(outputfold)