# speech-recognition-m5stickcplus2
## Micropython for M5Stack M5StickCPlus2 Board
Micropython codes for **speech recognition** and **servo control** using M5StickCPlus2.
Implementation is based on [Tinkerdoodle Project](https://tinkerdoodle.cc/user/_/notebooks/Shared/Junfeng/Speech%20Commands%20Model.ipynb) with some modifications

### Training Speech Model with Tinkerdoodle
Follow the instruction [here](https://www.tinkerdoodle.cc/user/junfeng/speech-commands.html) to get your own `speech_model.py` file

### Flash Firmware
* Download `firmware.bin` from this repo
* Load the firmware onto your device using esptool based on [this documentation](https://tinkerdoodle.cc/user/_/notebooks/Shared/Junfeng/Speech%20Commands%20Model.ipynb) (You might need to change the port setting according to your PC, for example "COM8" for Windows or "/dev/ttyUSB0" for Linux)

### Servo Control Library (optional)
`servo.py` is a library for controlling servo based on angle, check [this tutorial](https://www.upesy.com/blogs/tutorials/esp32-servo-motor-sg90-on-micropython?srsltid=AfmBOor8BqPs5Y3inoiWtjcSCKzADNxbNTkfzfmg6JtXK7Wn89qu65T1#google_vignette) for more details

### Simple main.py Example 
Here's an example main program for running the speech recognition model
  ```
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
  
  while True:
      mic.readinto(buffer)
      l, prob = speech_model.predict(buffer)
      # Print the label and the prediction probability
      print(l, prob)
      gc.collect()
```

### IDE
For further coding development and flashing your programs, use [Thonny](https://thonny.org/).
Make sure to load all the files: your own speech model, the servo library if you're going to use servo in your main program, and also your main program

### Other Example
`main.py` in this repo provides an example of controlling servo with speech commands

`speech_model.py` in this repo is my custom speech model in Bahasa with 3 keywords: "Hai Tangan" or Hi Hand as the wakeword, "Mulai" or Begin in English, and "Berhenti" or Stop in English

[![Demo](https://img.youtube.com/vi/qkBok0jFaOU/0.jpg)](https://youtube.com/shorts/qkBok0jFaOU?feature=share)
