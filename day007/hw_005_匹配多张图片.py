# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/7 17:13
# 文件名称: hw_005_匹配多张图片.py
# 开发工具: PyCharm

url = 'https://www.enterdesk.com/'

s = """
<div id="auto_width_bjtj" class="egene_pic_m center">
                    <div class="egene_pic_li">
            <dl class="egene_pic_dl" style="margin-left: 0px;">
                <dd style="width: 300px; height: 187px; overflow: hidden;"><a href="https://www.enterdesk.com/bizhi/17560.html" target="_blank"><img a1_width="576" a1_height="360" a_width="576" a_height="360" src="https://up.enterdesk.com/edpic_360_360/eb/5e/5d/eb5e5d63fc372f97e218c99f52090e92.jpg" alt="途经一片静美" title="途经一片静美" style="height: auto; width: 300px; position: relative; top: -0.25px;"></a></dd>
                <dt style="bottom: -20px;">
                    <div><a href="https://www.enterdesk.com/bizhi/17560.html" target="_blank">途经一片静美</a></div>
                    <div><span class="icosc icosc01">0</span><span class="icosc icosc02">3</span><span class="icosc icosc03">8514</span></div>
                </dt>
            </dl>
            </div>            <div class="egene_pic_li">
            <dl class="egene_pic_dl" style="margin-left: 6px;">
                <dd style="width: 300px; height: 187px; overflow: hidden;"><a href="https://mm.enterdesk.com/bizhi/16126.html" target="_blank"><img a1_width="576" a1_height="360" a_width="576" a_height="360" src="https://up.enterdesk.com/edpic_360_360/c1/a6/a5/c1a6a5b39e318b9314b38a47ff780526.jpg" alt="许自己一段旅行" title="许自己一段旅行" style="height: auto; width: 300px; position: relative; top: -0.25px;"></a></dd>
                <dt>
                    <div><a href="https://mm.enterdesk.com/bizhi/16126.html" target="_blank">许自己一段旅行</a></div>
                    <div><span class="icosc icosc01">163</span><span class="icosc icosc02">16</span><span class="icosc icosc03">20586</span></div>
                </dt>
            </dl>
            </div>            <div class="egene_pic_li">
            <dl class="egene_pic_dl" style="margin-left: 6px;">
                <dd style="width: 300px; height: 187px; overflow: hidden;"><a href="https://www.enterdesk.com/bizhi/15763.html" target="_blank"><img a1_width="576" a1_height="360" a_width="576" a_height="360" src="https://up.enterdesk.com/edpic_360_360/09/6a/da/096ada91bed79786caf307511901a17a.jpg" alt="人生一直在路上" title="人生一直在路上" style="height: auto; width: 300px; position: relative; top: -0.25px;"></a></dd>
                <dt style="bottom: -20px;">
                    <div><a href="https://www.enterdesk.com/bizhi/15763.html" target="_blank">人生一直在路上</a></div>
                    <div><span class="icosc icosc01">251</span><span class="icosc icosc02">25</span><span class="icosc icosc03">34608</span></div>
                </dt>
            </dl>
            </div>            <div class="egene_pic_li">
            <dl class="egene_pic_dl" style="margin-left: 6px;">
                <dd style="width: 300px; height: 187px; overflow: hidden;"><a href="https://mm.enterdesk.com/bizhi/27936.html" target="_blank"><img a1_width="640" a1_height="360" a_width="576" a_height="360" src="https://up.enterdesk.com/edpic_360_360/f0/03/a4/f003a44d2706b33eae302a835349e076.jpg" alt="遇见你,余生都是你" title="遇见你,余生都是你" style="height: 187px; width: auto; position: relative; left: -16.2222px;"></a></dd>
                <dt style="bottom: -20px;">
                    <div><a href="https://mm.enterdesk.com/bizhi/27936.html" target="_blank">遇见你,余生都是你</a></div>
                    <div><span class="icosc icosc01">0</span><span class="icosc icosc02">0</span><span class="icosc icosc03">4422</span></div>
                </dt>
            </dl>
            </div>            <div class="egene_pic_li">
            <dl class="egene_pic_dl" style="margin-left: 0px;">
                <dd style="width: 300px; height: 187px; overflow: hidden;"><a href="https://mm.enterdesk.com/bizhi/27958.html" target="_blank"><img a1_width="576" a1_height="360" a_width="576" a_height="360" src="https://up.enterdesk.com/edpic_360_360/94/22/a8/9422a82791624629ac0ab613aa4a654b.jpg" alt="我拿时光换你一世痴迷" title="我拿时光换你一世痴迷" style="height: auto; width: 300px; position: relative; top: -0.25px;"></a></dd>
                <dt style="bottom: -20px;">
                    <div><a href="https://mm.enterdesk.com/bizhi/27958.html" target="_blank">我拿时光换你一世痴迷</a></div>
                    <div><span class="icosc icosc01">0</span><span class="icosc icosc02">0</span><span class="icosc icosc03">3520</span></div>
                </dt>
            </dl>
            </div>            <div class="egene_pic_li">
            <dl class="egene_pic_dl" style="margin-left: 6px;">
                <dd style="width: 300px; height: 187px; overflow: hidden;"><a href="https://www.enterdesk.com/bizhi/29577.html" target="_blank"><img a1_width="640" a1_height="360" a_width="576" a_height="360" src="https://up.enterdesk.com/edpic_360_360/45/e1/97/45e1974946ab6ffc3a3f5599494ff832.jpg" alt="有一种美丽叫夕阳" title="有一种美丽叫夕阳" style="height: 187px; width: auto; position: relative; left: -16.2222px;"></a></dd>
                <dt style="bottom: -20px;">
                    <div><a href="https://www.enterdesk.com/bizhi/29577.html" target="_blank">有一种美丽叫夕阳</a></div>
                    <div><span class="icosc icosc01">0</span><span class="icosc icosc02">0</span><span class="icosc icosc03">1292</span></div>
                </dt>
            </dl>
            </div>            <div class="egene_pic_li">
            <dl class="egene_pic_dl" style="margin-left: 6px;">
                <dd style="width: 300px; height: 187px; overflow: hidden;"><a href="https://www.enterdesk.com/bizhi/17937.html" target="_blank"><img a1_width="576" a1_height="360" a_width="576" a_height="360" src="https://up.enterdesk.com/edpic_360_360/d4/7d/84/d47d84ad1f92b6defb76c866a1d7e6fe.jpg" alt="给恋人说晚安的图片" title="给恋人说晚安的图片" style="height: auto; width: 300px; position: relative; top: -0.25px;"></a></dd>
                <dt style="bottom: -20px;">
                    <div><a href="https://www.enterdesk.com/bizhi/17937.html" target="_blank">给恋人说晚安的图片</a></div>
                    <div><span class="icosc icosc01">0</span><span class="icosc icosc02">0</span><span class="icosc icosc03">8461</span></div>
                </dt>
            </dl>
            </div>            <div class="egene_pic_li">
            <dl class="egene_pic_dl" style="margin-left: 6px;">
                <dd style="width: 300px; height: 187px; overflow: hidden;"><a href="https://www.enterdesk.com/bizhi/16348.html" target="_blank"><img a1_width="576" a1_height="360" a_width="576" a_height="360" src="https://up.enterdesk.com/edpic_360_360/dc/42/f7/dc42f7bd1ce6ca665a47e4cea565e42c.jpg" alt="唯美淡雅的花草" title="唯美淡雅的花草" style="height: auto; width: 300px; position: relative; top: -0.25px;"></a></dd>
                <dt style="bottom: -20px;">
                    <div><a href="https://www.enterdesk.com/bizhi/16348.html" target="_blank">唯美淡雅的花草</a></div>
                    <div><span class="icosc icosc01">295</span><span class="icosc icosc02">29</span><span class="icosc icosc03">33455</span></div>
                </dt>
            </dl>
            </div>    </div>
"""

import re

pattern = re.compile(r'src="([\s\S]*?)"')
print(pattern.findall(s))
img_list = pattern.findall(s)
for img in img_list:
    print(img)
