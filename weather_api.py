import config
from pyowm import OWM

thunderstorm = u'\U0001F4A8'    # Code: 200's, 900, 901, 902, 905
drizzle = u'\U0001F4A7'         # Code: 300's
rain = u'\U00002614'            # Code: 500's
snowflake = u'\U00002744'       # Code: 600's snowflake
snowman = u'\U000026C4'         # Code: 600's snowman, 903, 906
atmosphere = u'\U0001F301'      # Code: 700's foogy
clearSky = u'\U00002600'        # Code: 800 clear sky
fewClouds = u'\U000026C5'       # Code: 801 sun behind clouds
clouds = u'\U00002601'          # Code: 802-803-804 clouds general
hot = u'\U0001F525'             # Code: 904
defaultEmoji = u'\U0001F300'    # default emojis


owm = OWM(config.open_weather_id) 
mgr = owm.weather_manager()

def forecast_manual(city_name):
    observation = mgr.weather_at_place(city_name)
    w = observation.weather
    print(observation.to_dict())
    print(w.weather_icon_url)
    msg, sticker_id = process_weather_data(observation)
    return(msg, sticker_id)

def forecast_location(latitude, longitude):
    observation = mgr.weather_at_coords(latitude, longitude)
    w = observation.weather
    print(observation.to_dict())
    print(w.weather_icon_url)
    msg, sticker_id = process_weather_data(observation)
    return(msg, sticker_id)

def process_weather_data(observation):
    w = observation.weather
    msg = getEmoji(w.weather_code)
    msg += getEmoji(w.weather_code)
    msg += getEmoji(w.weather_code)
    msg += "\nThe weather conditions at "
    msg += observation.location.name
    msg += " are the following:\n"
    msg += w.status 
    msg += "\nCurrent temperature is "
    temp = w.temperature('celsius')["temp"]
    feels_temp = w.temperature('celsius')["feels_like"]
    msg += str(temp) + "°C, and feels like "
    msg += str(feels_temp) + "°C\n"
    msg += getEmoji(w.weather_code)
    msg += getEmoji(w.weather_code)
    msg += getEmoji(w.weather_code)
    sticker_id = getSticker(w.weather_code)
    return msg, sticker_id

def getEmoji(weather_code):
    if weather_code:
        if str(weather_code)[0] == '2' or weather_code == 900 or weather_code==901 or weather_code==902 or weather_code==905:
            return thunderstorm
        elif str(weather_code)[0] == '3':
            return drizzle
        elif str(weather_code)[0] == '5':
            return rain
        elif str(weather_code)[0] == '6' or weather_code==903 or weather_code== 906:
            return snowflake + ' ' + snowman
        elif str(weather_code)[0] == '7':
            return atmosphere
        elif weather_code == 800:
            return clearSky
        elif weather_code == 801:
            return fewClouds
        elif weather_code==802 or weather_code==803 or weather_code==803:
            return clouds
        elif weather_code == 904:
            return hot
        else:
            return defaultEmoji

    else:
        return defaultEmoji

def getSticker(weather_code):
    if weather_code:
        if str(weather_code)[0] == '2' or weather_code == 900 or weather_code==901 or weather_code==902 or weather_code==905:
            return config.thunderstorm_id
        elif str(weather_code)[0] == '3':
            return config.drizzle_id
        elif str(weather_code)[0] == '5':
            return config.rain_id
        elif str(weather_code)[0] == '6' or weather_code==903 or weather_code== 906:
            return config_id.snowflake_id
        elif str(weather_code)[0] == '7':
            return config.atmosphere_id
        elif weather_code == 800:
            return config.clearSky_id
        elif weather_code == 801 or weather_code==802 or weather_code==803 or weather_code==803:
            return config.clouds_id
        elif weather_code == 904:
            return config.hot_id
        else:
            return config.love_id

    else:
        return config.love_id
