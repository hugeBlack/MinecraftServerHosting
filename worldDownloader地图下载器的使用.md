# 使用WorldDownloader

## 简介

World Downloader是一个外部工具，可以在不修改客户端的情况下下载服务器的地图

## 仓库

[World Downloader仓库](https://github.com/mircokroon/minecraft-world-downloader)

## 使用步骤

1. 要下载正版服的地图的话要先在Authentication里登录
2. 输入server address后点start
3. 客户端连接localhost后即开始下载
4. 进入要下载的世界
5. 开始跑图，直到软件界面上完整显示出要下载的全部地图
6. 点击右键菜单选择"Save & Exit"保存结果
7. 导出有用的地图
8. 进入导出的地图进行完整性检查

## Minecraft地图存储方式

Minecraft的地图文件都存在一个个.mca文件中，每个文件中都存储32*32个区块，其位于世界的`<存档文件夹>\region`的文件夹中，或者`<存档文件夹>\dimensions\<世界名称>\region`，具体请看Wiki对[MCA文件的介绍](https://minecraft.fandom.com/wiki/Region_file_format)

另见Wiki[对JE存档目录结构的介绍](https://minecraft.fandom.com/wiki/Java_Edition_level_format)

## 下载时的注意事项

1. 在下载时需要时刻注意要下载的世界名称，可以在F3界面看世界名称。一般显示在XYZ坐标上面一行
2. 下载完后记得记录下载区域的坐标，以免找不到
3. 要注意如果某个世界和要下载的世界名称相同，在下载前要记得右键选择'Delete All Downloaded Chunks'来删除之前下载的世界，如果不这么做则可能会出现两个两个世界出现在一个地图上的情况
4. 如果要下载的两个世界名称相同，则下完一个，导出，检查完，清除下载区块后再下载另一个世界
5. 在软件中发现世界已经全部下载完后及时右键点击'Pause Chunk Saving'以暂停区块下载，来防止其他玩家放置的方块干扰下载的文件

## 地图导出方式

根据服务器配置的不同，下载到的位置也不同，存在以下两种情况。注意，在这两种情况可能混合出现：

1. 当你处于要下载的世界中时，F3界面显示的名称为`minecraft:overworld`（一般出现在跨多个老版本的服务器上）
    
    在这种情况下，世界的区块文件直接存储在`<存档文件夹>\region`中，要单独提取这一个世界，可以进入下载的世界文件夹，将除了region文件夹外的所有文件**全部删除**（这是为了防止MC主动去生成没下载的世界浪费时间），然后[加入本仓库的提供的level.dat](./assets/level.dat)，这是一个虚空图的level.dat，可以防止进入地图后生成不想要的区块。

2. 如果服务器对每个世界都给不同的名字的话则在`<存档文件夹>\dimensions\<世界名称>`中可以找到，世界的region文件夹。
    
    在这种情况下，下载的时候每个维度会被下载到dimensions文件夹的子文件夹下，在`<存档文件夹>\dimensions\<世界名称>`目录下加一个[加入本仓库的提供的level.dat](./assets/level.dat)即可使用。

## 在检查和扫尾工作时可以使用以下一些指令

```
/kill @e[type=!player]
```
可以清除所有除玩家外的实体（生物、盔甲架等）