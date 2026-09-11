#dette var originalt oppgave 2, men jeg brukte det samme for oppgave 3 og den viser fortsatt jordens omkrets

radius = 6371000

radius2 = 6371001

omkrets = 2*3.14*radius #formelen for omkretsen av en srikel

omkrets2 = 2*3.14*radius2

forskjell = omkrets2 - omkrets #kalkulerer begge omkretser og så finner forskjellen

print(f"tauet er {omkrets2} meter som er {forskjell} mer enn jordens omkrets som er {omkrets}")