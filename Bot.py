from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import time
import json
import random

last = input()
api_txt = json.loads(last)
Api_Key = (api_txt["Api_Key"])
Comple = (api_txt["Comple"])
ranto = (api_txt["ranto"])

completed = 0
ordered = 0
errors = 0

#input()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
api = webdriver.Chrome(executable_path=r".\chromedriver.exe", chrome_options=chrome_options)


def Perform_1(Api_Key):
    global completed, ordered, errors
    Get1 = "https://botsapi.socpanel.com/getOrder?service_id="
    Get2 = "&account_identity="
    Get3 = "&api_token="

    rando = random.randint(1, int(ranto))
    #Rand = str(random.randint(1, 10000))

    Follow_Order = Get1+Comple+Get2+str(rando)+Get3+Api_Key
    api.get(Follow_Order)
    last = api.find_element(By.XPATH, "/html/body/pre")
    last = str(last.text)
    api_txt = json.loads(last)
    #try:
    job_follow = (api_txt["url"])
    id_follow = (api_txt["id"])
    print(job_follow)
    print(id_follow)
        #return jsonify({"Error": "No","Cash": "0.00011","Job": job_follow,"Id": id_follow})

    Check1 = "https://botsapi.socpanel.com/check?order_id="
    Check2 = "&account_identity="
    Check3 = "&api_token="

    Check_Order_Follow = Check1+str(id_follow)+Check2+str(rando)+Check3+Api_Key

    api.get(Check_Order_Follow)
    last = api.find_element(By.XPATH, "/html/body/pre")
    last = str(last.text)
    api_txt = json.loads(last)
    print(api_txt)
    #rando = random.randint(1, 30)
    completed = completed + 1

    try:
        if rando == 1:
            print("Done")
            Order_10(job_follow)
            print(str(rando))
        else:
            print(str(rando))
    except:
        time.sleep(2)

while True:
    try:
        print("stats "+str(completed)+"/"+str(errors))
        Perform_1(Api_Key)
    except:
        errors = errors + 1

#Order_10()
#while True:
#    try:
#        print("stats "+str(completed)+"/"+str(ordered)+"/"+str(errors))
#        Perform_1(Api_Key)
#    except:
#        errors = errors + 1
