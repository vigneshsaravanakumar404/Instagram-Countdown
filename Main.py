from requests import post
from pytz import timezone
from time import sleep
import schedule
import datetime


def calculate_time_left():
    # Get the current time in EDT
    eastern = timezone("America/New_York")
    current_time = datetime.datetime.now(eastern)

    # Make sure last_day is in EDT
    last_day = datetime.datetime(2024, 5, 31, 2 + 11, 20, 0, tzinfo=eastern)

    # Calculate the time left until the last day
    time_left = last_day - current_time

    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    minutes_left = (time_left.seconds % 3600) // 60

    # Format the time left
    time_left_formatted = f"{days_left}d {hours_left}h {minutes_left}m"
    message = f"School ends in {time_left_formatted}"

    updateStatus(message)


# Functions
def updateStatus(message):

    # Constants
    COOKIES = {
        "dpr": "1.25",
        "ig_did": "1C5E6BC1-0B73-49DF-93E9-5447F016A0F1",
        "ig_nrcb": "1",
        "datr": "0rAvZrpwxKE3QwpjL24R0K70",
        "ds_user_id": "50337138577",
        "ps_n": "1",
        "ps_l": "1",
        "csrftoken": "f4kfPdXAwIiylpwj4IXNJ1qxP4UNhBcO",
        "mid": "ZjJgNAALAAE9oJ1BgRDysnpjpxyD",
        "shbid": '"16493\\05450337138577\\0541746209252:01f7b94d210ec8de394b9396980a4c7320eae22a36c0d1f0c135bbcc7156ac04163f817f"',
        "shbts": '"1714673252\\05450337138577\\0541746209252:01f7ddc7634064a5ffb512328ada4b1ca730de387b27f56dbf9e11b9fc33bcfe6847c3cf"',
        "sessionid": "50337138577%3ADB5qGQYrdJKuZ6%3A25%3AAYfhcw1J7dY_RAEs-cR7GTgcQTirlOzzVHFYy3SkmQ",
        "rur": '"NAO\\05450337138577\\0541746225857:01f73eddf2d23dba8fb5674108849048a9f1548b4e498f3fb4eb89dc7075047246f8d3d3"',
    }

    HEADERS = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        # 'cookie': 'dpr=1.25; ig_did=1C5E6BC1-0B73-49DF-93E9-5447F016A0F1; ig_nrcb=1; datr=0rAvZrpwxKE3QwpjL24R0K70; ds_user_id=50337138577; ps_n=1; ps_l=1; csrftoken=f4kfPdXAwIiylpwj4IXNJ1qxP4UNhBcO; mid=ZjJgNAALAAE9oJ1BgRDysnpjpxyD; shbid="16493\\05450337138577\\0541746209252:01f7b94d210ec8de394b9396980a4c7320eae22a36c0d1f0c135bbcc7156ac04163f817f"; shbts="1714673252\\05450337138577\\0541746209252:01f7ddc7634064a5ffb512328ada4b1ca730de387b27f56dbf9e11b9fc33bcfe6847c3cf"; sessionid=50337138577%3ADB5qGQYrdJKuZ6%3A25%3AAYfhcw1J7dY_RAEs-cR7GTgcQTirlOzzVHFYy3SkmQ; rur="NAO\\05450337138577\\0541746225857:01f73eddf2d23dba8fb5674108849048a9f1548b4e498f3fb4eb89dc7075047246f8d3d3"',
        "dnt": "1",
        "origin": "https://www.instagram.com",
        "priority": "u=1, i",
        "referer": "https://www.instagram.com/direct/t/17851427906703548/",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua": '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-full-version-list": '"Chromium";v="124.0.6367.91", "Microsoft Edge";v="124.0.2478.67", "Not-A.Brand";v="99.0.0.0"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"15.0.0"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "x-asbd-id": "129477",
        "x-bloks-version-id": "fdd7c212ca363604f18135e94a97aa38e5b2ef8a0df1843ea9b47f5940b67fa5",
        "x-csrftoken": "f4kfPdXAwIiylpwj4IXNJ1qxP4UNhBcO",
        "x-fb-friendly-name": "usePolarisCreateInboxTrayItemSubmitMutation",
        "x-fb-lsd": "WowYdNA90R07Po98_Sf0Wr",
        "x-ig-app-id": "936619743392459",
    }

    variables = (
        '{"input":{"client_mutation_id":"1","actor_id":"17841450237332142","additional_params":{"note_create_params":{"note_style":0,"text":"'
        + message
        + '"}},"audience":0,"inbox_tray_item_type":"note"}}'
    )

    DATA = {
        "av": "17841450237332142",
        "__d": "www",
        "__user": "0",
        "__a": "1",
        "__req": "w",
        "__hs": "19845.HYP:instagram_web_pkg.2.1..0.1",
        "dpr": "1",
        "__ccg": "UNKNOWN",
        "__rev": "1013223300",
        "__s": "96remx:qp8mbb:foqrrr",
        "__hsi": "7364536335600723038",
        "__dyn": "7xeXzWwlEnwn8yEqxemh0cm5U4e1ZyUW3qi7UK360CEboG0IE6u3y4o2Gwfi0LVE4W0om78c87m0yE462mcw5Mx62G3i1ywOwv89k2C1Fwc60D82IzXw8W58jwGzEaE7622362W5olw8Xxm16wUwxwl8vwww4cwJCwLyES1TwooaQ0z8c86-3u2WE5B0bK1Iwqo5q1IQp1yUoxeufxui2qi9xi6Uf9E",
        "__csr": "gnMIN4yf584aNBFlZHIRnb5kQT23yiHkNlAFerVqunBBKFQyqGaBl4mVkiHKqt7DHyeKajAz4-V6RJpr9QX_CBABGl2oScKrDAgyQmviKFEDGlypkqHHzqyV8KbhqmvzUhhEGGJGuvgGeiw05k8IK22681IQ2aIyau1FDgGhKlO0JRh4m58Gl0Bgjxl1t05BBg3v-0cACm0iDe0kKKcwiooK7Fk3mqayoIM0GWWx51j81vBt4xi4pcYUSm3ufPG4k51lGjtPG9BomQi1qwa4US1CUhw5cgnxq3O18S0Uoy0rHge6mt2FEbpo4xBy8tw9Kh18zACCoybw2jpi0UmEhwaC2a1bzqix64E2WxaVQ2WfwVw59BDx65oN0Yw0o9o0FTw4QweB281pA0NF8bK0G83hG1Yw2FU2ewCwVw",
        "__comet_req": "7",
        "fb_dtsg": "NAcOhnodtrb9njnnUJ8aMPH_55owmkoyJsm1-3oBpH_svCZs1sQ0TzQ:17843676607167008:1714401495",
        "jazoest": "26496",
        "lsd": "WowYdNA90R07Po98_Sf0Wr",
        "__spin_r": "1013223300",
        "__spin_b": "trunk",
        "__spin_t": "1714689735",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "usePolarisCreateInboxTrayItemSubmitMutation",
        "variables": variables,
        "server_timestamps": "true",
        "doc_id": "7893338020710192",
    }

    response = post(
        "https://www.instagram.com/graphql/query",
        cookies=COOKIES,
        headers=HEADERS,
        data=DATA,
    )

    print(response.text)


calculate_time_left()
schedule.every().hour.at(":20").do(calculate_time_left)
while True:
    schedule.run_pending()
    sleep(1)
