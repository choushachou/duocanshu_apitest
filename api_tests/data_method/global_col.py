#coding : utf - 8
class global_var:
    id = '1'
    run = '4'
    header = '5'
    request_way = '6'
    url = '7'
    data = '8'
    case_depend = '9'
    data_depend = '10'
    field_depend = '11'
    expect = '12'
    code = '13'
    response_data = '14'
    assert_method = '15'
    result = '16'
    
    
def get_id():
    return global_var.id
def get_run():
    return global_var.run
def get_header():
    return global_var.header
def get_run_way():
    #获取允许方式，get或post
    return global_var.request_way
def get_url():
        #获取URL
    return global_var.url
def get_data():
    #获取请求数据
    return global_var.data
def get_case_depend():  #获得依赖的id
    return global_var.case_depend
def get_data_depend():  #获得依赖的返回字段
    return global_var.data_depend
def get_field_depend():  #获得依赖的请求字段
    return global_var.field_depend
def get_expect():
    #获取期望结果
    return global_var.expect
def get_code():
    #获取响应状态码
    return global_var.code
def get_response_data():
    #获取返回数据
    return global_var.response_data
def get_assert_method():
    #获取断言方式
    return global_var.assert_method

def get_result():
    #获取测试结果
    return global_var.result
