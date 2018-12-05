# 地震破坏力速报系统报告生成程序

Describe: Generate report for earthquake simulation.

Version: 0.1.0

Last update: 2018.12.05

Author: CJ

## 基本配置

- [VSCode] 及其插件 Markdown Preview Enhanced
- [腾讯云对象存储(COS)]，免费额度够用
    - 注册账号
    - 设置用户权限等
    - 建立一个**存储桶**
- 注册一个[135]微信编辑器账号
- 将135账号与微信公众号关联
- 配置环境
    - 安装[Python]，注意由于Anaconda的url库调用问题，**需要单独安装一个系统Python**
    - 安装 [腾讯云COS SDK for Python]

[VSCode]: https://code.visualstudio.com/
[腾讯云对象存储(COS)]: https://cloud.tencent.com/product/cos
[135]: https://www.135editor.com/
[Python]: https://www.python.org/downloads/
[腾讯云COS SDK for Python]: https://cloud.tencent.com/document/product/436/12269

## 使用

- 创建 `/input/config.json`，设置你的对象存储，下面的例子是假的
```json
{
  "bucket": "myfigures-1234567",
  "secret_id": "AKIDQffQzJ6R8auzpP9hhhGZeU5VigOraLFu",
  "secret_key": "Zt12qMehbGl7F3qMeiYBZicLq8B1h8KI",
  "region": "ap-beijing"
}
```
- 修改报告文字 `/input/text/text.json`
- 修改清华震害表 `/input/text/thu.txt`
- 替换图片 `/input/figures/dynamic/`
- 运行程序生成 `report.md`

## 程序说明

- ReportGeneration.py
主程序
- TextDealer.py
- FigureDealer.py
- template.md
报告模板
- my-style.less
外部样式表

## 微信制作

- 在VSCode打开`report.md`，用插件MPE查看预览
- 拷贝预览（不是文本）到关联了公众号的135编辑器
- 做一些你喜欢的调整
- 点击`保存文章`，设置一个封面图片，可以在选项里看到同步到公众号的选项（关联后重新打开生效）；或者在左侧`我的文章`也有`多图文同步`选项
- 点击`保存`，等待提示成功
- 在微信公众号里查看你的推送
