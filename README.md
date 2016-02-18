# DrawItforSublimeText
A sublime text plugin to draw square

** Only for Sublime Text2 **


![image](https://camo.githubusercontent.com/441da231d776da1fe52e4060ed1e4fbb73b76bf3/687474703a2f2f7777322e73696e61696d672e636e2f6c617267652f613661343961613867773166306f786d65746671756a32306b733069786a75782e6a7067)

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

Then the sublime text will create a new plugin file for you.

copy the code of drawit.py to  it


You may need set your keybidings like this:

  Preferences ---->  Key Bidings - Users

Add the followings:

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

If your key bidings file is empty,after you edit ,it may like this:

```json
[
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
]
```

Save it.

Then , you can press "Ctrl + ↑", "Ctrl + ←", "Ctrl + →", "Ctrl + ↓" "Ctrl + Space" to draw a square.

Ctrl + Space is for eraser.

In fact,this is my first Python Script.

If there is any bug, please forgive me and conatct me with email jerrieyuan@hotmail.com or submit an issue.

Thanks!




中文版：
一个sublime text的插件，用于绘制矩形

只有一些相当简单的功能，只能画框，箭头请用< > ^ V 将就下 =-=

Tools -> new plugin,

把drawit.py的代码，复制到sublime给你生成的新插件文件中

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

如果一开始它是空的，修改后将会是这个样子：

```json
[
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
]
```

保存


这是我写的第一个Python脚本，之前从没接触过Python，没想到上手把功能写完了。

磕磕碰碰的。

如果有任何bug，或者觉得代码烂，请谅解，并通过邮箱联系我：jerrieyuan@hotmail.com 或提交 issue 。。
