# 使用slimeWorldManager

## 简介

slimeWorldManager(SWM)是一个世界管理器，其特点是使用slime格式存储世界的数据，适用于不太需要保存，经常需要读取的**小型**小游戏地图，如空岛、起床战争等。整个世界在首次加载时直接完全加载到内存中，这样一来每次需要重新读取时都直接从内存中读出，以内存为代价提高了服务器的运行速度。

先前的[Slime World Manager](https://github.com/Grinderwolf/Slime-World-Manager)已经停止维护，仍然活跃的是[Advanced Slime World Manager](https://github.com/InfernalSuite)，是前者的一个分支，其开发者也在开发一个整合了SWM的Paper服务端，目前还在Bata阶段。


## 安装方法

其分为两个部分：class-modifier和插件部分，在使用时两个部分都需要正确安装，安装方法详见[官方教程](https://github.com/InfernalSuite/Advanced-Slime-World-Manager/blob/develop/.docs/usage/install.md)

一般来说，最新版都在discord服务器上发布，没有找到合适的版本可以去那里看看。

## 将原有的世界导入SWM

1. 在导入之前，先设定好世界的Gamerule，如怪物破坏等规则，之后修改可能比较麻烦；然后建议用工具删除不需要的区块，来减少世界的体积，使得转换后的世界文件体积更小。

2. 将要导入的原版世界文件夹复制到服务器根目录（核心所在的目录），重启服务器，用`/swm list [页数]`查看导入的世界名称
3. 先用`/swm unload <world>`卸载世界，如果提示世界已经被卸载了就直接看下一步
4. 用`/swm import <path-to-world> <data-source> [new-world-name]`指令转换世界，其中
    - `path-to-world`为世界文件夹相对服务端根目录的相对路径，在这里我们直接填入文件夹的名称即可
    - `data-source`在这里我们直接定为file
    - `new-world-name`新世界的名称，可不填，默认为文件夹的名称
5. 可能会提示确认，重新输入一遍同样的命令即可
6. 此时已经导入成功了，可以用指令`/swm goto <world>`前往新导入的世界，如果不需要可以直接删除根目录下原版的世界了

其他的管理相关指令可以看[这里](https://github.com/Grinderwolf/Slime-World-Manager/blob/develop/.docs/usage/commands-and-permissions.md)

## 修改Slime格式世界的选项

具体的官方教程可以[看这里](https://github.com/Grinderwolf/Slime-World-Manager/blob/develop/.docs/config/configure-world.md)

我们在这里注意两个key：
- loadOnStartup: false 开服时加载。对于某些没有适配SWM的插件，可以通过设为`true`，来开服加载的方式让它们检测到世界的存在；对于适配了SWM的插件（比较少），这些插件可能会在合适的时候去加载世界，此时true或false都可。
- readOnly: true 世界只读。将这项设置为true后该世界就变为只读状态，所有对世界的更改不会保存到硬盘，设为false时在关服时地图会保存。