# 首先你需要在引用的python文件内导入该对象所在的文件，也就是main_menu.py
import urllib.request
import urllib.parse
import re
from PyQt5.QtCore import QThread, pyqtSignal
from selenium import webdriver
import time
import win32api
from selenium.webdriver.chrome.options import Options
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import PyQt5.sip
import untitled  # 导入该对象所在文件
import sys
import pyperclip
j = None
# 该程序用的是分析源码然后获取值的方法，还有一种执行js语句得到值的方法。
def myurl():
    # url = "https://www.microsoft.com/zh-cn/software-download/windows10ISO"
    #
    # header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.2"}
    #
    # request = urllib.request.Request(url,headers=header)

    # html = urllib.request.urlopen(request).read().decode("utf-8")

    chrome_options = Options()
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    chrome_options.add_argument('User-Agent="Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.2"')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='lib/chromedriver.exe')
    # print("正在悄悄的从微软获取下载链接，请稍等···")
    driver.get("https://www.microsoft.com/zh-cn/software-download/windows10ISO")

    html = driver.page_source
    driver.quit()
    return html
def pageid(html):
    fr = re.compile(r'data-defaultpageid="([^\"]*)"',re.S)
    itme_list = fr.findall(html)
    return itme_list
def sessionid(html):
    fr = re.compile(r'session_id=([^\"]*)\"', re.S)
    itme_list = fr.findall(html)
    return itme_list
def optionid(html):
    fr = re.compile(r'<option value="([^\"]*)\"', re.S)
    itme_list = fr.findall(html)
    itme_list.remove('')
    return itme_list
def optionidname(html,optionid):
    itme_list = []
    for optionids in optionid:
        fr = re.compile(r'<option value="'+optionids+'">([^\<]*)</option>', re.S)
        if fr == None:
            pass
        else:
            itme_list.append(fr.findall(html))

    return itme_list
def optone(optionidname):
    i = 1
    for optionidnames in optionidname:
        print(str(i) + "、" + optionidnames[0])
        i = i + 1
    print("请输入你的选项：", end="")
    while True:
        a = input()
        a = int(a)
        for io in range(1,i):
            if a == io:
                return a-1
                break
        print("没有这个选项噢！")
def opttwo(languagename):
    i = 1
    for languagenames in languagename:
        print(str(i) + "、" + languagenames)
        i = i + 1
    print("请输入你的选项：", end="")
    while True:
        a = input()
        a = int(a)
        for io in range(1,i):
            if a == io:
                return a-1
                break
        print("没有这个选项噢！")

def tolink1(pageid,sessionid,optionid):
    url = "https://www.microsoft.com/zh-cn/api/controls/contentinclude/html?pageId="+pageid+"&host=www.microsoft.com&segments=software-download%2cwindows10ISO&query=&action=getskuinformationbyproductedition&sessionId="+sessionid+"&productEditionId="+optionid+"&sdVersion=2"

    header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.2"}

    request = urllib.request.Request(url,headers=header)

    html = urllib.request.urlopen(request).read().decode("utf-8")
    return html
def languageid(html):
    fr = re.compile(r';id&quot;:&quot;([^\&]*)&quot', re.S)
    itme_list = fr.findall(html)
    # itme_list.remove('')
    return itme_list
def languagename(html):
    fr = re.compile(r';language&quot;:&quot;([^\&]*)&quot', re.S)
    itme_list = fr.findall(html)
    # itme_list.remove('')
    return itme_list
def tolink2(pageid,sessionid,languageid,languagename):
    url = "https://www.microsoft.com/zh-cn/api/controls/contentinclude/html?pageId="+pageid+"&host=www.microsoft.com&segments=software-download%2cwindows10ISO&query=&action=GetProductDownloadLinksBySku&sessionId="+sessionid+"&skuId="+languageid+"&language="+languagename+"&sdVersion=2"

    header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.2"}

    request = urllib.request.Request(url,headers=header)

    html = urllib.request.urlopen(request).read().decode("utf-8")
    # print(url)
    return html
def downlinkname(html):
    fr = re.compile(r'<span class="product-download-type">([^\<]*)</span>', re.S)
    itme_list = fr.findall(html)
    # itme_list.remove('')
    return itme_list
def downlink(html):
    fr = re.compile(r'href="([^\"]*)"', re.S)
    itme_list = fr.findall(html)
    # itme_list.remove('')
    return itme_list
