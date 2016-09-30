
### 首先，爬取链家 上海浦东新区、徐汇价位在2000到4000的一室户数据

使用scrapy，编写好爬虫，执行爬取命令，保存到result.csv文件中

    scrapy crawl lianjia -o result.csv -t csv


```python
# 读取数据
import pandas
df = pandas.read_csv('crawler/result.csv')
```


```python
# 统计下总个数
len(df)
```




    2239




```python
# 显示数据结构
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>floor</th>
      <th>url</th>
      <th>price</th>
      <th>title</th>
      <th>community</th>
      <th>location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>低层/6层</td>
      <td>http://sh.lianjia.com/zufang/shz3354705.html</td>
      <td>3000</td>
      <td>毗邻地铁，上门实勘，小户型，看房末班车</td>
      <td>东沟四村</td>
      <td>金桥</td>
    </tr>
    <tr>
      <th>1</th>
      <td>中层/11层</td>
      <td>http://sh.lianjia.com/zufang/shz2851576.html</td>
      <td>3500</td>
      <td>上门实勘，享受好房，一室小户型，抢手火热</td>
      <td>环龙公寓</td>
      <td>北蔡</td>
    </tr>
    <tr>
      <th>2</th>
      <td>低层/6层</td>
      <td>http://sh.lianjia.com/zufang/shz3407791.html</td>
      <td>2000</td>
      <td>业主降价，热门好房，交通便利，上门实拍</td>
      <td>玉兰苑（川沙）</td>
      <td>川沙</td>
    </tr>
    <tr>
      <th>3</th>
      <td>中层/5层</td>
      <td>http://sh.lianjia.com/zufang/shz3452689.html</td>
      <td>4000</td>
      <td>出行方便，如您所见，刚刚降价，上门实勘</td>
      <td>上钢一村</td>
      <td>世博</td>
    </tr>
    <tr>
      <th>4</th>
      <td>高层/27层</td>
      <td>http://sh.lianjia.com/zufang/shz3458271.html</td>
      <td>3800</td>
      <td>高区阳光房，上门实拍，链家房源，地铁沿线</td>
      <td>地杰国际城</td>
      <td>御桥</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 统计各个位置租房个数
df.groupby('location').size()
```




    location
    万体馆      14
    三林      180
    上海南站     54
    世博      172
    北蔡      173
    华东理工     91
    华泾       30
    南码头      53
    合庆        2
    周浦       96
    唐镇       38
    塘桥       22
    外高桥      75
    川沙       93
    康健       96
    康桥       50
    建国西路      4
    张江       71
    徐家汇      52
    徐汇滨江      4
    御桥       26
    惠南       14
    斜土路      25
    曹路       39
    杨东        5
    植物园      23
    泥城镇       1
    洋泾       72
    源深       26
    漕河泾      16
    潍坊       36
    田林       46
    碧云        7
    花木       14
    衡山路      22
    金杨      120
    金桥      210
    长桥       45
    陆家嘴      12
    高东       21
    高行       46
    龙华       43
    dtype: int64




```python
# 忽略几个离工作地点比较远的地方
ignore_location = ['周浦', '北蔡', '唐镇 ',  '外高桥', '川沙', '康健', '康桥', '御桥', '惠南', '曹路', '植物园', '金杨', '高东']
mask = df['location'].isin(ignore_location)
df = df[~mask]
```


```python
# 清理小区数据
df['community_c'] = df['community'].apply(lambda x: x.split('（')[0])

# 统计各个小区租房个数
df.groupby('community_c').size()
```




    community_c
    三杨新村一街坊        6
    三杨新村二街坊        3
    三林世博家园        12
    三林安居苑          2
    三林新村          21
    三林苑            2
    三林路430弄        1
    三江小区          12
    上南一村           5
    上南七村           3
    上南三村           4
    上南九村           1
    上南二村           6
    上南五村           2
    上南八村           6
    上南六村           4
    上南十一村          5
    上南十二村          1
    上南十村           5
    上南四村           7
    上南路3520弄       1
    上南路3827弄       2
    上南路3848弄       1
    上方花园           4
    上海新村           2
    上溶新村           2
    上缝小区           3
    上船大楼           1
    上钢一村           9
    上钢三村           3
                  ..
    阳光二村           7
    阳光城MODO自由区     2
    阳光城市家园         1
    阳光花城           1
    陆家嘴中央公寓        2
    陇南小区           5
    陈家宅小区          7
    陈家门小区          2
    香楠小区           8
    馨宁公寓           1
    高安路18弄         1
    高弘家苑           6
    高海家苑           3
    高行家园           1
    齐七小区           1
    齐二小区           4
    齐八小区           3
    齐友佳苑           1
    齐爱佳苑           6
    龙东花园           1
    龙华茶花园          1
    龙华路2373弄       1
    龙南七村           1
    龙南三村           2
    龙吴路11弄         1
    龙吴路13弄         2
    龙吴路410弄        2
    龙山新村           3
    龙州小区           1
    龙漕路66弄         1
    dtype: int64




