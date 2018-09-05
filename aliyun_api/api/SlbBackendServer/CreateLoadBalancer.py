# -*- coding: utf-8 -*-
from aliyun_api.common.Slb import UrlRequest
"""
Created on Fri Mar 23 10:04:31 2018

@author: Abner.F
"""

if __name__ == '__main__':

    # CreateLoadBalancer
    '''
    创建新的LoadBalancer
    接口说明地址        https://help.aliyun.com/document_detail/27577.html
    
    return 返回参数
    参数              类型           描述
    RequestId        String        请求ID。
    LoadBalancerId   String        负载均衡实例的ID。
    Address          String        分配的负载均衡实例的IP地址。
    VpcId            String        负载均衡实例的所属专有网络的ID。
    VSwitchId        String        负载均衡实例的所属交换机的ID。
    MasterZoneId     String        负载均衡实例的主可用区。
    SlaveZoneId      String        负载均衡实例的备可用区。
    LoadBalancerName String        负载均衡实例的名称。
    LoadBalancerSpec String        负载均衡的实例规格。若没有指定规格，值为空（表示是性能共享型实例）。
    '''

    apiParameter = {
        'Format': 'JSON',
        'Version': '2014-05-15',
        'AccessKeyId': 'LTAI7OvbAcI28O7u',
        'SignatureMethod': 'HMAC-SHA1',
        'SignatureVersion': '1.0',
        'Action': 'CreateLoadBalancer',
        'RegionId': 'cn-shenzhen',
        'LoadBalancerName': 'dfxk-test-CreateLoadBalancer',
        'AddressType': 'internet',
        'InternetChargeType' : 'paybytraffic',
        '':''
    }

    result = UrlRequest(apiParameter).getResult()
    print(result)