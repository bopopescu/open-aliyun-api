# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 14:33
# @Author  : Abner.F
# @Site    : 
# @File    : DescribeLoadBalancers.py
# @Software: PyCharm
# @python  : 3.6


from aliyun_api.common.Slb import UrlRequest
from aliyun_api.common.config import Slb
from aliyun_api.api.SlbBackendServer.config import DescribeHealthStatus
from aliyun_api.common.Logger import Logger

if __name__ == '__main__':
    api_parameter = {
        'Action': 'DescribeLoadBalancers',
        'RegionId': 'cn-shenzhen'
    }

    result = UrlRequest(api_parameter).getResult(Slb.qiandai.commonParameter)
    Logger("Ecs-DescribeInstances").getLogger().info(result)
