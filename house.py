# encoding:utf-8
# python3.0

from source.save import saveData
from source.common import getHtml
from source.report import reportData
import configparser
import webbrowser
import os


# ------主函数------
# delete()
if __name__ == '__main__':
    # 获取参数
    config = configparser.ConfigParser()
    config.read("config.ini")

    # 清除数据
    save = saveData(config)
    save.deleteOldData()

    # 贝壳找房 （例：北京、通州 251-499万 80-100平） 根据自己需求添加链接
#    beike1 = getHtml('''https://bj.ke.com/ershoufang/tongzhou/co32ba80ea100bp251ep499/''')
#    beike2 = getHtml('''https://bj.ke.com/ershoufang/tongzhou/pg2co32ba80ea100bp251ep499/''')
#    beike3 = getHtml('''https://bj.ke.com/ershoufang/tongzhou/pg3co32ba80ea100bp251ep499/''')
#    beike_htmls = [beike1, beike2, beike3]
#    for beike_html in beike_htmls:
#        save.beike_save(beike_html)

    # 链家 （例：北京 0-600万 60-100平） 根据自己需求添加链接
    lianjia1 = getHtml('''https://sh.lianjia.com/ershoufang/c5011000003124/?sug=%E5%B9%B3%E5%8D%97%E4%B8%89%E5%9B%9B%E6%9D%91''')
    lianjia2 = getHtml('''https://sh.lianjia.com/ershoufang/c5011000004258rs%E5%B9%B3%E5%8D%97%E4%B8%80%E4%BA%8C%E6%9D%91/''')
    lianjia3 = getHtml("""https://sh.lianjia.com/ershoufang/c5011000015238/?sug=%E5%B9%B3%E9%98%B3%E6%96%B0%E6%9D%91%E5%9B%9B%E8%A1%97%E5%9D%8A""")
    lianjia4 = getHtml('''https://sh.lianjia.com/ershoufang/xinqiao/l2l3/''')
    lianjia5 = getHtml('''https://sh.lianjia.com/ershoufang/rs%E7%94%B0%E6%9E%97/''')
    lianjia_htmls = [lianjia1, lianjia2, lianjia4, lianjia5, lianjia3]
#    lianjia_htmls = [lianjia2]
    for lianjia_html in lianjia_htmls:
        save.lianjia_save(lianjia_html)

    # 58同城 高新园区 80-120W 3室 精装修
#    tongcheng1 = getHtml('''https://sh.58.com/gumeiluoyang/chuzu/0/j1/?PGTID=0d3090a7-01ee-eccd-bf17-fa4baf1ab071&ClickID=2''')
#    tongcheng2 = getHtml('''http://bj.58.com/ershoufang/pn2/?huansuanyue=200_600&bunengdaikuan=0&area=60_100&PGTID=0d300000-0000-0b90-1e0b-bf894f74b13a&ClickID=1''')
#    tongcheng3 = getHtml('''http://bj.58.com/ershoufang/pn3/?huansuanyue=200_600&bunengdaikuan=0&area=60_100&PGTID=0d300000-0000-08f9-ba56-6673c850e2b8&ClickID=1''')
    # print(str(tongcheng1.encode('GB18030')))
#    tongcheng_htmls = [tongcheng1, tongcheng2, tongcheng3]
#    for tongcheng_html in tongcheng_htmls:
#        save.tongcheng_save(tongcheng_html)

    # 安居客 （例：北京 200-600万 60-100平 按最新排序） 根据自己需求添加链接
#    anjuke1 = getHtml('''https://beijing.anjuke.com/sale/o5/?from_area=60&to_area=100&from_price=200&to_price=600''')
#    anjuke2 = getHtml('''https://beijing.anjuke.com/sale/o5-p2/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
#    anjuke3 = getHtml('''https://beijing.anjuke.com/sale/o5-p3/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
#    anjuke_htmls = [anjuke1, anjuke2, anjuke3]
#    for anjuke_html in anjuke_htmls:
#        save.anjuke_save(anjuke_html)

    # # 赶集 高新园区 80-120W 3室 精装修
    # ganji1 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3q2/''')
    # ganji2 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o2q2/''')
    # ganji3 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o3q2/''')
    # ganji_htmls = [ganji1, ganji2, ganji3]
    # for ganji_html in ganji_htmls:
    #     ganji_save(ganji_html)

    print("生成报告中...")
    rep = reportData()
    reportFileName = rep.get_report()
    webbrowser.open('''file:///''' + os.path.dirname(__file__) + '''/reports/''' + reportFileName)

    print("OVER!!!")
