# Subl 小工具

一些写来自用的Sublime Text小工具，如果能给你的工作带来便捷，就再好不过了。

[keymap](https://code.aliyun.com/JRY/subltips/blob/master/Default.sublime-keymap)

## DrawItforSublimeText

支持sublime Text 2/3

（橡皮擦功能正在编写中……摔！）

一个sublime text的插件，用于绘制矩形

只有一些相当简单的功能，只能画框，箭头请用< > ^ V 将就下。

效果如下：


```

                                        +----------+
               +-----------+            |          |
               |           |         +--> drawit   |
               | sublime   |>--------+  |          |
               |  text2    |            +----------+
               |           >---------+
               +-----------+         |
                                     |                  +-------+
                                     |                  |       |
It only has some Simple functions    +------------------> 你好  |
A little ugly                                           |       |
                                                        |       |
                                                        +-------+
```



Tools -> new plugin,

把drawit_v2.py/drawit_v3.py（对应相应的sublime版本）的代码，复制到sublime给你生成的新插件文件中

设置你的按键map：

  Preferences ---->  Key Bidings - Users

增加：

```json
    {
        "command":"up",
        "keys":[
            "ctrl+up"
        ]
    },
    {
        "command":"down",
        "keys":[
            "ctrl+down"
        ]
    },
    {
        "command":"left",
        "keys":[
            "ctrl+left"
        ]
    },
    {
        "command":"right",
        "keys":[
            "ctrl+right"
        ]
    },
    {
        "command":"space",
        "keys":[
            "ctrl+space"
        ]
    }


```

## GoClean

[代码](https://code.aliyun.com/JRY/subltips/blob/master/goclean.py)

当你自己在编写库的时候，每次保存后，文件并不会重新编译成.a文件。

在linux下，安装gosublime似乎能在import一个缺失的包时，自动编译出包文件。但如果一个包本来是存在的，它的代码更新后，不会去重新编译包。

并且，在windows下，似乎自动编译缺失包这个功能不大能正常运行……

这个工具，在你编辑好代码后，按下CTRL+SHIFT+C，自动把包编译到pkg目录下，其实就是运行了一次go install。

因为go install 本身会检测代码和包的日期时间，所以如果在上次编译后，代码没有修改，则不会重新编译。

需要修改key map如下:

```json
[
	{
        "command":"goclean",
        "keys":[
            "ctrl+shift+c"
        ]
    }
]
```