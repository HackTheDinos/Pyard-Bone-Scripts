import requests
import os
import time
# import mechanize
import random

#TODO: config file?

class STL_Uploader:

    def __init__(self, model_path):
        self.model_path = model_path
        self.name = os.path.basename(model_path)
        self.token = '96397003df2a4f3e87c162278977ddb5'
        self.post_endpoint = 'https://api.sketchfab.com/v2/models'
        self.pword = 'pyradactyl'
        self.post_payload = {
            "token":self.token,
            'model_file':self.model_path,
            "model_file_name":self.name,
        }
        self.file = {'model_file':open(model_path, 'rb')}
        # self.br = mechanize.Browser()
        self.uid = None
        self.status_url = None
        self.post()


    def post(self):
        if not self.status_url:
            self.post_response = requests.post(self.post_endpoint, 
                              data=self.post_payload, 
                              files=self.file)
            if self.post_response.ok:
                self.uid = self.post_response.json().get('uid')

    def get_status(self):
        if not self.uid:
            self.post()
        else:
            self.status_url = 'https://api.sketchfab.com/v2/models/{}/status?cache={}'\
                    .format(self.uid, random.randint(0,100))
            print("pinging {}".format(self.status_url))
            s = requests.session()
            res = s.get(self.status_url) #, headers={'User-Agent': 'chrome'})
            print(res.text)
            return res.json()['processing']

    def wait_for_upload(self, wait=5):
        '''
        will wait until sucess or failure
        will update sucess url
        will return url, uid tuple
        '''
        while True:
            status = self.get_status()
            print('your status is',status)
            if status in ('PROCESSING','PENDING'):
                print("status: {}, call back in {} seconds. \
                      check here: {}".format(status, wait, self.status_url))
                time.sleep(wait)
            elif status == 'SUCCEEDED':
                self.success_url = "https://sketchfab.com/models/{}/embed".format(self.uid)
                self.succesful = True
                return self.success_url 
            else: #None or FAILED
                self.succesful = False
                return None

def upload_all_STLs(root_dir):
    for dir_path, dir_names, filenames in os.walk(root_dir):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.stl':
                uploader = STL_Uploader(os.path.join(dir_path, filename))
                uploader.post()
                stl_proxy = uploader.wait_for_upload()
                break
    return stl_proxy

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        _,model_path = argv
    else:
        print("no model provided")
    uploader = STL_Uploader(model_path)
    url = uploader.wait_for_upload()
    if url:
        resp_dict = {'stl_proxy_url':url}
        print(resp_dict)
    else:
        print('sorry, something went wrong')







