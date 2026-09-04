def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) != 10:
        return False
    else:
        return(walk.count("n") == walk.count("s") and walk.count("w") == walk.count("e"))
