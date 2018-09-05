# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:47:06 2018

@author: Abner.F
"""

from aliyun_api.common.Slb import UrlRequest

if __name__ == '__main__':

    # SetBackendServers
    '''
    设置后端服务器权重。
    接口说明地址        https://help.aliyun.com/document_detail/27634.html
    
    #"[{'ServerId':'i-wz9fzprkt1ullkni4w38', 'Weight':'50'}]"

    return 返回参数
    参数              类型           描述
    RequestId        String        请求ID。
    LoadBalancerId   String        负载均衡实例ID。
    BackendServers   List          后端服务器列表。

    BackendServers   objects
    ServerId         string        ECS实例ID。
    Weight           Integer       后端服务器的权重。
    
    	
    i-wz9glp2ttd1099jgers8
    
    '''
    
    
    BackendServers = {'ServerId':'i-wz9glp2ttd1099jgers8', 'Weight':'100'}
    BackendServersObj = []
    BackendServersObj.append(BackendServers)
    
    apiParameter = {
        'Action': 'SetBackendServers',
        'RegionId': 'cn-shenzhen',
        'LoadBalancerId': 'lb-wz937jr1qc2bssbt8ptd0',
        'BackendServers': str(BackendServersObj)
    }

    result = UrlRequest(apiParameter).getResult()
    print(result)

