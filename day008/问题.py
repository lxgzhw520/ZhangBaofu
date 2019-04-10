# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/8 19:31
# 文件名称: 问题.py
# 开发工具: PyCharm

s = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>中国银行_金融市场_外汇牌价</title>
<meta content="" name="keywords" />
<meta content="" name="description" />
<link href="/images/boc2013_common.css" rel="stylesheet" type="text/css" ignoreapd="1">
<link href="/images/boc2013_reset.css" rel="stylesheet" type="text/css" ignoreapd="1">
<link href="/images/boc2013_pages.css" rel="stylesheet" type="text/css" ignoreapd="1">
<script language="JavaScript" src="/head.js" ignoreapd="1"></script>
<script language="JavaScript" src="/bottom.js" ignoreapd="1"></script>
<script language=javascript src="../images/boc2013_search.js"></script> 
<script language=javascript src="../images/WebCalendar.js"></script> 
</head>

<body>
<div class="wrapper">
	<!--头部模板start-->
			<script language="JavaScript">
			<!--
			createTop();
			//-->
			</script>
			<!--头部模板end-->
    <!--cramb-->
    <div class="cramb"><span>当前位置：</span><a href="/index.html">首页</a> &gt; <a href="/fimarkets">金融市场</a> &gt; 外汇牌价</div>
    
    <div class="per_bank_login">
    	<a href="#" class="hover_btn">网银登录</a>
        <div class="hover_menu">
        	<ul>
        		<li><a href="/ebanking/bocnet_login/index.html">个人客户网银登录</a></li>
                <li><a href="/ebanking/bocnet_login/index1.html">个人贵宾网银登录</a></li>
                <li class="last"><a href="/ebanking/bocnet_login/index2.html">企业客户网银登录</a></li>
        	</ul>
        </div>
    </div>
    
   	<div class="BOC_main">
    	<div class="publish" style="float:left;width:980px;">
        	<h2 class="title">中国银行外汇牌价<br /><!-- <span>2014年01月07日</span> --></h2>
            <!--分享 打印-->
            <div class="function">
            	<!-- <a href="#" class="share">分享</a> -->
                <a href="javascript:window.print()" class="print">打印</a>
                <!-- <ul class="share_pop">
                	<li><a href="#" class="sina" title=""></a></li>
                    <li><a href="#" class="wb" title=""></a></li>
                    <li><a href="#" class="wx" title=""></a></li>
                    <li><a href="#" class="qzone" title=""></a></li>
                </ul> -->
            </div><!--分享 打印-->
            <!--发布-->
                        <div>
