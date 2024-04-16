def timer(t,t_max):
    from datetime import datetime

    end_time =  datetime.now()
    x1 = end_time - t
    x = x1.total_seconds()

    if x > t_max:
        print('Time is out! Try next time')
        exit()
