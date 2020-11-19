#coding : utf - 8
import json
import os
path = os.path.dirname(os.path.abspath(__file__))#获得上一级路径
class OperationJson:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = path+'\\cookie.json'
        else:
            self.file_path = file_path
            
    def read_data(self):
        #读取json文件,"rb"   以二进制读方式打开，只能读文件 ， 如果文件不存在，会发生异常
        with open(self.file_path,'rb') as fp:  
            data = json.load(fp)
            
            return data
    def get_data(self,id):
        #根据关键字读取数据
        if id =='':
            return None
        else:
            return self.read_data()[id]
    def write_data(self,data):
        #r du w xie
        with open(self.file_path,'w') as fp:
            fp.write(json.dumps(data))

if __name__ == '__main__':
    res = OperationJson()
    #re = res.get_data('token')
    re = res.read_data()
    print(re)