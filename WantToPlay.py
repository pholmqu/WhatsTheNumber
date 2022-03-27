def WantToPlay():
    play = ""
    while play != "yes" and play != "no":
        try:
            play = (input("Do you want to play \"What's the Number?\" ")).lower()
        except ValueError:
            print("Please answer yes or no.")
    return(play)