```python
# 小区数
df.groupby('community_c').size().count()
```




    503




```python
# 获取各小区名
communities = list(set(df['community_c'].tolist()))
```


```python
# 名称转为坐标
import requests
import urllib

# 高德地图 key
key = 'XXXXXX'

# 地理编码
code_url = u'http://restapi.amap.com/v3/geocode/geo?key=' + key + '&city=shanghai&address={}'

def name2location(name):
    res = requests.get(code_url.format(urllib.quote(name)))
    data = res.json()['geocodes']
    if data:
        return data[0]['location']
    else:
        return None
```


```python
# 目的地
destination = "卢湾区淮海中路381号中环广场"

# 获取目的地坐标
destination_location = name2location(destination)

# 获取小区名称为坐标
community_locations = dict()
for c in communities:
    loc = name2location(c)
    if loc:
        community_locations[c] = name2location(c)
```


```python
# 计算小区到目的地时间

durations = dict()
for (k,v) in community_locations.items():
    durations[k] = get_duration(v)
```


```python
# 添加坐标信息
df['community_loc'] = df['community_c'].apply(lambda x: community_locations[x] if x in community_locations else None)
```


```python
# 添加时间信息
df['duration'] = df['community_c'].apply(lambda x: durations[x] if x in durations else None)
```


```python
#  保存计算结果
df.sort_values(by=['duration', 'price'])
df.to_csv('house.csv')
```


```python
df.head()

```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>floor</th>
      <th>url</th>
      <th>price</th>
      <th>title</th>
      <th>community</th>
      <th>location</th>
      <th>community_c</th>
      <th>community_loc</th>
      <th>duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>638</th>
      <td>低层/4层</td>
      <td>http://sh.lianjia.com/zufang/shz3447021.html</td>
      <td>3800</td>
      <td>上方花园，新鲜好房，地铁沿线，1室1厅1卫</td>
      <td>上方花园</td>
      <td>衡山路</td>
      <td>上方花园</td>
      <td>121.451190,31.212590</td>
      <td>569.0</td>
    </tr>
    <tr>
      <th>155</th>
      <td>高层/3层</td>
      <td>http://sh.lianjia.com/zufang/shz3413139.html</td>
      <td>4000</td>
      <td>采光无敌好，1室0厅1卫，一链倾城，有钥匙</td>
      <td>上方花园</td>
      <td>衡山路</td>
      <td>上方花园</td>
      <td>121.451190,31.212590</td>
      <td>569.0</td>
    </tr>
    <tr>
      <th>592</th>
      <td>高层/3层</td>
      <td>http://sh.lianjia.com/zufang/shz3423023.html</td>
      <td>2000</td>
      <td>上方花园，有爱有家，远离雾霾带，一室小户型</td>
      <td>上方花园</td>
      <td>衡山路</td>
      <td>上方花园</td>
      <td>121.451190,31.212590</td>
      <td>569.0</td>
    </tr>
    <tr>
      <th>595</th>
      <td>低层/4层</td>
      <td>http://sh.lianjia.com/zufang/shz3429361.html</td>
      <td>3800</td>
      <td>上方花园，真实在租，上下楼方便，温馨一室</td>
      <td>上方花园</td>
      <td>衡山路</td>
      <td>上方花园</td>
      <td>121.451190,31.212590</td>
      <td>569.0</td>
    </tr>
    <tr>
      <th>557</th>
      <td>中层/3层</td>
      <td>http://sh.lianjia.com/zufang/shz3386110.html</td>
      <td>3500</td>
      <td>紧邻地铁，好楼层，上门实拍，温馨一室</td>
      <td>华亭路31弄</td>
      <td>衡山路</td>
      <td>华亭路31弄</td>
      <td>121.450167,31.215623</td>
      <td>696.0</td>
    </tr>
  </tbody>
</table>
</div>


