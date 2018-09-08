# open-aliyun-api
open aliyun api , such as dns 、slb、vps and so on

### 阿里云SLB api接口

   >目前要尽可能做到全自动化， 目前后端的上线操作要通过页面的SLB对后端的服务器设置权重来确保操作的正确性。  
   >所以研究阿里云的SLB api接口调用是全自动化必然走的一个过程， 阿里云的SLB api接口传参后的签名是个坑,    
   >现在实现了SLB api接口类的封装， SLB 公共参数在common的config的Slb.py配置，api各接口参数形成一    
   >个字典，传递字典就能返回完整的URL， 调用相关请求方法就能返回json结果。

### 要求版本

   >python 2.7.x
   
#### 打包发布
   
  > pip install setuptools  
  > python setup.py install

#### 卸载

  > python setup.py install -record uninstall_requirements.txt  
  > cat uninstall_requirements.txt | xargs rm -rf

#### 推荐环境 pipenv （pip install pipenv）

  > cd 工程目录  
  > pipenv --two  （安装python 2.7.x 版本）   
  > pipenv install （安装依赖， 会搜当前项目路径有没有Pipfile以及Pipfile.lock，   
   若有，根据这些安装；若无，根据requirements.txt安装依赖，   
   形同 pip install -r requirements.txt）       
  > pipenv graph （已安装依赖的图）  
  > pipenv shell (激活虚拟环境）
