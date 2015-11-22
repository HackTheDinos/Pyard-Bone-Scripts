import requests
import os
import time

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
        self.post()


    def post(self):
        self.post_response = requests.post(self.post_endpoint, 
                          data=self.post_payload, 
                          files=self.file)
        if self.post_response.ok:
            self.uid = self.post_response.json().get('uid')

    def get_status(self):
        self.status_url = 'https://api.sketchfab.com/v2/models/{}/status?'\
                .format(self.uid)
        res = requests.get(self.status_url, headers={'User-Agent': 'firefox'})
        print(res.text)
        return res.json()['processing']

    def wait_for_upload(self):
        '''
        will wait until sucess or failure
        will update sucess url
        will return url, uid tuple
        '''
        while True:
            status = self.get_status()
            print('your status is',status)
            if status in ('PROCESSING','PENDING'):
                print("status: {}, call back in 20 seconds. \
                      check here: {}".format(status, self.status_url))
                time.sleep(20)
            elif status == 'SUCCEEDED':
                self.success_url = "https://sketchfab.com/models/{}/".format(uid)
                self.succesful = True
                print("woohoo!, it worked, go to {}".format(url))
                return self.url 
            else: #None or FAILED
                self.succesful = False
                return None


# then the get requests to check on it

# success_url = 'https://sketchfab.com/models/{}'.format(uid)

# waiting = True
# while waiting:
#     poll_response = requests.get(poll_url, params=token)
#     status = poll_response.json().get('processing')
#     print status
#     if status in ('PROCESSING','PENDING'):
#         print "status: {}, call back in 30 seconds".format(status)
#         time.sleep(30)
#     elif status == 'SUCCEEDED':
#         url = "https://api.sketchfab.com/v2/models/{}/".format(uid)
#         print "yeah, it worked, go to {}".format(url)
#         break
#     else: #None or FAILED
#         break
#
if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        _,model_path = argv
    else:
        print("no model provided")
    uploader = STL_Uploader(model_path)
    url = uploader.wait_for_upload()
    if url:
        print('{"stl_proxy_url":{}}'.format(url))
    else:
        print('sorry, something went wrong')







