# -*- coding: utf-8 -*-
"""
@author  : Abner.F
@software: PyCharm
@file    : DescribeInstancesRequest.py
@time    : 2018/4/2 15:42
@desc    :
"""

from aliyun_api.common.Slb import UrlRequest
from aliyun_api.common.config import Ecs
# from aliyun_api.api.SlbBackendServer.config import DescribeHealthStatus
from aliyun_api.common.Logger import Logger

if __name__ == '__main__':
    """
    获取实例列表
    https://help.aliyun.com/document_detail/25506.html
    名称        类型    是否必需    描述
    ZoneId     String    否    实例所属可用区
    PageNumber Integer   否    实例状态列表的页码。起始值：1    默认值：1
    PageSize   Integer   否    分页查询时设置的每页行数。取值范围：[1, 50]    默认值： 10
    :param page_number: page_number
    :param page_size: page_size
    :return: json str
    """
    api_parameter = {
        'Action': 'DescribeInstances',
        'RegionId': 'cn-shenzhen',
        'PageNumber': '1',
        'PageSize': '50'
    }
    result = UrlRequest(api_parameter).getResult(Ecs.qiandai.commonParameter)
    Logger("Ecs-DescribeInstances").getLogger().info(result)
