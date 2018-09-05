# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 16:05
# @Author  : Abner.F
# @Site    : 
# @File    : DescribeDomainsRequest.py
# @Software: PyCharm
# @python  : 3.6

from aliyun_api.common.Slb import UrlRequest
from aliyun_api.common.config import Dns
from aliyun_api.common.Logger import Logger



if __name__ == '__main__':

    api_parameter = {
        'Action': 'DescribeDomainRecords',
        'DomainName': 'ttjiekuan.com',
        'RegionId': 'cn-shenzhen',
        'PageNumber': '1',
        'PageSize': '50'
    }
    result = UrlRequest(api_parameter).getResult(Dns.jiekuan.commonParameter)
    Logger("Ecs-DescribeInstances").getLogger().info(result)