def downiso(downlink,downlinkname):
    i = 1
    if not downlinkname:
        win32api.MessageBox(0, "微软官网已将你的IP屏蔽，稍等一会再访问或者换个IP访问吧\n\n温馨提醒：切勿频繁获取，否则微软会长时间屏蔽你的IP噢！", "错误提示")
        sys.exit()
    else:
        # print(downlink,downlinkname)
        for downlinknames in downlinkname:
            print(str(i)+"、"+downlinknames)
            i = i + 1
        while True:
            print("请选择你需要的位数：",end="")
            a = input()
            a = int(a)
            for io in range(1,i):
                if a == io:
                    return a
                    break
            else:
                print("没有这个选项噢！")

    # print('%.2f%%' % per,end="")
    # print("当前已下载大小："+str(a * b),end="")
    # print("文件总大小："+str(c),end="")
    # time.sleep(0.5)
    # sys.stdout.write("\r")

def filename(downlinks):
    fr = re.compile(r'/(W[^\?]*)\?', re.S)
    itme_list = fr.findall(downlinks)
    # itme_list.remove('')
    return itme_list
def settext(aString):
   pyperclip.copy(aString)
   win32api.MessageBox(0, "复制成功！", "提示")
class Worker(QThread):
    sinOut = pyqtSignal(str) # 自定义信号，执行run()函数时，从相关线程发射此信号
    sinOut2 = pyqtSignal(list)
    sinOut3 = pyqtSignal(int)
    sinOut4 = pyqtSignal(list)
    sinOut5 = pyqtSignal(list)
    sinOut6 = pyqtSignal(list)
    sinOut7 = pyqtSignal(str)
    opt1 = None
    opt2 = None
    opt3 = None
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()



    def jeishou1(self,n):
        if n == None:
            self.opt1 = None
        else:
            self.opt1 = n
    def jeishou2(self,n):
        if n == None:
            self.opt2 = None
        else:
            self.opt2 = n
    def jeishou3(self,n):
        if n == None:
            self.opt3 = None
        else:
            self.opt3 = n

    def jindu(self,a, b, c):
        # print("jindu???")
        list_abc = []
        # print("jindu???")
        per = 100 * a * b / c
        # print("jindu???")
        if per > 100:
            per = 100
            win32api.MessageBox(0, "下载完成！", "提示")
            sys.exit()
        # print("jindu???")
        list_abc.append(per)
        list_abc.append(a)
        list_abc.append(b)
        list_abc.append(c)
        # print("jindu???")
        self.sinOut6.emit(list_abc)
        # print("jindu???")
    def run(self):

        html = myurl()
        self.sinOut.emit(html)
        # print(html)


        pageid1 = pageid(html)
        sessionid1 = sessionid(html)
        optionid1 = optionid(html)
        optionidname1 = optionidname(html, optionid1)
        time.sleep(5)
        self.sinOut2.emit(optionidname1)
        # print(optionidname1,type(optionidname1))
        while True:
            if self.opt1 == None:
                # print("pass")
                pass
            else:
                # print(self.opt1)
                break

        # optone1 = optone(optionidname1)
        optone1 = self.opt1
        time.sleep(5)
        self.sinOut3.emit(optone1)
        linkhtml1 = tolink1(pageid1[0], sessionid1[0], optionid1[optone1])
        languageid1 = languageid(linkhtml1)
        languagename1 = languagename(linkhtml1)
        self.sinOut4.emit(languagename1)
        while True:
            if self.opt2 == None:
                # print("pass")
                pass
            else:
                # print(self.opt2)
                break
        # opttwo1 = opttwo(languagename1)
        opttwo1 = self.opt2
        languagename1[opttwo1] = urllib.parse.quote(languagename1[opttwo1], safe='()')
        linkhtml2 = tolink2(pageid1[1], sessionid1[0], languageid1[opttwo1], languagename1[opttwo1])
        downlink1 = downlink(linkhtml2)
        downlinkname1 = downlinkname(linkhtml2)
        if not downlinkname1:
            win32api.MessageBox(0, "微软官网已将你的IP屏蔽，稍等一会再访问或者换个IP访问吧\n\n温馨提醒：切勿频繁获取，否则微软会长时间屏蔽你的IP噢！", "错误提示")
            sys.exit()
        time.sleep(5)
        self.sinOut5.emit(downlinkname1)
        while True:
            if self.opt3 == None:
                # print("pass")
                pass
            else:
                # print(self.opt3)
                break
        downiso1 = self.opt3
        # print(downlink1, downlinkname1)
        # downiso1 = downiso(downlink1, downlinkname1)
        downlinks = downlink1[downiso1].replace('&amp;', '&')
        # print(downlinks)
        filename1 = filename(downlinks)
        # print(filename,type(filename))
        # print("正在下载中···")
        # print(downlinks,filename1)
        # self.sinOut7.emit(downlinks)
        self.sinOut7.emit(downlinks)
        a, b = urllib.request.urlretrieve(downlinks, filename1[0], self.jindu)
        # a, b = urllib.request.urlretrieve(downlinks, filename[0], jindu)

            # 发出信号

