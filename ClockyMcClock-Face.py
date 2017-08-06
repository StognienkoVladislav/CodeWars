

def what_time_is_it(angle):
    
    if angle > 360:
        angle -= 360

    if angle == 0 :
        angle = 360

    time_min = angle*2
    time_hours = time_min//60
    time_min = time_min - time_hours*60
    time_hours = int(time_hours)
    time_min = int(time_min)

    if time_hours == 0:
        time_hours = 12

    if time_hours < 10:
        time_hours = "0{}".format(time_hours)

    if time_min < 10:
        time_min = "0{}".format(time_min)    
    time = str(time_hours) + ':' + str(time_min)

    return time


def what_time_is_itPro(angle):
    h = angle//30
    m = (angle%30)*2
    return '%02d:%02d'%(h,m) if h else '12:%02d'%m


def what_time_is_itPro2(angle):
    hours, minutes = int(agnle // 30), int((angle % 30) * 2)
    if hours == 0: hours = 12
    return '{:0>2}:{:0>2}'.format(hours, minutes)

if __name__ == '__main__':
    print(what_time_is_it(0), '12:00')
    print(what_time_is_it(250.788), '08:21')
    print(what_time_is_it(360), '12:00')
    print(what_time_is_it(90), '03:00')
    print(what_time_is_it(180), '06:00')
    print(what_time_is_it(270), '09:00')
    print(what_time_is_it(30), '01:00')