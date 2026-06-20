def resistor_label(colors):
    code_colors = {'black':'0','brown':'1','red':'2','orange':'3','yellow':'4','green':'5','blue':'6','violet':'7','grey':'8','white':'9'}
    tolerances = {'grey': '0.05','violet':'0.1','blue':'0.25','green':'0.5','brown':'1','red':'2','gold':'5','silver':'10'}
    values = ''
    count = 0
    for color in colors:
        count += 1
        if count > 2 and len(colors) == 4:
            values += '0' * int(code_colors[color])
            break
        if count > 3 and len(colors) == 5:
            values += '0' * int(code_colors[color])
            break
        else:
            values += code_colors[color]
            
    if colors[-1] != 'black':
        tolerance_value = tolerances[colors[-1]]

            
    if values[0] == '0' and len(colors) > 3:
        values = values[1:]
    if values[0] == '0':
        return '0 ohms'
    if values.count('0') == 9:
        return values[:-9] + f' gigaohms ±{tolerance_value}%'
    if values.count('0') < 9  and values.count('0') >= 6:
        if len(values[:-6]) > 3:
            result = int(values[:-6]) / 1000
            return f'{result} gigaohms ±{tolerance_value}%'
        return values[:-6] + f' megaohms ±{tolerance_value}%'
    if values.count('0') < 6 and values.count('0') >= 3:
        if len(values[:-3]) > 3:
            result = int(values[:-3]) / 1000
            return f'{result} megaohms ±{tolerance_value}%'
        return values[:-3] + f' kiloohms ±{tolerance_value}%'
    if len(values) > 3:
        result = int(values) / 1000
        return f'{result} kiloohms ±{tolerance_value}%'
    return values + f' ohms ±{tolerance_value}%'
    #pass