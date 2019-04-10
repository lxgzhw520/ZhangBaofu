# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/8 17:42
# 文件名称: hw_004_匹配电影排行榜.py
# 开发工具: PyCharm

s = """

<!DOCTYPE html>

<!--[if IE 8]><html class="ie8"><![endif]-->
<!--[if IE 9]><html class="ie9"><![endif]-->
<!--[if gt IE 9]><!--><html><!--<![endif]-->
<head>
  <title>热映口碑榜 - 猫眼电影 - 一网打尽好电影</title>
  
  <link rel="dns-prefetch" href="//p0.meituan.net"  />
  <link rel="dns-prefetch" href="//p1.meituan.net"  />
  <link rel="dns-prefetch" href="//ms0.meituan.net" />
  <link rel="dns-prefetch" href="//s0.meituan.net" />
  <link rel="dns-prefetch" href="//ms1.meituan.net" />
  <link rel="dns-prefetch" href="//analytics.meituan.com" />
  <link rel="dns-prefetch" href="//report.meituan.com" />
  <link rel="dns-prefetch" href="//frep.meituan.com" />

  
  <meta charset="utf-8">
  <meta name="keywords" content="猫眼电影,电影排行榜,热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100">
  <meta name="description" content="猫眼电影热门榜单,包括热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100,多维度为用户进行选片决策">
  <meta http-equiv="cleartype" content="yes" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="renderer" content="webkit" />

  <meta name="HandheldFriendly" content="true" />
  <meta name="format-detection" content="email=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="viewport" content="width=device-width, initial-scale=1">

  
  <script>"use strict";!function(){var i=0<arguments.length&&void 0!==arguments[0]?arguments[0]:"_Owl_",n=window;n[i]||(n[i]={isRunning:!1,isReady:!1,preTasks:[],dataSet:[],use:function(i,t){this.isReady&&n.Owl&&n.Owl[i](t),this.preTasks.push({api:i,data:[t]})},add:function(i){this.dataSet.push(i)},run:function(){var t=this;if(!this.isRunning){this.isRunning=!0;var i=n.onerror;n.onerror=function(){this.isReady||this.add({type:"jsError",data:arguments}),i&&i.apply(n,arguments)}.bind(this),(n.addEventListener||n.attachEvent)("error",function(i){t.isReady||t.add({type:"resError",data:[i]})},!0)}}},n[i].run())}();</script>
  <script>
  cid = "c_wx6zb55";
  ci = 1;
val = {"subnavId":7};    window.system = {};

  window.openPlatform = '';
  window.openPlatformSub = '';
  window.$mtsiFlag = '0';

  </script>
  <link rel="stylesheet" href="//s0.meituan.net/bs/?f=myfe/mywww:/common.d0f96cc2.css"/>
<link rel="stylesheet" href="//s0.meituan.net/bs/?f=myfe/mywww:/board-index.92a06072.css"/>
  <script crossorigin="anonymous" src="//s0.meituan.net/bs/?f=myfe/mywww:/stat.88d57c80.js"></script>
  <script>if(window.devicePixelRatio >= 2) { document.write('<link rel="stylesheet" href="//s0.meituan.net/bs/?f=myfe/mywww:/image-2x.8ba7074d.css"/>') }</script>
  <style>
    @font-face {
      font-family: stonefont;
      src: url('//vfile.meituan.net/colorstone/7d447601254e82cac54e33dfd85a80713168.eot');
      src: url('//vfile.meituan.net/colorstone/7d447601254e82cac54e33dfd85a80713168.eot?#iefix') format('embedded-opentype'),
           url('//vfile.meituan.net/colorstone/b65837e3a66c7467aaf7d91a1624ae2b2080.woff') format('woff');
    }

    .stonefont {
      font-family: stonefont;
    }
  </style>
</head>
<body>


<div class="header">
  <div class="header-inner">
        <a href="/" class="logo" data-act="icon-click"></a>
        <div class="city-container" data-val="{currentcityid:1 }">
            <div class="city-selected">
                <div class="city-name">
                  北京
                  <span class="caret"></span>
                </div>
            </div>
            <div class="city-list" data-val="{ localcityid: 1 }">
                <div class="city-list-header">定位城市：<a class="js-geo-city">北京</a></div>
                
            </div>
        </div>


        <div class="nav">
            <ul class="navbar">
                <li><a href="/" data-act="home-click"  >首页</a></li>
                <li><a href="/films" data-act="movies-click" >电影</a></li>
                <li><a href="/cinemas" data-act="cinemas-click" >影院</a></li> 
                <li><a href="http://www.gewara.com">演出</a></li>
                
                <li><a href="/board" data-act="board-click"  class="active" >榜单</a></li>
                <li><a href="/news" data-act="hotNews-click" >热点</a></li>
                <li><a href="/edimall"  >商城</a></li>
            </ul>
        </div>

        <div class="user-info">
            <div class="user-avatar J-login">
              <img src="https://p0.meituan.net/movie/7dd82a16316ab32c8359debdb04396ef2897.png">
              <span class="caret"></span>
              <ul class="user-menu">
                <li><a href="javascript:void 0">登录</a></li>
              </ul>
            </div>
        </div>

        <form action="/query" target="_blank" class="search-form" data-actform="search-click">
            <input name="kw" class="search" type="search" maxlength="32" placeholder="找影视剧、影人、影院" autocomplete="off">
            <input class="submit" type="submit" value="">
        </form>

        <div class="app-download">
          <a href="/app" target="_blank">
            <span class="iphone-icon"></span>
            <span class="apptext">APP下载</span>
            <span class="caret"></span>
            <div class="download-icon">
                <p class="down-title">扫码下载APP</p>
                <p class='down-content'>选座更优惠</p>
            </div>
          </a>
        </div>
    
  </div>
</div>
<div class="header-placeholder"></div>

<div class="subnav">
  <ul class="navbar">
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:7}"
          data-state-val="{subnavId:7}"
          class="active" href="javascript:void(0);"
      >热映口碑榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:6}"
          href="/board/6"
      >最受期待榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:1}"
          href="/board/1"
      >国内票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:2}"
          href="/board/2"
      >北美票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:4}"
          href="/board/4"
      >TOP100榜</a>
    </li>
  </ul>
</div>


    <div class="container" id="app" class="page-board/index" >

<div class="content">
    <div class="wrapper">
        <div class="main">
            <p class="update-time">2019-04-08<span class="has-fresh-text">已更新</span></p>
            <p class="board-content">榜单规则：将昨日国内热映的影片，按照评分从高到低排列取前10名，每天上午10点更新。相关数据来源于“猫眼专业版”及“猫眼电影库”。</p>
            <dl class="board-wrapper">
                <dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1167831" title="波西米亚狂想曲" class="image-link" data-act="boarditem-click" data-val="{movieId:1167831}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/d94e5c3054778f6f48bff3a813b0b7cd5300998.jpg@160w_220h_1e_1c" alt="波西米亚狂想曲" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1167831" title="波西米亚狂想曲" data-act="boarditem-click" data-val="{movieId:1167831}">波西米亚狂想曲</a></p>
        <p class="star">
                主演：拉米·马雷克,本·哈迪,约瑟夫·梅泽罗
        </p>
<p class="releasetime">上映时间：2019-03-22</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/1206605" title="绿皮书" class="image-link" data-act="boarditem-click" data-val="{movieId:1206605}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/c9b280de01549fcb71913edec05880585769972.jpg@160w_220h_1e_1c" alt="绿皮书" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1206605" title="绿皮书" data-act="boarditem-click" data-val="{movieId:1206605}">绿皮书</a></p>
        <p class="star">
                主演：维果·莫腾森,马赫沙拉·阿里,琳达·卡德里尼
        </p>
<p class="releasetime">上映时间：2019-03-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-3">3</i>
    <a href="/films/1212492" title="老师·好" class="image-link" data-act="boarditem-click" data-val="{movieId:1212492}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/b8821d597382e319f9679b7e24e49d113204356.jpg@160w_220h_1e_1c" alt="老师·好" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1212492" title="老师·好" data-act="boarditem-click" data-val="{movieId:1212492}">老师·好</a></p>
        <p class="star">
                主演：于谦,汤梦佳,王广源
        </p>
<p class="releasetime">上映时间：2019-03-22</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-4">4</i>
    <a href="/films/1239544" title="调音师" class="image-link" data-act="boarditem-click" data-val="{movieId:1239544}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/29caaa1b66c95807a3f4d29b5b03644b1876102.jpg@160w_220h_1e_1c" alt="调音师" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1239544" title="调音师" data-act="boarditem-click" data-val="{movieId:1239544}">调音师</a></p>
        <p class="star">
                主演：阿尤斯曼·库拉纳,塔布,拉迪卡·艾普特
        </p>
<p class="releasetime">上映时间：2019-04-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-5">5</i>
    <a href="/films/1220571" title="我的英雄学院：两位英雄" class="image-link" data-act="boarditem-click" data-val="{movieId:1220571}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/a053d99960838d4085004233cdf8d43e3502877.jpg@160w_220h_1e_1c" alt="我的英雄学院：两位英雄" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1220571" title="我的英雄学院：两位英雄" data-act="boarditem-click" data-val="{movieId:1220571}">我的英雄学院：两位英雄</a></p>
        <p class="star">
                主演：山下大辉,三宅健太,志田未来
        </p>
<p class="releasetime">上映时间：2019-03-15</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-6">6</i>
    <a href="/films/1211727" title="反贪风暴4" class="image-link" data-act="boarditem-click" data-val="{movieId:1211727}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/c63849c7a9de360a7b192bc322792a111705236.jpg@160w_220h_1e_1c" alt="反贪风暴4" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1211727" title="反贪风暴4" data-act="boarditem-click" data-val="{movieId:1211727}">反贪风暴4</a></p>
        <p class="star">
                主演：古天乐,郑嘉颖,林峯
        </p>
<p class="releasetime">上映时间：2019-04-04</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-7">7</i>
    <a href="/films/247295" title="驯龙高手3" class="image-link" data-act="boarditem-click" data-val="{movieId:247295}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/9ef02a501fee7f62d49d2096b52175d32155331.jpg@160w_220h_1e_1c" alt="驯龙高手3" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/247295" title="驯龙高手3" data-act="boarditem-click" data-val="{movieId:247295}">驯龙高手3</a></p>
        <p class="star">
                主演：杰伊·巴鲁切尔,刘昊然,亚美莉卡·费雷拉
        </p>
<p class="releasetime">上映时间：2019-03-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-8">8</i>
    <a href="/films/346765" title="小飞象" class="image-link" data-act="boarditem-click" data-val="{movieId:346765}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/b9784931b6212e633978298fd827142b316254.jpg@160w_220h_1e_1c" alt="小飞象" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/346765" title="小飞象" data-act="boarditem-click" data-val="{movieId:346765}">小飞象</a></p>
        <p class="star">
                主演：科林·法瑞尔,迈克尔·基顿,丹尼·德维托
        </p>
<p class="releasetime">上映时间：2019-03-29</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/410629" title="阿丽塔：战斗天使" class="image-link" data-act="boarditem-click" data-val="{movieId:410629}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/fc4dd6cd0c6f7db566a128cc05c475355664427.jpg@160w_220h_1e_1c" alt="阿丽塔：战斗天使" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/410629" title="阿丽塔：战斗天使" data-act="boarditem-click" data-val="{movieId:410629}">阿丽塔：战斗天使</a></p>
        <p class="star">
                主演：罗莎·萨拉查,克里斯托弗·沃尔兹,基恩·约翰逊
        </p>
<p class="releasetime">上映时间：2019-02-22</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/507792" title="地久天长" class="image-link" data-act="boarditem-click" data-val="{movieId:507792}">
      <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/b8a625614c1d401d9cd170b092230ae01516197.jpg@160w_220h_1e_1c" alt="地久天长" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/507792" title="地久天长" data-act="boarditem-click" data-val="{movieId:507792}">地久天长</a></p>
        <p class="star">
                主演：王景春,咏梅,齐溪
        </p>
<p class="releasetime">上映时间：2019-03-22</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">9</i></p>        
    </div>

      </div>
    </div>

                </dd>
            </dl>

        </div>
    </div>
</div>

    </div>

<div class="footer">
    <p class="friendly-links">
        关于猫眼 :
        <a href="http://ir.maoyan.com/s/index.php#pageScroll0" target="_blank">关于我们</a>
        <span></span>
        <a href="http://ir.maoyan.com/s/index.php#pageScroll1" target="_blank">管理团队</a>
        <span></span>
        <a href="http://ir.maoyan.com/s/index.php#pageScroll2" target="_blank">投资者关系</a>
        &nbsp;&nbsp;&nbsp;&nbsp;
        友情链接 :
        <a href="http://www.meituan.com" data-query="utm_source=wwwmaoyan" target="_blank">美团网</a>
        <span></span>
        <a href="http://www.gewara.com" data-query="utm_source=wwwmaoyan">格瓦拉</a>
        <span></span>
        <a href="http://i.meituan.com/client" data-query="utm_source=wwwmaoyan" target="_blank">美团下载</a>
        <span></span>
        <a href="https://www.huanxi.com" data-query="utm_source=maoyan_pc" target="_blank">欢喜首映</a>
    </p>
    <p class="friendly-links">
      商务合作邮箱：v@maoyan.com
      客服电话：10105335
      违法和不良信息举报电话：4006018900
      <br/>
      投诉举报邮箱：tousujubao@meituan.com
      舞弊线索举报邮箱：wubijubao@maoyan.com
    </p>
    <p>
        &copy;2016
        猫眼电影 maoyan.com
        <a href="https://tsm.miit.gov.cn/pages/EnterpriseSearchList_Portal.aspx?type=0&keyword=京ICP证160733号&pageNo=1" target="_blank">京ICP证160733号</a>
        <a href="http://www.miibeian.gov.cn" target="_blank">京ICP备16022489号-1</a>
        <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003232" target="_blank">京公网安备 11010102003232号</a>
        <a href="/about/licence" target="_blank">网络文化经营许可证</a>
        <a href="http://www.meituan.com/about/rules" target="_blank">电子公告服务规则</a>
    </p>
    <p>北京猫眼文化传媒有限公司</p>
</div>

    <script crossorigin="anonymous" src="//www.dpfile.com/app/owl/static/owl_1.7.11.js"></script>
    <script>
      Owl.start({
        project: 'com.sankuai.movie.fe.mywww', 
        pageUrl: location.href.split('?')[0].replace(/\/\d+/g, '/:id'),
        devMode: false
      })
    </script>
    <!--[if IE 8]><script crossorigin="anonymous" src="//s0.meituan.net/bs/?f=myfe/mywww:/es5-shim.bbad933f.js"></script><![endif]-->
    <!--[if IE 8]><script crossorigin="anonymous" src="//s0.meituan.net/bs/?f=myfe/mywww:/es5-sham.d6ea26f4.js"></script><![endif]-->
    <script crossorigin="anonymous" src="//s0.meituan.net/bs/?f=myfe/mywww:/common.96772a2e.js"></script>
<script crossorigin="anonymous" src="//s0.meituan.net/bs/?f=myfe/mywww:/board-index.1a1ab13d.js"></script>
</body>
</html>

"""
r = '[\s\S]*?'
import re