<div class="main" id="DefaultMain" >
<form method="post" name="historysearchform" id="historysearchform" action="search.jsp">
<div class="invest_t" style="float:left;width:980px;padding-bottom:15px;">
<style>
.invest_t table td,.publish table th ,.publish table tr{
	font-size:12px;
}
.invest_t table tr td select{
	height:30px;
}
.invest_t table tr th select{
	height:auto;
}
.invest_t select{
	width:auto;
	height:auto;
}
#calendarTable tr td{
	font:12px Verdana,Geneva,sans-serif,"宋体"
}
</style>
	<table cellpadding="0" cellspacing="0" width="100%">
		<tr>
			<td align="right" width="8%">起始时间：</td>
			<td align="left" width="100px;">
				<div class="search_bar" style="float:left;width:100px;margin-left:10px;">
					<input class="search_ipt" style="width:100px;" type="text" name="erectDate" id="erectDate" onclick="new Calendar(2001, 2019,0).show(this);">
				</div>
			</td>
			<td align="right" width="8%">结束时间：</td>
			<td align="left" width="100px;">
				<div class="search_bar" style="float:left;width:100px;margin-left:10px;">
					<input class="search_ipt" style="width:100px;" type="text" name="nothing" id="nothing" onclick="new Calendar(2001, 2019,0).show(this);">
				</div>
			</td>
			<td align="right" width="10%">牌价选择：</td>
			<td align="left" width="100px;">
				<select name="pjname" id="pjname">
					<option value="0">选择货币</option>
					<option value="1314">英镑</option>
					<option value="1315">港币</option>
					<option value="1316">美元</option>
					<option value="1317">瑞士法郎</option>
					<option value="1318">德国马克</option>
					<option value="1319">法国法郎</option>
					<option value="1375">新加坡元</option>
					<option value="1320">瑞典克朗</option>
					<option value="1321">丹麦克朗</option>
					<option value="1322">挪威克朗</option>
					<option value="1323">日元</option>
					<option value="1324">加拿大元</option>
					<option value="1325">澳大利亚元</option>
					<option value="1326">欧元</option>
					<option value="1327">澳门元</option>
					<option value="1328">菲律宾比索</option>
					<option value="1329">泰国铢</option>
					<option value="1330">新西兰元</option>
					<option value="1331">韩元</option>
					<option value="1843">卢布</option>
					<option value="2890">林吉特</option>
					<option value="2895">新台币</option>
					<option value="1370">西班牙比塞塔</option>
					<option value="1371">意大利里拉</option>
					<option value="1372">荷兰盾</option>
					<option value="1373">比利时法郎</option>
					<option value="1373">芬兰马克</option>
					<option value="3030">印尼卢比</option>
					<option value="3253">巴西里亚尔</option>
                    <option value="3899">阿联酋迪拉姆</option>
                    <option value="3900">印度卢比</option>
                    <option value="3901">南非兰特</option>
                    <option value="4418">沙特里亚尔</option>
                    <option value="4560">土耳其里拉</option>
				</select>
			</td>
			<td align="left" width="30px;">
				<input class="search_btn" style="float:right;margin-righth:26px;" type="button" onclick="search_for_whpj()">
			</td>
			<td width="350px;" align="right"><div style="text-align:right; margin-right:30px;"><a href="http://www.bankofchina.com/custserv/bi2/201903/t20190322_14995133.html" style="color:#000" target="_blank">【关于远离违法违规外汇交易的风险提示】</a></div></td>
		</tr>
	</table>
	</div>
</form>	 

