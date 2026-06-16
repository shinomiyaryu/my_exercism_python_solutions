def response(hey_bob):
    trimmed_bob = hey_bob.strip()
    if trimmed_bob.endswith('?') and not trimmed_bob.isupper():
        return 'Sure.'
    elif trimmed_bob.isupper() and not trimmed_bob.endswith('?'):
        return 'Whoa, chill out!'
    elif trimmed_bob.isupper() and trimmed_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    elif trimmed_bob.isspace() or trimmed_bob == "":
        return 'Fine. Be that way!'
    return 'Whatever.'
    #pass
