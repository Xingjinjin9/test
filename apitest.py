import json

import requests

url1='https://test-edu-hfsaas.jiangweikj.com/api-user/v1/login/app/login'
data={
        "tyg": "i996needMoney996",
        "cipherText": "8Bu2tQxu7DFso7mzM5QmCuXHGaSUSY/2uQFI00EzlOBJ1tW17pxKKjMPMz0SwQhlde2sODD8u0QZYwZU2jWxXGkqz3l4qAn7fb/WWwn43dtrcagMbNCHzIDJ3VGanznUsIKK4fSxdtEa2dfHMgG02AXPyo2nq6Ap9/qCASTedwFoOdnCW2UBWsqjeQSjm5HGU3P9PkfzBlJCL3RU4ugmq1eTf+9QWj8b3DGYyxgAsl6ClOsFzze5L34iOknWYvM1fmS2A4Bwemn3+72KoMJU6qE3uhX0tWGISx+H1c8So5orFlflc41UPo5/pLgJGZK/YXQx+LZULV8p5evVyYJA4ixYP2+qPNbRSaGlstqbWYCFmuC46Z13KdsxnNW2xviD"
}
res=requests.post(url1,json=data)
#print(res.text)
#res1=json.loads(res.text)
#print(res1)

url2='https://dev-edu-hfsaas.jiangweikj.com/api-common/v1/sys/hf_decrypt'
data=json.loads(res.text)
res_login=requests.post(url=url2,json=data)
token=json.loads(res_login.text)['model']['token']
#print(token)

url3='https://test-edu-hfsaas.jiangweikj.com/api-kg-fee/program_kg_app/v1/get_program_fee_info?'
headers={
        "token":token
}
res_free=requests.get(url=url3,headers=headers)
print(res_free.text)