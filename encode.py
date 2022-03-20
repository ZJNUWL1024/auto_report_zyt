# url解码地址 http://tool.chinaz.com/tools/urlencode.aspx
# 2022/01/22


from urllib.parse import quote


def encode(loc):
    prov = loc.get("province")
    city = loc.get("city")
    region = loc.get("region")
    flag = '✰'
    location = prov + flag + city + flag + region
    url_loc = quote(location)
    return url_loc



