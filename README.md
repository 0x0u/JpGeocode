# JpGeocode

https://pypi.org/project/JpGeocode/  
データ元: [Google Maps API](https://cloud.google.com/maps-platform/?hl=ja)
## なにこれ
日本の市区町村名を入れて座標を出すやつ。

## インストール
pipでインストールします。
```
$ pip3 install JpGeocode
```

## 使い方
インポート
```python
import JpGeocode
```

北海道札幌市の座標を検索(`都道府県名,市町村名`を指定します)
```Python
name = '北海道,札幌市'
geocode = JpGeocode.jpgeocode(name)
print(geocode)

## => {'lat': 43.0620958, 'lng': 141.3543763}
```
