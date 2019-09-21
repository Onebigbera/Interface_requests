# -*-coding:utf-8 -*-
# File :interface.py
# Author:George
# Date : 2019/9/20
# motto: Someone always give up while someone always try!
"""
    Interface test project demo with Python
"""
import requests
import time

base_url = 'http://httpbin.org'


def basic_requests(url):
    """
    Test the basic http methods
    :param url:
    :return:
    """
    # get requests
    response = requests.get(base_url+'/get')
    print(response.status_code)

    time.sleep(3)
    print("Sleep 3 seconds")
    # post requests
    response = requests.post(base_url+'/post')
    print(response.status_code)

    time.sleep(2)
    print("Sleep 3 seconds")
    response = requests.put(base_url + '/put')
    print(response.status_code)

    time.sleep(2)
    print("Sleep 3 seconds")
    response = requests.delete(base_url + '/delete')
    print(response.status_code)


def get_request_with_parameters():
    """
    get requests with parameters in dictionary form, params in requests strings query sting
    :return:
    """
    param_data = {'account': '张xx', 'password': 'this is a password'}
    response = requests.get(base_url + '/get', params=param_data)
    print(response)
    print(response.url)
    print(response.status_code)


def post_requests_with_parameter():
    """
    post requests with parameters  in dictionary format  params in requests body  query body
    :return:
    """
    format_date = {"sequence": 3, 'level': 'common'}
    response = requests.post(base_url + '/post', data=format_date)
    print(response.status_code)
    print(response.text)


def set_headers():
    """
    Set fatal headers to avoid auth  set user-agent
    :return:
    """
    format_data = {'sequence': 2, 'Level': 1}
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.post(base_url + '/post', data=format_data, headers=headers)
    print(response.text)
    print(response.json())
    print(response.status_code)


def set_cookies():
    """Set cookies to avoid auth"""
    cookie = {'user': 'george', 'password': '1123abc'}
    response = requests.get(base_url + '/cookies', cookies=cookie)
    print(response.status_code)
    print(response.text)

    # request baidu
    response = requests.get('https://baidu.com')

    print(response.cookies)
    print(type(response.cookies))
    # to traversal a dict  use for key,value in dict.items() method
    for key, value in response.cookies.items():
        print(key + ':' + value)


def timeout_handle():
    """
    set timeout  use timeout param
    :return:
    """
    response = requests.get(base_url + '/get', params=None, timeout=3)
    print(response.json)
    print(response.status_code)


def upload_file():
    """
    upload an image of N
    :return:
    """
    # Define an image object
    image_path = r'F:\Testing_Development\Projects\Interface_requests\Interface_requests\upload_files\Napoleon Bonaparte.jpg'
    file = {'file': open('Napoleon Bonaparte.jpg', 'rb')}
    # response = requests.post(base_url + '/post', files=file, timeout=3)
    response = requests.post(base_url + '/post', files=file)
    print(response.status_code)
    print(response.text)


def session_relevance():
    """
    Session can relevance the relationship between interfaces
    :return:
    """

    # instantiation a session object in the first step
    session = requests.Session()

    # interface 1
    response = session.get(base_url + '/cookies/set/user/tom')
    print(response.text)

    # get the cookie in the same domain
    response = session.get(base_url + '/cookies')
    print(response.cookies)
    print(response.text)
    # In fact this is the rule you must obey in the test website
    # response = session.get(base_url + '/cookies/set/user/george')
    # print(response.status_code)
    # print(response.text)


def certificate_auth():
    """
    whether to open SSL certificate auth
    :return:
    """
    url = 'https://www.12306.cn'
    response = requests.get(url, verify=False)
    print(response.status_code)
    print(response.text)


def identify_num_simulate():
    """
    simulate ip address to avoid check form service website
    :return:
    """
    # http / https  ip:port
    proxy = {'http': 'http://112.85.165.113:9999'}
    response = requests.get(base_url + '/get', proxies=proxy)
    print(response.status_code)
    print(response.text)


def identify_auth():
    """
    whether to open identify auth
    :return:
    """
    from requests.auth import HTTPBasicAuth
    from requests.auth import HTTPDigestAuth
    # HTTPBasicAuth Auth Method
    response = requests.get(base_url + '/basic-auth/51zxw/8888', auth=HTTPBasicAuth('51zxw', '8888'))
    print(response.status_code)
    print(response.text)

    # HTTPDigestAuth Auth Method
    response = requests.get(base_url + '/digest-auth/auth/zwx/6666', auth=HTTPDigestAuth('zwx', '6666'))
    print(response.status_code)
    print(response.text)
    print(response.json())


def stream_handler():
    """
    iter_lines()
    :return:
    """
    import json
    response = requests.get(base_url + '/stream/10', stream=True)
    print(response.text)
    if response.encoding is None:
        response.encoding = 'utf-8'

    for line in response.iter_lines(decode_unicode=True):
        if line:
            line = json.loads(line)
            print(line['id'])


if __name__ == "__main__":
    url = base_url
    # basic_requests(url)
    # get_request_with_parameters()
    # post_requests_with_parameter()
    # set_headers()
    # set_cookies()
    # timeout_handle()
    # upload_file()
    # session_relevance()
    # certificate_auth()
    # identify_num_simulate()
    # identify_auth()
    stream_handler()