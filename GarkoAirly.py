import requests
import os


# SOCP:
# https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# INSERT send FILEPATH HERE
send_filename = "path/to/send.exe" # or ./send.py


def send_text(text):
    os.system(send_filename + " " + text)
    # print(text)


# Airly API main address
base_url = 'https://airapi.airly.eu'

# Specific API endpoint. You can change it if you want to grab different data
url = base_url + '/v2/measurements/point'

# INSERT YOUR API KEY HERE
api_key = 'Your AIRLY API key'

# Headers, no need to change those
headers = {'Accept': 'application/json',
           'apikey': api_key}

# INSERT YOUR LOCATION HERE
arguments = {'lat': 50.00,
             'lng': 20.00} #give your position as 2 floating point numbers


def main():
    response = requests.get(url, params=arguments, headers=headers)

    color_hex = response.json()['current']['indexes'][0]['color']

    color_tuple = hex_to_rgb(color_hex)

    for i in range(3):
        send_text(format(color_tuple[i], '03d'))


if __name__ == "__main__":
    main()
