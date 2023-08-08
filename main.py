from machine import Pin, PWM, I2C
import neopixel
from microdot import Microdot, send_file, Response
from microdot_utemplate import render_template
from microdot_ssl import create_ssl_context
import time
import os


ring = neopixel.NeoPixel(Pin(15), 12)
buzzer = PWM(Pin(14), freq=1, duty=0)

def startDome(red=0, green=0, blue=0, freq=1, duty=0, soundLength=0, quietLength=0, repeat=0):
    ring.fill((red, green, blue))
    ring.write()
    logging("Ring set to (" + str(red) + "," + str(green) + "," + str(blue) + ")")
    buzzer.freq(freq)

    for i in range(repeat):
        buzzer.duty(duty)
        time.sleep(soundLength)
        buzzer.duty(0)
        time.sleep(quietLength)

    logging("Buzzer played at " + str(freq) + "hz freq, " + str(duty) + " duty, with " + str(soundLength) + "s sound length and " + str(quietLength) + "s quiet length " + str(repeat) + " time(s)")
    return

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/')
def index(request):
    return render_template('index.tpl')

@app.route('/style.css')
def css(request):
    return render_template('style.css'), {'Content-Type': 'text/css'}

@app.route('/api/<int:redValue>/<int:greenValue>/<int:blueValue>/<int:freqValue>/<int:dutyValue>/<int:soundLengthValue>/<int:quietLengthValue>/<int:repeatValue>')
def api(request, redValue, greenValue, blueValue, freqValue, dutyValue, soundLengthValue, quietLengthValue, repeatValue):
    startDome(red=redValue, green=greenValue, blue=blueValue, freq=freqValue, duty=dutyValue, soundLength=soundLengthValue, quietLength=quietLengthValue, repeat=repeatValue)
    return 'Dome Command Sent', 200

@app.route('/logs')
def log(request):
    return render_template('logs.tpl', files=os.listdir('logs'))

@app.route('/logs/<path:path>')
def logReturn(request, path):
    return send_file('logs/' + path)

@app.route('/updatedome')
def setDome(request):
    return render_template('updateDome.tpl')

sslctx = create_ssl_context('certs/cert.der', 'certs/key.der')
app.run(debug=True, ssl=sslctx)