Ui_MainWindow = untitled.Ui_MainWindow  # 指定Ui_MainWindow 为main_menu文件下的Ui_MainWindow对象。
class CoperQt(QtWidgets.QMainWindow, Ui_MainWindow):  # 创建一个Qt对象
    # 这里的第一个变量是你该窗口的类型，第二个是该窗口对象。
    # 这里是主窗口类型。所以设置成当QtWidgets.QMainWindow。
    # 你的窗口是一个会话框时你需要设置成:QtWidgets.QDialog
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_MainWindow.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象
        self.pushButton_2.hide()
        self.pushButton.clicked.connect(self.slotStart)
        self.thread = Worker()
        self.thread.sinOut.connect(self.slotAdd)
        self.thread.sinOut2.connect(self.xuanxiang1)
        self.thread.sinOut3.connect(self.slotAdd2)
        self.thread.sinOut4.connect(self.xuanxiang2)
        self.thread.sinOut5.connect(self.xuanxiang3)
        self.thread.sinOut6.connect(self.downmyfile)
        self.thread.sinOut7.connect(self.zhantie)
        # self.thread.sinOut7.connect(self.zhantie)
    def zhantie(self,m):
        self.pushButton_2.show()
        self.pushButton_2.clicked.connect(lambda : settext(m))
    def slotStart(self):
        self.pushButton.setEnabled(False)
        self.progressBar.show()
        self.thread.start()

        self.testtime = QtCore.QTimer()
        self.testtime.timeout.connect(lambda: self.xunhuan())
        self.testtime.start(1000)

    def xunhuan(self):
        if self.progressBar.value() == 100:
            win32api.MessageBox(0, "网络连接失败！", "提示")
            sys.exit()
        else:
            nowv = self.progressBar.value()
            nowv += 1
            self.progressBar.setValue(nowv)
    # self.progressBar.show()
    def slotAdd(self, file_inf):
        self.progressBar.setValue(100)
        self.testtime.stop()
        self.testtime2 = QtCore.QTimer()
        self.testtime2.timeout.connect(lambda: self.slotAdd2_1())
        self.testtime2.start(1000)
    def slotAdd2_1(self):
        if self.progressBar_2.value() == 100:
            win32api.MessageBox(0, "网络连接失败！", "提示")
            sys.exit()
        else:
            nowv = self.progressBar_2.value()
            nowv += 1
            self.progressBar_2.setValue(nowv)
    def slotAdd3(self):
        if self.progressBar_3.value() == 100:
            win32api.MessageBox(0, "网络连接失败！", "提示")
            sys.exit()
        else:
            nowv = self.progressBar_3.value()
            nowv += 1
            self.progressBar_3.setValue(nowv)
    def slotAdd4(self):
        if self.progressBar_4.value() == 100:
            win32api.MessageBox(0, "网络连接失败！", "提示")
            sys.exit()
        else:
            nowv = self.progressBar_4.value()
            nowv += 1
            self.progressBar_4.setValue(nowv)
    def slotAdd2(self, n):
            pass
    def xuanxiang1(self, n):
        self.progressBar_2.setValue(100)
        self.testtime2.stop()
        items = []
        for ns in n:
            items.append(ns[0])
        value, ok = QtWidgets.QInputDialog.getItem(self, "请选择版本","", items, 0, False)
        # print(value,ok)
        m = items.index(value)
        if ok == True:
            # print(m)
            self.thread.jeishou1(m)
            self.progressBar_3.show()
            self.testtime3 = QtCore.QTimer()
            self.testtime3.timeout.connect(lambda: self.slotAdd3())
            self.testtime3.start(500)
        elif ok == False:
            sys.exit()
    def xuanxiang2(self, n):
        self.progressBar_3.setValue(100)
        self.testtime3.stop()
        value, ok = QtWidgets.QInputDialog.getItem(self, "请选择语言","",n, 0, False)
        # print(value,ok)
        m = n.index(value)
        if ok == True:
            # print(m)
            self.thread.jeishou2(m)
            self.testtime4 = QtCore.QTimer()
            self.testtime4.timeout.connect(lambda: self.slotAdd4())
            self.testtime4.start(500)
        elif ok == False:
            sys.exit()
    def xuanxiang3(self, n):
        self.progressBar_4.setValue(100)
        self.testtime4.stop()
        value, ok = QtWidgets.QInputDialog.getItem(self, "请选择位数","", n, 0, False)
        # print(value,ok)
        m = n.index(value)
        if ok == True:
            # print(m)
            self.thread.jeishou3(m+1)
        elif ok == False:

            sys.exit()
    def downmyfile(self,list_abc):
        # print("downmyfile")
        self.progressBar_5.setValue(list_abc[0])
        xianshi = str(100.000 * list_abc[1] * list_abc[2] / list_abc[3])+"%"
        self.label_8.setText(xianshi)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('windowsvista')
    window = CoperQt()  # 创建QT对象
    window.show()  # QT对象显示
    sys.exit(app.exec_())