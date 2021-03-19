"""Count-down timer with notifications."""

import time

if __name__ == "__main__":
    while True:
        uin = input('Enter seconds >> ')
        notification_text = input('Enter a notification >> ')

        try:
            when_to_stop = abs(int(uin))
        except KeyboardInterrupt:
            break
        except:
            print('Not a number!')

        while when_to_stop > 0:
            m, s = divmod(when_to_stop, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + \
                ":" + str(s).zfill(2)
            print(time_left + '\r', end='')
            time.sleep(1)
            when_to_stop -= 1

        if len(notification_text) < 8:
            print(notification_text + '        ')
        else:
            print(notification_text + '\n')
