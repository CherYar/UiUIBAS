import keyboard  
def on_key_event(event):
    if event.name == 'q':
        print('Клавиша "q" нажата. Программа завершена.')
        return False
keyboard.hook(on_key_event)
keyboard.wait()
