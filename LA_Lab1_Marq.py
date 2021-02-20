def grades_average(name, course, prelims, midterms, finals, border):

    final_average = (float(prelims) + float(midterms) + float(finals))/3
    final_grade = round(final_average, 2)

    Happy = ("\U0001F600 :>> " + "Congrats on getting a high grade!")
    Laughing = ("\U0001F606 :| " + "Congrats on getting a passing grade!")
    Sad = ("\U0001F62D :<< " + "Never give up!")

    if final_grade > 70.00:
        emoji = Happy
    elif final_grade == 70.00:
        emoji = Laughing
    else:
        emoji = Sad

    print(("Hi, " + name + " from " + course + " department!") +
        ("\nYour Prelims Grade is " + prelims) +
        ("\nYour Midterms Grade is " + midterms) +
        ("\nYour Finals Grade is " + finals) +
        ("\nAnd your Final Average is " + str(final_grade)) +
        ("\n"+ emoji) + (("\n⊹˙⋆°••°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹✭⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°••°⋆˙⊹")))

print("⊹˙⋆°••°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹✭⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°••°⋆˙⊹")
grades_average(input("What's your name? "),
                input("What's your course? "),
                input("What's your Prelims Grade? "),
                input("What's your Midterms Grade? "),
                input("What's your Finals Grade? "),
                print("⊹˙⋆°••°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹•°⋆˙⊹✭⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°•⊹˙⋆°••°⋆˙⊹"))