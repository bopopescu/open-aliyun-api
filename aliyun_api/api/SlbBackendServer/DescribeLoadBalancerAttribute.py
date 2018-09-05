# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 14:29
# @Author  : Abner.F
# @Site    : 
# @File    : DescribeLoadBalancerAttribute.py
# @Software: PyCharm
# @python  : 3.6

from aliyun_api.common.config import Slb
from aliyun_api.common.Slb import UrlRequest

if __name__ == '__main__':
    # SetBackendServers
    '''
    根据负载均衡ID查询实例的详细信息。
    接口说明地址        https://help.aliyun.com/document_detail/27583.html

    返回参数
    
    参数	                类型	    描述
    LoadBalancerId	    String	负载均衡实例的ID。
    RegionId	        String	负载均衡实例的地域ID。
    RegionIdAlias	    String	负载均衡实例所属的Region编号别名，和DescribeRegions返参一致。
    LoadBalancerName	String	负载均衡实例的名称。
    LoadBalancerStatus	String	负载均衡实例状态：    inactive: 此状态的实例监听不会再转发流量。    active: 实例创建后，默认状态为active.    locked: 实例已经欠费或被阿里云锁定。
    
    Address	            String	负载均衡实例的服务地址。
    AddressType	        String	负载均衡实例的网络类型。
    NetworkType	        String	私网负载均衡实例的网络类型。
    VpcId	            String	私网负载均衡实例的专有网络ID。
    VswitchId	        String	私网负载均衡实例的交换机ID。
    Bandwidth	        Integer	按带宽计费的公网型实例的带宽峰值。
    CreateTime	        String	负载均衡实例的创建时间。
    ListenerPorts	    List	负载均衡实例前端使用的端口列表。    ListenerPort: 监听使用的前端端口。    
    ListenerPortsAndProtocol	List    负载均衡实例前端使用的端口和协议列表。    ListenerPort: 负载均衡实例前端使用的端口。    ListenerProtocol: 负载均衡实例前端使用的协议。
    BackendServers	    List    负载均衡实例的后端服务器列表。    ServerId: 后端服务器名（ECS实例）ID。   Weight: 后端服务器的权重。
    MasterZoneId	    String	负载均衡实例的主可用区ID。
    SlaveZoneId	        String	该创建实例的备可用区ID。
    LoadBalancerSpec	String	负载均衡实例的的性能规格。
    '''

    apiParameter = {
        'Action': 'DescribeLoadBalancerAttribute',
        'LoadBalancerId': 'lb-wz937jr1qc2bssbt8ptd0',
        'RegionId': 'cn-shenzhen'
    }

    result = UrlRequest(apiParameter).getResult(Slb.qiandai.commonParameter)
    print(result)