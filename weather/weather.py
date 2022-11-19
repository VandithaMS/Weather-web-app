from bs4 import BeautifulSoup
import requests

def get_weather(city):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+{city}').text

    soup = BeautifulSoup(html_content, 'html.parser')

    result = dict()

    result['location'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    result['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    result['time'], result['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split('\n')
    return result


def image(time):
    time=time.strip()[len(time)-2:]
    print(time)
    if time=="am":
        img="https://media.istockphoto.com/photos/mountain-landscape-picture-id517188688?k=20&m=517188688&s=612x612&w=0&h=i38qBm2P-6V4vZVEaMy_TaTEaoCMkYhvLCysE7yJQ5Q="
    else:
        img="https://cdn.dribbble.com/users/1735338/screenshots/6186224/media/9f6e4b5b13ec38b64068d721a4426702.jpg?compress=1&resize=800x600&vertical=top"
    return img