</div>

                <table cellpadding="0" align="left" cellspacing="0" width="100%">
                	<tr>
                    	<th>货币名称</th>
                        <th>现汇买入价</th>
                        <th>现钞买入价</th>
                        <th>现汇卖出价</th>
                        <th>现钞卖出价</th>
                        <th>中行折算价</th>
                        <th>发布日期</th>
                        <th>发布时间</th>
                    </tr>
					 
					  
                    <tr>
                    	<td>阿联酋迪拉姆</td>
                        <td></td>
                        <td>176.51</td>
                        <td></td>
                        <td>189.31</td>
                        <td>182.96</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>澳大利亚元</td>
                        <td>475.91</td>
                        <td>461.13</td>
                        <td>479.41</td>
                        <td>480.58</td>
                        <td>477.08</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>巴西里亚尔</td>
                        <td></td>
                        <td>166.57</td>
                        <td></td>
                        <td>182.19</td>
                        <td>173.45</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>加拿大元</td>
                        <td>500.82</td>
                        <td>485.01</td>
                        <td>504.52</td>
                        <td>505.74</td>
                        <td>502.46</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>瑞士法郎</td>
                        <td>669.7</td>
                        <td>649.03</td>
                        <td>674.4</td>
                        <td>676.62</td>
                        <td>672.03</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>丹麦克朗</td>
                        <td>100.82</td>
                        <td>97.7</td>
                        <td>101.62</td>
                        <td>101.91</td>
                        <td>100.97</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>欧元</td>
                        <td>753.22</td>
                        <td>729.82</td>
                        <td>758.78</td>
                        <td>760.46</td>
                        <td>753.74</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>英镑</td>
                        <td>873.88</td>
                        <td>846.73</td>
                        <td>880.32</td>
                        <td>882.46</td>
                        <td>876.05</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>港币</td>
                        <td>85.45</td>
                        <td>84.77</td>
                        <td>85.79</td>
                        <td>85.79</td>
                        <td>85.61</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>印尼卢比</td>
                        <td></td>
                        <td>0.0458</td>
                        <td></td>
                        <td>0.049</td>
                        <td>0.0475</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>印度卢比</td>
                        <td></td>
                        <td>9.0656</td>
                        <td></td>
                        <td>10.223</td>
                        <td>9.7101</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>日元</td>
                        <td>6.0079</td>
                        <td>5.8213</td>
                        <td>6.0521</td>
                        <td>6.0554</td>
                        <td>6.0173</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>韩国元</td>
                        <td>0.5843</td>
                        <td>0.5637</td>
                        <td>0.5889</td>
                        <td>0.6104</td>
                        <td>0.5909</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>澳门元</td>
                        <td>83.1</td>
                        <td>80.32</td>
                        <td>83.43</td>
                        <td>86.11</td>
                        <td>83.19</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>林吉特</td>
                        <td>165.39</td>
                        <td></td>
                        <td>166.88</td>
                        <td></td>
                        <td>164.37</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>挪威克朗</td>
                        <td>78.11</td>
                        <td>75.69</td>
                        <td>78.73</td>
                        <td>78.95</td>
                        <td>78.06</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>新西兰元</td>
                        <td>451.05</td>
                        <td>437.13</td>
                        <td>454.21</td>
                        <td>459.78</td>
                        <td>452.17</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>菲律宾比索</td>
                        <td>12.84</td>
                        <td>12.44</td>
                        <td>12.94</td>
                        <td>13.54</td>
                        <td>12.87</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>卢布</td>
                        <td>10.26</td>
                        <td>9.63</td>
                        <td>10.34</td>
                        <td>10.73</td>
                        <td>10.28</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>沙特里亚尔</td>
                        <td></td>
                        <td>174.15</td>
                        <td></td>
                        <td>183.21</td>
                        <td>179.18</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>瑞典克朗</td>
                        <td>72.11</td>
                        <td>69.88</td>
                        <td>72.69</td>
                        <td>72.89</td>
                        <td>72.3</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>新加坡元</td>
                        <td>493.92</td>
                        <td>478.67</td>
                        <td>497.38</td>
                        <td>498.87</td>
                        <td>495.92</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>泰国铢</td>
                        <td>20.94</td>
                        <td>20.29</td>
                        <td>21.1</td>
                        <td>21.75</td>
                        <td>21.06</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>土耳其里拉</td>
                        <td>117.87</td>
                        <td>112.09</td>
                        <td>118.81</td>
                        <td>134.06</td>
                        <td>119.18</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>新台币</td>
                        <td></td>
                        <td>21.02</td>
                        <td></td>
                        <td>22.67</td>
                        <td>21.78</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>美元</td>
                        <td>670.59</td>
                        <td>665.13</td>
                        <td>673.43</td>
                        <td>673.43</td>
                        <td>672.01</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
					  
                    <tr>
                    	<td>南非兰特</td>
                        <td>47.47</td>
                        <td>43.82</td>
                        <td>47.79</td>
                        <td>51.44</td>
                        <td>47.67</td>
                        <td>2019-04-08</td>
                        <td>19:28:40</td>
                    </tr>
					
                        
                   
                </table></div>
            </div><!--发布-end-->
            <div class="pb_ft clearfix" style="float:left;width:980px;margin-bottom: 20px;">
            <div class="turn_page">
            	<p>共<span>10</span>页</p>
                <ol>
                	<SCRIPT LANGUAGE="JavaScript">
