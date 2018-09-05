# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 14:23
# @Author  : Abner
# @File    : DescribeHealthStatus.py
# @Software: PyCharm
from aliyun_api.common.Slb import UrlRequest
from aliyun_api.common.config import Slb
from aliyun_api.api.SlbBackendServer.config import DescribeHealthStatus
from aliyun_api.common.Logger import Logger

if __name__ == '__main__':
    parameter = {
        'Action': 'DescribeHealthStatus',
        'RegionId': 'cn-shenzhen',
        'LoadBalancerId': 'lb-wz937jr1qc2bssbt8ptd0'
    }
    # result = UrlRequest(DescribeHealthStatus.qiandai.parameter).getResult(Slb.qiandai.parameter)
    result = UrlRequest(parameter).getResult(Slb.qiandai.commonParameter)
    Logger("Slb-DescriberHealthStatus").getLogger().info(result)

