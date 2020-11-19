#coding:utf - 8
import json
import operator
from api_tests.data_method.get_data import GetData
class PanDuan:
    def __init__(self):
        self.data = GetData()

    def if_panduan(self,str_one,str_two):
        flag=''
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag
    def is_equal_dict(self,dict_one,dict_two):
        if isinstance(dict_one,str):
            dict_one = json.dumps(dict_one)
        if isinstance(dict_two,str):
            dict_two = json.dumps(dict_two)
        return operator.lt(dict_one,dict_two )

    def assert_result(self,n,row,expect,res="",code=""):
        if n == 1:  # 状态码判断
            exp = str(expect)[:3]
            p = self.if_panduan(exp, code)
            if p == True:
                self.data.write_result(row, 'pass')
            else:
                self.data.write_result(row, 'fail')
                self.data.write_res_data(row, res)
        elif n == 2:  # 返回数据判断
            exp = str(expect)
            p = self.if_panduan(exp, res)
            if p == True:
                self.data.write_result(row, 'pass')
            else:
                self.data.write_result(row, 'fail')
                self.data.write_res_data(row, res)
        else:
            # 通过sql语句判断
            exp = self.data.get_expect_data_for_mysql(row)
            p = self.is_equal_dict(exp, res)
            if p == True:
                self.data.write_result(row, 'pass')
            else:
                self.data.write_result(row, 'fail')
                self.data.write_res_data(row, res)