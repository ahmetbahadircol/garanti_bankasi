import requests
import datetime
import time


def main():
    link = "https://customers.garantibbva.com.tr/internet/digitalpublic/currency-convertor-public/v1/currency-convertor/currency-list-detail"

    header = {
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": "",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "JSESSIONID=C96385B9E60D13CC72ACE3165CFE8C5C; rxVisitor=167704486979627MB2MIAP63KEI11F5NF75MS1QBP465J; _gcl_au=1.1.1368024138.1677044871; _ga=GA1.1.1054540940.1659090798; gb_opq_id=b188fa06fd60a355eceec0b6b9a0e75d; dtSa=-; _ga_C9SB1YJPFM=GS1.1.1677044871.1.0.1677045320.0.0.0; dtCookie=v_4_srv_18_sn_611926CC2FC0051FF8DC1C82037E0300_perc_100000_ol_0_mul_1_app-3Af257a4f77568aef4_1_app-3A14a5699feafd6c51_1_app-3Ad121d29f2475c438_1; dtLatC=1; dtPC=18$41060564_225h2vNQWOLEAJNUKWTKFCEMCHAUAMMBPMHGFC-0e0; rxvt=1683642860892|1683641039351",
        "Host": "customers.garantibbva.com.tr",
        "Origin": "https://webforms.garantibbva.com.tr",
        "Referer": "https://webforms.garantibbva.com.tr/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "channel": "Public",
        "client-id": "DslahJXaDW59ibNZppCm",
        "client-session-id": "dfe0-8957-29c5-490a-ac56",
        "client-type": "ArkClient",
        "dialect": "TR",
        "guid": "d9037cefeff04fdcaec40a050f41e29b",
        "ip": "127.0.0.1",
        "sec-ch-ua": """Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99""""",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "state": "",
        "tenant-app-id": "",
        "tenant-company-id": "GAR",
        "tenant-geolocation": "TUR",
        "x-client-trace-id": "d9037cefeff04fdcaec40a050f41e29b"
    }

    req = requests.get(link, headers=header)

    rate = format(req.json()[6].get("exchBuyRate"), '.4f')
    t = datetime.datetime.now()

    print(f"Time: {t} - GPB Rate: {rate}")

    with open("GPB_rates.txt", "a") as file:
        file.write(f"\n{t} - {rate}")

    time.sleep(10)


while True:
    main()
