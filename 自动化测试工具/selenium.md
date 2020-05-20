# selenium

## 谷歌无头浏览器

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
```

## 如何规避selenium被监测

~~~
from selenium import webdriver
from selenium.webdriver import ChromeOptions  # 需要导入的类
# 创建 option 对象
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 创建浏览器对象
driver = webdriver.Chrome(options=option)
~~~

## selenium一些常用功能

driver.page_source 打印网页源代码

driver.close() 关闭浏览器

get_attribute('class')获取元素属性

text获取文本值

获取 id 位置 标签名 大小

id
location
tag_name
size

## 查找元素

### 单个元素查找

多个元素查找find_elements即可

~~~python
driver.find_element_by_id('')
driver.find_element_by_xpath('')
#通用模式
from selenium.webdriver.common.by import By
driver.find_element(By.Id,'')
driver.find_element(By.XPATH,'')
~~~

### 元素交互操作

~~~
input.send_keys()#给输入框发送内容
input.clear()#清空输入框内容
button.click()#按钮点击
~~~

### 实现交互模式

~~~
from selenium.webdriver import ActionChains

driver.switch_to.frame('iframeResult') ##切换到iframeResult子标签里
sourse=driver.find_element_by_id('draggable')   #源
target=driver.find_element_by_id('droppable')   #目标

方式一：基于同一个动作链串行执行
# actions=ActionChains(driver) #拿到动作链对象
# actions.drag_and_drop(sourse,target) #把动作放到动作链中，准备串行执行，水平执行
# actions.perform()

#方式二：不同的动作链，每次移动的位移都不同
    ActionChains(driver).click_and_hold(sourse).perform()  #选中源，不松手
    distance=target.location['x']-sourse.location['x']   #source.location: 源的坐标   target.location['x']

    track=0  #走过的距离
    while track < distance:   # 走过的距离小于总距离
        ActionChains(driver).move_by_offset(xoffset=2,yoffset=0).perform()  #每次移动两个单位
        track+=2   #加2

    ActionChains(driver).release().perform()
#现在滑动验证码很少能够用这种方式了
~~~

### 执行javascript

~~~
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")

browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
~~~



### 模拟键盘事件

~~~
from selenium.webdriver.common.keys import Keys

send_keys(Keys.BACK_SPACE)	删除键BackSpace
send_keys(Keys.SPACE)	空格键Space
send_keys(Keys.TAB)	制表键Tab
send_keys(Keys.ESPACE)	回退键Esc
send_keys(Keys.ENTER)	回车键Enter
send_keys(Keys.CONTROL,‘a’)	全选Ctrl+A
send_keys(Keys.CONTROL,‘c’)	复制CTRL+C
send_keys(Keys.CONTROL,‘x’)	剪切CTRL+X
send_keys(Keys.CONTROL,‘v’)	粘贴Ctrl+V
send_keys(Keys.F1)	键盘F1
send_keys(Keys.F12)	键盘F12
~~~

