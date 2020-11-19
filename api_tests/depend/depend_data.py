#coding=utf-8
#coding : utf-8
from api_tests.util.excel_util import OperationExcel
from api_tests.run_method.request_method import RunMethod
from api_tests.data_method.get_data import GetData
from jsonpath_rw import jsonpath,parse
from api_tests.util.json_util import OperationJson
class DependdentData:
    def __init__(self,case_id):
        self.case_id = case_id
        #print(self.case_id)
        self.opera_excel=OperationExcel()
        self.data = GetData()
    def get_case_line_data(self):    #通过casse_id去获取该case_id的整行数据
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        #print(rows_data)
        return rows_data
    def run_dependent(self):    #执行有依赖测试，获取结果
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_request_data(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        chuan_json = OperationJson()
        headers = chuan_json.read_data()
        # header = chuan_json.get_data("token")
        # headers = {"token": header}
        res = run_method.run_main(method, url, request_data, headers = headers)
        return res[0]
    def get_data_for_key(self,row):     #根据依赖的key去获取执行依赖测试case的响应，在相应中找被依赖的value值
        depend_data = self.data.get_depend_key(row)  #获得依赖的返回字段key
        response_data = self.run_dependent()
        a_list=[]
        for dep in depend_data:
            json_exe = parse(dep)  #在结果json中找数据
            madle = json_exe.find(response_data)  #找响应的数据
            res = [math.value for math in madle][0]
            a_list.append(res)
        return a_list