import gc
import speech_model
from machine import I2S, Pin
import array
import time
from servo import Servo

# Use the M5StickC built-in microphone.
mic = I2S(I2S.NUM0, ws=Pin(0), sdin=Pin(34), mode=I2S.MASTER_PDW,
    dataformat=I2S.B16, channelformat=I2S.ONLY_LEFT,
    samplerate=16000, dmacount=16, dmalen=256)

buffer = array.array("h", 4096 * [0])
label = ''
label_index = -1

gc.collect()


motor=Servo(pin=26) # A changer selon la broche utilisée
motor.move(0) # tourne le servo à 0°
time.sleep(0.5)

current_angle = 0
target_angle = 180
step = 5
label = '[OTHER]'

def move_servo():
    global current_angle, target_angle
    
    if current_angle < target_angle:
        current_angle += step
        print(current_angle)
        motor.move(current_angle)
    elif current_angle > target_angle:
        current_angle -= step
        print(current_angle)
        motor.move(current_angle)

while True:
    mic.readinto(buffer)
    l, prob = speech_model.predict(buffer)
    print(l, prob)
    gc.collect()
    
    if l == '[OTHER]' or prob <= 70:
        if label != '[OTHER]':
            move_servo()
        continue
    
    label = l

    if l == 'Mulai':
        target_angle = 180
    elif l == 'Berhenti':
        target_angle = 0
        
    move_servo()