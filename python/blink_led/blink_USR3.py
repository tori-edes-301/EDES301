# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blink USR3 LED
--------------------------------------------------------------------------
License:
Copyright 2026 - Tori Barrera

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
may be used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Blink the USR3 LED at 5 Hz.

--------------------------------------------------------------------------
"""

# control time LED is on/off
import time

# control the PocketBeagle GPIO/LED
import Adafruit_BBIO.GPIO as GPIO 

# setting up USR3 LED as an output 
GPIO.setup("USR3", GPIO.OUT)

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

# making LED blink at 5 Hz 
# one cycle turns on and off 
# for 5 cycles/sec each cycle takes 0.2 sec 
# each half of cycle (on and off) takes 0.1 sec 

while True: 
   
    # turns LED on 
    GPIO.output("USR3", GPIO.HIGH)
    time.sleep(0.1) 
    
    # turns LED off 
    GPIO.output("USR3", GPIO.LOW)
    time.sleep(0.1)