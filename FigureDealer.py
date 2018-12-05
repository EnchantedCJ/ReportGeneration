######################
# Reference: https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py
######################

# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError

# import sys
# import logging
import json
import os


# 腾讯云COSV5Python SDK, 目前可以支持Python2.6与Python2.7以及Python3.x

# pip安装指南:pip install -U cos-python-sdk-v5

# cos最新可用地域,参照https://www.qcloud.com/document/product/436/6224

# logging.basicConfig(level=logging.INFO, stream=sys.stdout)
def deal_figure():
    client, myBucket = initialization()
    figures = upload(client, myBucket)
    return figures


def upload(client, myBucket):
    figures = {
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': '',
        '6': '',
        '7': '',
        '8': '',
        '9': '',
        '10': '',
        '11': '',
        '12': '',
        '13': '',
        'station_loc': '',
        'EW': '',
        'NS': '',
        'UD': '',
        'spectrum': '',
        'single_frame': '',
        'single_3frame': '',
        'single_shanghai': '',
        'single_z15': '',
        'single_4frm': '',
        'city': '',
        'town': '',
        'country': '',
        'distribution': '',
    }
    # upload
    # 高级上传接口(推荐)
    # static
    for root, dirs, filesWalk in os.walk('./input/figures/static'):
        for file_name in filesWalk:
            response = client.upload_file(
                Bucket=myBucket,
                LocalFilePath='./input/figures/static/' + file_name,
                Key='static/' + file_name,
                PartSize=10,
                MAXThread=10
            )
            print(response['ETag'])

            url = client.get_presigned_url(
                Bucket=myBucket,
                Key='static/' + file_name,
                Method='GET',
                Expired=3600
            )

            file_name1 = file_name.split('.')[0]
            figures[file_name1] = url

    # dynamic
    for root, dirs, filesWalk in os.walk('./input/figures/dynamic'):
        for file_name in filesWalk:
            response = client.upload_file(
                Bucket=myBucket,
                LocalFilePath='./input/figures/dynamic/' + file_name,
                Key='dynamic/' + file_name,
                PartSize=10,
                MAXThread=10
            )
            print(response['ETag'])

            url = client.get_presigned_url(
                Bucket=myBucket,
                Key='dynamic/' + file_name,
                Method='GET',
                Expired=3600
            )

            file_name1 = file_name.split('.')[0]
            figures[file_name1] = url

    # error
    file_name = 'error.jpg'
    response = client.upload_file(
        Bucket=myBucket,
        LocalFilePath='./input/figures/' + file_name,
        Key=file_name,
        PartSize=10,
        MAXThread=10
    )
    url_error = client.get_presigned_url(
        Bucket=myBucket,
        Key=file_name,
        Method='GET',
        Expired=3600
    )
    print(response['ETag'])
    for key in figures:
        if figures[key] == '':
            figures[key] = url_error

    # print(figures)
    return figures


def initialization():
    # read config.json
    with open('./input/config.json', 'r', encoding='utf-8') as f:
        iniData = f.read()
    ini = json.loads(iniData)
    myBucket = ini['bucket']

    # 设置用户属性, 包括secret_id, secret_key, region
    # appid已在配置中移除,请在参数Bucket中带上appid。Bucket由bucketname-appid组成
    secret_id = ini['secret_id']  # 替换为用户的secret_id
    secret_key = ini['secret_key']  # 替换为用户的secret_key
    region = ini['region']  # 替换为用户的region
    scheme = 'https'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
    token = None  # 使用临时秘钥需要传入Token，默认为空,可不填
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)  # 获取配置对象
    client = CosS3Client(config)

    # check bucket
    reponse = client.head_bucket(
        Bucket=myBucket
    )
    # print(reponse)

    return (client, myBucket)

# debug
# if __name__ == '__main__':
#     deal_figure()
