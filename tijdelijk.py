#Opdracht 2: maak een dictionary aan
prijzen={
    "aardbei":3,
    "Vanille":4,
    "Chocolade":5
}
#Opdracht 3: Aanmaken van een variable aanbieding die aardbei vermenigvuldig met0.8
aanbieding=(prijzen["aardbei"])*0.8

#Opdracht 4: Aanmaken van een variabele reclame_tekst met zin in combinatie met vorige variable
reclame_tekst=f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"

#Opdracht 5: Aanmaken van een andere variable reclame_tekst 2 waarbij u na de dubbele punt de index plaatst van de eerste 0
reclame_tekst2=reclame_tekst[:62]

#Opdracht 6: Aanmaken van variable reclame_tekst3 die de zelfde waarde heeft al variable reclame_tekst2 maar in hoofdletters
reclame_tekst3=reclame_tekst2.upper()

#Opdracht 7: Aanmaken van een variable reclame_tekst4 die een list maakt van de variabele reclame_tekst3
reclame_tekst4=reclame_tekst3.split()

#Opdracht 8:Creër een for-loop met de elementen van de list in reclame_tekst4. gebruik de variabele el voor de loop
for el in reclame_tekst4:
    #Opdracht 9:Voeg een if-statement toe aan de for-loop waarbij de element van de list die 5 of meer karakters hebben in hoofdletters worden geprint
    if len(el)>=5:
       
       print(el.upper())

    else:

       print(el.lower())
   

   
