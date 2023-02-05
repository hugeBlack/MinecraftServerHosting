# skinRestorer遇到的问题

## 皮肤无法更新

在minecraft.net更新皮肤以后skinRestorer没反应，过了好长时间还是老皮肤，所以[写了个脚本](/assets/skinFileGen.py)来生成正版玩家的皮肤文件，输入玩家名即可生成永久不过期的.skin文件，放入`plugins/SkinsRestorer/Skins`文件夹下即可手动更新皮肤

*.skin文件参考了[官方文档](https://github.com/SkinsRestorer/SkinsRestorerX/wiki/About-.skin-&-.player)，同时使用[Mojang的API](https://wiki.vg/Mojang_API#UUID_to_Profile_and_Skin.2FCape)