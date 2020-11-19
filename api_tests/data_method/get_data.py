#coding : utf - 8
from api_tests.util.connect_mysql import OperationMysql
from api_tests.util.excel_util import OperationExcel
from api_tests.util.json_util import OperationJson
from api_tests.data_method import global_col
class GetData:
    def __init__(self):
        self.o_excel=OperationExcel()
        self.o_json=OperationJson()
        
    def get_case_lines(self):  #获取表格一共多少行
        return self.o_excel.get_rowss()
    def get_is_run(self,row):
        #获取是否执行
        col = int(global_col.get_run())
        run_model = self.o_excel.get_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag
    def is_header(self,row):
        #获取是否有请求头
        col = int(global_col.get_header())
        header = self.o_excel.get_value(row,col)
        if header != '':
            return header
        else:
            return None
        
    def get_request_method(self,row):
        #获取请求方式
        col = int(global_col.get_run_way())
        method = self.o_excel.get_value(row,col)
        return method
    def get_request_url(self,row):
        #获取url
        col = int(global_col.get_url())
        request_url = self.o_excel.get_value(row,col)
        return request_url
    def get_request_data(self,row):
        #获取请求参数
        col = int(global_col.get_data())
        request_data = self.o_excel.get_value(row,col)
        return request_data
    def get_expect_data(self,row):
        #获取预期结果
        col = int(global_col.get_expect())
        expect = self.o_excel.get_value(row,col)
        return expect
        
    def write_result(self,row,value):   
        col = int(global_col.get_result())
        result = self.o_excel.write_value(row,col,value)
        return result
    
    def write_code(self,row,value):
        #往表格中写入响应状态码
        col = int(global_col.get_code())
        result_code = self.o_excel.write_value(row,col,value)
        return result_code
        
    def write_res_data(self,row,value):
        #写入返回如数据
        col = int(global_col.get_response_data())
        res_data= self.o_excel.write_value(row,col,value)
        return res_data
    def get_assert_method(self,row):
        #判断断言方式，1为状态码校验，2为响应文本校验，3为数据库校验
        col = int(global_col.get_assert_method())
        method = self.o_excel.get_value(row,col)
        return method

    def get_expect_data_for_mysql(self, row):
        op_mysql = OperationMysql()
        sql = self.get_expect_data(row)
        res = op_mysql.search_one(sql)
        return res

    def is_depend(self,row):    #判断是否有case依赖
        col = int(global_col.get_case_depend())
        depend_case_id = self.o_excel.get_value(row,col)
        if depend_case_id =="":
            return None
        else:
            return depend_case_id

    def get_depend_key(self,row):    #获取被依赖数据的key
        col = int(global_col.get_data_depend())
        depent_key = self.o_excel.get_value(row,col)
        re = depent_key.split(",")
        if re == "":
            return None
        else:
            return re

    def get_depend_field(self,row):  #获取下一个接口依赖字段
        col = int(global_col.get_field_depend())
        depend_case_id = self.o_excel.get_value(row,col)
        re = depend_case_id.split(",")
        if re == "":
            return None
        else:
            return re

if __name__ == '__main__':
    re = GetData()
    res = re.get_depend_field(6)
    print(res)