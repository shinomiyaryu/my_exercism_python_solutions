def line_up(name, number):
    ending = 'th'
    if str(number).endswith('1') and not str(number).endswith('11'):
        ending = 'st'
    elif str(number).endswith('2') and not str(number).endswith('12'):
        ending = 'nd'
    elif str(number).endswith('3') and not str(number).endswith('13'):
        ending = 'rd'
    return f'{name}, you are the {number}{ending} customer we serve today. Thank you!'
    #pass
