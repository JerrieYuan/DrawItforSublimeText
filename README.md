# DrawItforSublimeText
A sublime text plugin to draw square(一个sublime text的插件，用于绘制矩形）

![image](http://ww2.sinaimg.cn/large/a6a49aa8gw1f0oxmetfquj20ks0ixjux.jpg)

```

                                        +----------+
               +-----------+            |          |
               |           |         +--> drawit   |
               | sublime   |>--------+  |          |
               |  text2    |            +----------+
               |           |
               +-----------+
```

It only has some Simple functions  
A little ugly          

只有一些相当简单的功能，只能画框，箭头请用< > ^ V 将就下 =-=

Tools -> new plugin,

Then the sublime text will create a new plugin file for you。
copy the code of drawit.py to  it

把drawit.py的代码，复制到sublime给你生成的新插件文件中

You may need set your keybidings like this:
设置你的按键map：
 
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
    }

```

If your key bidings file is empty,after you edit ,it may like this:
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
    }
]
```

Save it.

Then , you can press "Ctrl + ↑", "Ctrl + ←", "Ctrl + →", "Ctrl + ↓" to draw a square.

In fact,this is my first Python Script.
If there is any bug, please forgive me and conatct me with email jerrieyuan@hotmail.com or submit an issue
Thanks!

这是我写的第一个Python脚本，之前从没接触过Python，没想到上手把功能写完了。
磕磕碰碰的。
如果有任何bug，或者觉得代码烂，请谅解，并通过邮箱联系我：jerrieyuan@hotmail.com 或提交 issue 。。
