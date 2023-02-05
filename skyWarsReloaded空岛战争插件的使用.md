# skyWarsReloaded空岛战争插件的使用

[skyWars插件官网](https://www.spigotmc.org/resources/skywarsreloaded-updated-recoded-1-19-support-new-features-1-8x-1-19x.69436/)

## 使用方法

导入新地图(需要先完成slimeWorldManager的操作)

1. 在`/home/container/plugins/Skywars/mapsData`下，创建`<your-map-name>.yml`
2. 使用`/sw reload`
3. 使用`/swmap legacyload <your-map-name>`，对地图内宝箱初始化，默认为NORMAL
4. 使用`/swmap edit <your-map-name>`，开始编辑出生点、宝箱等
5. 使用`/swmap save <your-map-name>`保存地图
6. 使用`/swmap register <your-map-name>`将地图加入游戏列表

常用编辑指令

设置玩家出生点`/swmap spawn player`
设置宝箱`/swmap chesttype <your-map-name>`
