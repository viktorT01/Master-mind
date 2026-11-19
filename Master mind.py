import random

print("Datorn kommer slumpa fram en kod på 4 siffror mellan 1-6.")
print("Du ska försöka gissa denna kods siffror på max 12 drag")
print("Efter respektive gissning så kommer du få en respons:")
print("För varje gissad korrekt siffra på korrekt plats i koden: ✓")
print("För varje gissad korrekt siffra på fel plats i koden: □")
print("För de siffror som inte finns med i koden ges ingen markering.\n")
    
print("Exemple: om de slumpade talen är 2315")
print("och du gissar  3165")
print("så blir responsen ✓□□\n")

print("Du får välja mellan två svårighetsnivåer:")
print("Lättare nivå: Alla siffror är garanterat olika")
print("Svårare nivå: Det kan finnas upprepningar av en eller flera siffror")

while True:

    while True:
        svar = input("\nVälj spelläge lätt(1) eller svår(2): ")
        print("")

        if svar == "1" or svar == "2":
            break

        print("Ogiltigt val! Försök igen.")

    kod = ""

    if svar == "1":
        while len(kod) < 4:
            siffra = str(random.randint(1,6))

            if siffra not in kod:
                kod += siffra
    else:
        kodlist = [random.randint(1, 6) for i in range(4)]
        kod = str(kodlist[0])+str(kodlist[1])+str(kodlist[2])+str(kodlist[3])

    def get_feedback(guess, kod):
        feedback = []
        remaining = {}

        for i in range(4):
            if guess[i] == kod[i]:
                feedback.append("✓")
            else:
                digit = kod[i]
                remaining[digit] = remaining.get(digit, 0) + 1

        for i in range(4):
            if guess[i] != kod[i]:
                digit = guess[i]

                if remaining.get(digit, 0) > 0:
                    feedback.append("□")
                    remaining[digit] -= 1
        return feedback

    guesses = []
    feedbacks = []

    for attempt in range(12):

        print("\nDrag #        Gissning           Feedback")
        print(70*"-")
        print("")

        for i in range(11, -1, -1):
            if i < len(guesses):
                print(f"{i+1:>2}           {guesses[i]:>10}                 {' '.join(feedbacks[i])}")
                print("")
            else:
                print(f"{i+1:>2}")
                print("")

        while True:
            guess = input("Ange gissning med fyra siffror -> ")

            if len(guess) != 4 or not guess.isdigit():
                print("Skriv exakt fyra siffror!")
            elif any(digit not in "123456" for digit in guess):
                print("Endast siffrorna 1-6 är tillåtna!")
            elif svar == "1" and len(set(guess)) != 4:
                print("Du måste använda fyra olika siffror!")
            else:
                break

        feedback = get_feedback(guess, kod)

        guesses.append(guess)
        feedbacks.append(feedback)

        if guess == kod:
            print("Snyggt :-)")
            print("Du klarade det på", attempt + 1, "försök!")
            break

    else:
        print("Nästa gång går det bättre! Den rätta koden var:", kod)

    print("\nSpelet är slut!")

    while True:
        spela_igen = input("\nVill du spela igen? (j/n): ").lower()

        if spela_igen == "j":
            print("\nNu börjar ett nytt spel!\n")
            break

        elif spela_igen == "n":
            print("Tack för att du spelade!")
            break

        else:
            print("Skriv \"j\" eller \"n\"!")

    if spela_igen == "n":
        break
