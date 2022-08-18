import requests

async def Get_Tractor_Q(tractor_actions):
    url = 'http://192.168.1.11:80/index/'
    
    client = requests.session()
    # Retrieve the CSRF token first
    client.get(url)  # sets cookie
    #print(client.cookies)
    if 'csrftoken' in client.cookies:
        # Django 1.6 and up
        csrftoken = client.cookies['csrftoken']
    else:
        # older versions
        csrftoken = client.cookies['csrf']
        
    #Prepare data to send
    data = {}
    data['tractor_actions'] = tractor_actions
    data['csrfmiddlewaretoken'] = csrftoken
    r = client.post(url, data=data, headers=dict(Referer=url))
    print(r)
    
    return r