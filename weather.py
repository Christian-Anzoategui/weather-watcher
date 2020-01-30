import requests, json, datetime
from credentials import weather_api_key


def get_weather(location="San Marino, US"):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # complete url address
    # units=imperial(F), metric(C), and nothing is Kelvin
    complete_url = base_url + "appid=" + weather_api_key + "&q=" + location + "&units=imperial"

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # grab current time D/M/Y time
    time = datetime.datetime.now()


    response_msg = ""
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the city
        current_city = x["name"]

        # store the value corresponding
        # to the "temp" key of y
        current_temp = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_hum = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        description = z[0]["description"]

        response_msg = "\nLocation: {} \nTemperature: {} \nHumidity: {} \nDescription: {}" \
            .format(location, str(current_temp), str(current_hum), str(description))

    else:
        response_msg = "\nCity Not Found "

    return "\n" + time.strftime("%c") + response_msg


