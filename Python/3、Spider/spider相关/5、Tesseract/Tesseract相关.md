### 不记文档，白忙一场

------

#### 概述

> ```python
> tesseract 是一套流行的OCT算法。专门做图片内容识别。我们只需要下载相应的训练数据就能使用tesseract进行图片内容读取。
> ```

#### window下安装tesseract

> ```python
> 安装参考：https://jingyan.baidu.com/article/219f4bf788addfde442d38fe.html
> 【注】如果不安装，就在python中用pytesseract，会报错：											pytesseract.pytesseract.TesseractNotFountError:tesseract is not installed or it's not 	  in your path
> ```

#### python安装pytesseract

> ```python
> 安装pytesseract： pip install pytesseract
> ```

#### 识别汉字

> ```python
> import pytesseract
> from PIL import Image
> 
> image = Image.open('QQ.png')
> 
> result = pytesseract.image_to_string(image, lang='chi_sim')
> print(result)
> ```

#### 对图片进行处理

> ```python
> from PIL import Image
> 
> import pytesseract
> 
> image = Image.open('./douban.jpg')
> 
> # 灰度化
> image = image.convert('L')
> # 杂点清除掉。只保留黑的和白的。返回像素对象
> data = image.load()
> w, h = image.size
> for i in range(w):
>     for j in range(h):
>         if data[i, j] > 120:
>             data[i, j] = 255 # 纯白
>         else:
>             data[i, j] = 0 # 纯黑
> image.save('clean_captcha.png')
> image.show()
> 
> result = pytesseract.image_to_string(image, lang='eng')
> print(result)
> 
> 
> image.show()
> ```

#### 机器视觉

> ```python
> 从 Google 的无人驾驶汽车到可以识别假钞的自动售卖机，机器视觉一直都是一个应用广泛且具有深远的影响和雄伟的愿景的领域
> ```
>
> ```python
> 我们将重点介绍机器视觉的一个分支：文字识别，介绍如何用一些 Python库来识别和使用在线图片中的文字
> ```
>
> ```python
> 我们可以很轻松的阅读图片里的文字，但是机器阅读这些图片就会非常困难，利用这种人类用户可以正常读取但是大多数机器人都没法读取的图片，验证码 (CAPTCHA)就出现了
> ```
>
> ```python
> 将图像翻译成文字一般被称为光学文字识别(Optical Character Recognition, OCR)
> ```

#### 应用案例

> ```python
> import pytesseract
> from PIL import Image
> import requests
> import subprocess
> 
> url = 'https://www.bjgjj.gov.cn/wsyw/servlet/PicCheckCode1'
> 
> def binarizing(img,threshold): #input: gray image
>     pixdata = img.load()
>     w, h = img.size
>     for y in range(h):
>         for x in range(w):
>             if pixdata[x, y] < threshold:
>                 pixdata[x, y] = 0
>             else:
>                 pixdata[x, y] = 255
>     return img
> def cleanFile(filePath, newFilePath):
>     image = Image.open(filePath)
>     # 对图片进行灰度化处理
>     image = image.convert('L')
>     # 对图片进行阈值过滤,然后保存
>     binarizing(image,120)
>     image.save(newFilePath)
>     # 调用系统的tesseract命令对图片进行OCR识别
>     subprocess.call(["tesseract", newFilePath, "output"])
> 
> # 下载图片机型保存
> response = requests.get(url,verify = False)
> with open('picCheckcode.png',mode='wb') as file:
>     file.write(response.content)
>     print('save completed')
> 
> # 清洗图片
> cleanFile("picCheckcode.png", "text2clean.png")
> image = Image.open('text2clean.png')
> image.show()
> 
> # 使用pytesseract
> # text = pytesseract.image_to_string(Image.open('test.jpg'))
> # 使用修改代码的pytesseract进行图片识别
> text = pytesseract.image_to_string('text2clean.png')
> print('-----------------------------',text.strip())
> ```
>

