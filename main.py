from machine import Pin, PWM, I2C
import neopixel
import microdot
from microdot_utemplate import render_template
from microdot_ssl import create_ssl_context
import time
import os
import uasyncio
from microdot_asyncio import Microdot, send_file, Response

ring = neopixel.NeoPixel(Pin(15), 12)
buzzer = PWM(Pin(14), freq=1, duty=0)

async def startDome(red=0, green=0, blue=0, freq=1, duty=0, soundLength=0, quietLength=0, repeat=0):
    ring.fill((red, green, blue))
    ring.write()
    logging("Ring set to (" + str(red) + "," + str(green) + "," + str(blue) + ")")
    buzzer.freq(freq)

    for i in range(repeat):
        buzzer.duty(duty)
        await uasyncio.sleep(soundLength)
        buzzer.duty(0)
        await uasyncio.sleep(quietLength)
    
    logging("Buzzer played at " + str(freq) + "hz freq, " + str(duty) + " duty, with " + str(soundLength) + "s sound length and " + str(quietLength) + "s quiet length " + str(repeat) + " time(s)")
    return

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/')
async def index(request):
    return render_template('index.tpl')

@app.route('/style.css')
async def css(request):
    return render_template('style.css'), {'Content-Type': 'text/css'}

@app.route('/api/<int:redValue>/<int:greenValue>/<int:blueValue>/<int:freqValue>/<int:dutyValue>/<int:soundLengthValue>/<int:quietLengthValue>/<int:repeatValue>')
async def api(request, redValue, greenValue, blueValue, freqValue, dutyValue, soundLengthValue, quietLengthValue, repeatValue):
    uasyncio.create_task(startDome(red=redValue, green=greenValue, blue=blueValue, freq=freqValue, duty=dutyValue, soundLength=soundLengthValue, quietLength=quietLengthValue, repeat=repeatValue))
    return 'Dome Command Sent', 200

@app.route('/logs')
async def log(request):
    return render_template('logs.tpl', files=os.listdir('logs'))

@app.route('/logs/<path:path>')
async def logReturn(request, path):
    return send_file('logs/' + path)

@app.route('/updatedome')
async def setDome(request):
    return render_template('updateDome.tpl')

app.run(debug=True, port=80)
