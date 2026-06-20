def label(colors):
    code_colors = {'black':'0','brown':'1','red':'2','orange':'3','yellow':'4','green':'5','blue':'6','violet':'7','grey':'8','white':'9'}
    values = ''
    count = 0
    for color in colors:
        count += 1
        if count > 2:
            values += '0' * int(code_colors[color])
            break
        else:
            values += code_colors[color]
    if values[0] == '0':
        values = values[1:]
    if values[0] == '0':
        return '0 ohms'
    if values.count('0') == 9:
        return values[:-9] + ' gigaohms'
    if values.count('0') < 9  and values.count('0') >= 6:
        return values[:-6] + ' megaohms'
    if values.count('0') < 6 and values.count('0') >= 3:
        return values[:-3] + ' kiloohms'
    return values + ' ohms'
    #pass