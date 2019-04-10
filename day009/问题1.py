# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/9 17:58
# 文件名称: hw_004_实战_正则匹配猫眼电影排行.py
# 开发工具: PyCharm

s = """
<dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/1219670" title="海市蜃楼" class="image-link" data-act="boarditem-click" data-val="{movieId:1219670}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default">
      <img alt="海市蜃楼" class="board-img" src="https://p0.meituan.net/movie/cd0820329098a64e157ee5af583f21f43774858.jpg@160w_220h_1e_1c">
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1219670" title="海市蜃楼" data-act="boarditem-click" data-val="{movieId:1219670}">海市蜃楼</a></p>
        <p class="star">
                主演：阿德里亚娜·乌加特,奇诺·达林,哈维尔·古铁雷斯
        </p>
<p class="releasetime">上映时间：2019-03-28</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">7</i></p>        
    </div>

      </div>
    </div>

                </dd>
"""

# board-index-10
import re

print(re.findall(r'board-index-(\d+)', s))
# print(re.findall(r'board-index-\d+', s))

# <i class="board-index board-index-10">10</i>
