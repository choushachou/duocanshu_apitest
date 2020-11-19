# coding : utf -8
import sys,os
path=os.path.abspath(os.path.join(os.getcwd(), "../.."))#获得上一级的上一级目录
sys.path.append(path)
from api_tests.data_method.get_data import GetData
from api_tests.run_method.request_method import RunMethod
from api_tests.util.excel_util import OperationExcel
from api_tests.util.json_util import OperationJson
from api_tests.data_method.panduan import PanDuan
from api_tests.depend.depend_data import DependdentData
import json
import traceback
from api_tests.logs.user_log import UserLog
class RunTest:
    def __init__(self):
        self.run_method= RunMethod()
        self.data=GetData()
        self.excel=OperationExcel()
        self.panduan=PanDuan()
        self.log = UserLog()
        #self.closelog = UserLog().close_handle()
    def running(self):
        try:
            #程序执行的主入口
            rows_count=self.data.get_case_lines()#获取表格总行数

            for i in range(2,rows_count): #从第二行开始
                self.log.get_log().info(i)
                is_run = self.data.get_is_run(i)
                if is_run:  # 如果是yes就执行，是no不执行

                    url = self.data.get_request_url(i)
                    method = self.data.get_request_method(i)
                    header = self.data.is_header(i)
                    data = json.loads(self.data.get_request_data(i))#将字符产转为字典
                    depend_case = self.data.is_depend(i)
                    num_method = self.data.get_assert_method(i)
                    expect = self.data.get_expect_data(i)
                    if header == 'write': #通过账号获得token，将token写道json文件中
                        #res = self.run_method.run_main(method,url,data)
                        res = self.excel.h_token(i,7)


                    elif header == 'yes':#到json文件中获得token，执行接口时用
                        c_json = OperationJson()
                        headers = c_json.read_data()
                        if depend_case != None:  # 执行数据依赖
                            self.depend_data = DependdentData(depend_case)
                            depend_response_data = self.depend_data.get_data_for_key(i)  # 获取的依赖响应数据value
                            depend_key = self.data.get_depend_field(i)  # 获取下一个接口要依赖的key
                            #将两个列表一一对应转成字典
                            nvs = zip(depend_key,depend_response_data)
                            nvDict = dict ((depend_key,depend_response_data) for depend_key,depend_response_data in nvs)
                            for k,v in nvDict.items():
                                data[k] = v
                        res = self.run_method.run_main(method,url,data,headers)

                    else:#不带header
                        res = self.run_method.run_main(method,url,data)

                    #判断是否超时，没有超时写入结果
                    if res == 'error':
                        self.data.write_result(i,'超时')
                    else:
                        code = str(res[1])
                        res1 = str(res[0])
                        self.data.write_code(i,code)

                        #通过判断方式写执行结果
                        self.panduan.assert_result(num_method,i,expect,res1,code)


        except Exception as e:
            self.log.get_log().error(traceback.format_exc())
        self.log.close_handle()
if __name__ == '__main__':
    run = RunTest()
    run.running()
# if self.data.get_assert_method(i) == 1:#状态码判断
                        #     expect = str(self.data.get_expect_data(i))[:3]
                        #     p = self.panduan.if_panduan(expect,code)
                        #     if p == True:
                        #         self.data.write_result(i,'pass')
                        #     else:
                        #         self.data.write_result(i,'fail')
                        #         self.data.write_res_data(i,res1)
                        # elif self.data.get_assert_method(i) == 2:#返回数据判断
                        #     expect = str(self.data.get_expect_data(i))
                        #     p = self.panduan.if_panduan(expect,res1)
                        #     if p == True:
                        #         self.data.write_result(i, 'pass')
                        #         #pass_count.append(i)
                        #     else:
                        #         self.data.write_result(i, 'fail')
                        #         self.data.write_res_data(i,res1)
                        # else:
                        #     #通过sql语句判断
                        #     expect = self.data.get_expect_data_for_mysql(i)
                        #     p = self.panduan.is_equal_dict(expect,res1)
                        #     if p == True:
                        #         self.data.write_result(i, 'pass')
                        #         #pass_count.append(i)
                        #     else:
                        #         self.data.write_result(i, 'fail')
                        #         self.data.write_res_data(i,res1)