function createPageHTML(_nPageCount, _nCurrIndex, _sPageName, _sPageExt){
	if(_nPageCount == null || _nPageCount<=1){
		return;
	}
	//制定一个分页的HTML
	var pagehtml = "";
	//当前显示的页数信息
	var nCurrIndex = _nCurrIndex || 0;
	//当前显示第1页
	if(nCurrIndex == 1 || nCurrIndex == 0)
		pagehtml += '<li class="turn_pre"><a href="'+_sPageName+ '.'+_sPageExt+'">上一页</a></li>';
	else
		pagehtml += '<li class="turn_pre"><a href="'+_sPageName+'_' + (nCurrIndex-1) + '.'+_sPageExt+'">上一页</a></li>';
	//得到中间的部分
	pagehtml += getPageStr(_nPageCount,(_nCurrIndex+1), _sPageName, _sPageExt);
	//显示下一页信息
	if(nCurrIndex == (_nPageCount-1))
		pagehtml += '<li class="turn_next"><a href="'+_sPageName+'_'+(_nPageCount-1)+'.'+_sPageExt+'">下一页</a></li>';
	else
		pagehtml += '<li class="turn_next"><a href="'+_sPageName+'_'+(nCurrIndex+1)+'.'+_sPageExt+'">下一页</a></li>';
	document.write(pagehtml);
}
//页码显示函数
function getPageStr(pages,dbpage, _sPageName, _sPageExt)
{
	var curpage = parseInt(dbpage);
	var start = curpage - 2;
	var end = curpage +2;
	//对页码显示范围进行分析
	if(start < 1)
	{
		end = end - start + 1;
		if(end > pages)
			end = pages;
		start = 1;
	}
	if(end > pages)
	{
		start = start - (end - pages);
		if(start < 1)
			start = 1;
		end = pages;
	}
	var pagestr = "";
	for(var i=start;i<=end;i++)
	{
		if(i == curpage){
			if(i == 1)
				pagestr += '<li><a href="'+_sPageName+'.'+_sPageExt+'" class="current">'+i+'</a></li>';
			else
				pagestr += '<li><a href="'+_sPageName+'_'+(i-1)+'.'+_sPageExt+'" class="current">'+i+'</a></li>';
		}
		else{
			if(i == 1)
				pagestr += '<li><a href="'+_sPageName+'.'+_sPageExt+'">'+i+'</a></li>';
			else
				pagestr += '<li><a href="'+_sPageName+'_'+(i-1)+'.'+_sPageExt+'">'+i+'</a></li>';
		}
	}
	return pagestr;
}
createPageHTML(10, 0, "index", "html");
</SCRIPT>

                </ol>
            </div><!--翻页-->
            <!-- <a class="search_lk" href="#">往日外汇牌价搜索</a> -->
    	
<table width="980" border="0" cellpadding="5" cellspacing="0" align="center">
		<tr>
	              <td height="70" class='nav'>

中国银行外汇牌价网页声明：<br>
1.本汇率表单位为100外币换算人民币，仅供参考，客户办理结/购汇业务时，应以中国银行网上银行、手机银行、智能柜台或网点柜台实际交易汇率为准，对使用该汇率表所导致的结果，中国银行不承担任何责任； <br>
2.未经中国银行许可，不得以商业目的转载本汇率表的全部或部分内容，如需引用相关数据，应注明来源于中国银行； <br>
3.中国银行外汇牌价业务系统于2011年10月30日进行了升级，本汇率表原有的"卖出价"细分为"现汇卖出价"和"现钞卖出价"，此前各货币的"卖出价"均显示在"现汇卖出价"项下。<br>
4.具体兑换币种以当地中国银行实际开办币种为准，客户可前往当地中国银行网点咨询或致电95566。<br>
			</td> 
		</tr>
	</table>
	</div><!--content--end-->
   </div>
 </div><!--main-end-->
    
<table width="980" border="0" align="center" cellpadding="0" cellspacing="0" bgcolor="#FFFFFF">
	<tr>
		<td>
			<!--尾部模板start-->
			<script language="JavaScript">
			<!--
			createBottom();
			//-->
			</script>
			<!--尾部模板end-->
		</td>
	</tr>
</table>

<!--footer-end-->

</div><!--wrapper-end-->
<script type="text/javascript" src="/images/boc2013_jquery-min.js" ignoreapd="1"></script>
<script type="text/javascript" src="/images/boc2013_boc.js" ignoreapd="1"></script>
</body>
</html>
"""

# 要从中取出 美元的那一行
import re

pattern = re.compile(r'<td>(.*?)</td>')
# print(pattern.findall(s))
new_list = pattern.findall(s)
# temp_list = []
# for i in pattern.findall(s):
#     print(i)
#     if i == '美元':
#         temp_list.append(i)
#     elif i == '南非兰特':
#         break
# print(temp_list)
print(new_list)
# 得到美元下标
print(new_list.index('美元'))
index = new_list.index('美元')
print(new_list[index:index + 8])
