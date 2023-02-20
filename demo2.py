# File Name: demo2.py
# Author: Codebat_Raymond
# Date: 2/18/2023

import requests

cookies = {
    'btoken': 'HMF4QQ5XDJHINAIVO6B0Y95M9PVG434F',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1676699395',
    'hy_data_2020_id': '186631265a46c1-0f334f7c6e4db5-26031951-2073600-186631265a5f2e',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%22186631265a46c1-0f334f7c6e4db5-26031951-2073600-186631265a5f2e%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22186631265a46c1-0f334f7c6e4db5-26031951-2073600-186631265a5f2e%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1676699562',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'btoken=HMF4QQ5XDJHINAIVO6B0Y95M9PVG434F; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1676699395; hy_data_2020_id=186631265a46c1-0f334f7c6e4db5-26031951-2073600-186631265a5f2e; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22186631265a46c1-0f334f7c6e4db5-26031951-2073600-186631265a5f2e%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22186631265a46c1-0f334f7c6e4db5-26031951-2073600-186631265a5f2e%22%7D; sajssdk_2020_cross_new_user=1; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1676699562',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

#加密参数逆向
json_data = {
    'payload': 'LBc3V0I6ZGB6bXsxTCQnPRBuBhgbPj1fJDpwd2R1Tw==',
    'sig': '49AF9D32DA6AA7E5B32214EC011FE0B7',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"payload":"LBc3V0I6ZGB6bXsxTCQnPRBuBhgbPj1fJDpwd2R1Tw==","sig":"49AF9D32DA6AA7E5B32214EC011FE0B7","v":1}'
#response = requests.post(
#    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)