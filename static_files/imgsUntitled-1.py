import requests

def get_proxy():
    return requests.get("https://api.linux-do-proxy.com/get/").json()

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = "128.106.14.227:9401"
    while retry_count > 0:
        try:
            html = requests.get('http://ipinfo.io', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    return None

print(getHtml())