from flask import Flask, Response
from flask_restful import Resource, Api
import datetime
import Adafruit_DHT
import threading

app = Flask(__name__)
api = Api(app)

# It returns a simple YES to check if the App is working
@app.route('/is/it/working')
def isitworking():
    return Response('YES', status=200)

# API REST to return AM2302 Temperatures
class api_temperature(Resource):
    temperature, humidity = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

    def cur_temp(self): 
        if self.temperature is not None:
            return ("%.2f" % self.temperature)
        else:
            return ("Error")

    def cur_hum(self):
        if self.humidity is not None:
            return ("%.2f" % self.humidity)
        else:
            return ("Error")

    def get(self, **kwargs):

        self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

        return {'current_temp': self.cur_temp(),
        'current_humidity': self.cur_hum()#,
        #'current_time': datetime.timedelta(hours=h,minutes=m),
        #'next_update': time.strftime("%H:" + "%M" + "%S")
        }

api.add_resource(api_temperature, '/api/temperature/')

