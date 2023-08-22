# Weather_SMS
Using OpenWeather's and Twilio's free API to message myself if there is forecasted rain for the next 12 hours at 8 a.m. so that I know to check the weather and schedule my run around it because lately I have been getting caught in thunderstorms :) 
I chose to automate this message at 8 a.m. through PythonAnywhere. Hid sensitive information in config.py. Twilio generates a free phone number I used to send the messages, and OpenWeather provides hourly data through OneCall 2.8, rain is based off weather ID.