# pattern = re.compile(
#     r'<dd>{}href="({})" title="({})"{}<img{}class="board-img" src="({})">{}<p class="star">({})</p>{}<p class="releasetime">({})</p>{}</dd>'.format(
#         r, r, r, r, r, r, r, r, r, r, r
#     ))
# ret = pattern.findall(s)
# for i in ret:
#     print(i)
# 第一步 得到所有的dd  一个dd是一部电影的信息
dd = re.compile(r'(<dd>{}</dd>)'.format(r))
dd_list = dd.findall(s)
url = 'https://maoyan.com/board'
movies = []
for dd in dd_list:
    # print(dd)
    # 第二步 从dd中提取每一部影片的信息
    title = re.search(r'title="({})"'.format(r), dd).group(1).strip()
    print(title)
    role = re.search(r'<p class="star">({})</p>'.format(r), dd).group(1).strip()
    print(role)
    time = re.search(r'<p class="releasetime">({})</p>'.format(r), dd).group(1).strip()
    print(time)
    img = re.findall(r'src="({})"'.format(r, r), dd)[1]
    print(img)
    # 第三步 将每部电影放进字典中
    print('--' * 22)
    movies.append({
        'title': title,
        'role': role,
        'time': time,
        'img': img
    })
    # exit()

# 打印电影
for movie in movies:
    print(movie)
