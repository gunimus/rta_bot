def get_time(time):
    m, s = divmod(time.seconds, 60)
    h, m = divmod(m, 60)
    hour = str(h)
    mins = str(m)
    sec = str(s)
    ms = str(time.microseconds)[:-3]
    if h != 0:
        if time.microseconds != 0:
            return hour + 'h ' + mins.zfill(2) + 'm ' + sec.zfill(2) + 's ' + ms.zfill(3) + 'ms'
        else:
            return hour + 'h ' + mins.zfill(2) + 'm ' + sec.zfill(2) + 's'
    else:
        if time.microseconds != 0:
            return mins + 'm ' + sec.zfill(2) + 's ' + ms.zfill(3) + 'ms'
        else:
            return mins + 'm ' + sec.zfill(2) + 's'

def get_place(place):
    place = str(place)
    if place == '11' or place == '12' or place == '13':
        return place + 'th'
    elif place[-1] == '1':
        return place + 'st'
    elif place[-1] == '2':
        return place + 'nd'
    elif place[-1] == '3':
        return place + 'rd'
    else:
        return place + 'th'