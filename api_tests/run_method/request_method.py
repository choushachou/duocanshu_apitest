#encod=utf-8
import requests
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            try:
                res = requests.post(url=url,data=data,headers=header,verify=False,timeout=(1,1))
            except requests.exceptions.Timeout:
                return('error')

        else:
            try:
                res=requests.post(url=url,data=data,verify=False,timeout=(0.1,0.1))
            except requests.exceptions.Timeout:
                return('error')

        return res

    def get_main(self,url,data,header=None):
        res = None
        if header != None:
            try:
                res = requests.get(url=url,data=data,headers=header,verify=False,timeout=(0.1,0.1))
            except requests.exceptions.Timeout:
                return 'error'
        else:
            try:
                res = requests.get(url=url,data=data,verify=False,timeout=(0.1,0.1))
            except requests.exceptions.Timeout:
                return 'error'
        return res
    def run_main(self,method,url,data=None,headers=None):
        res = None
        if method.upper =="GET":
            res = self.get_main(url,data,headers)
        else:
            res = self.post_main(url,data,headers)
        if res == 'error':
            return 'error'
        else:
            return res.json(),res.status_code
        
        
if __name__ == '__main__':
    RunMethod()