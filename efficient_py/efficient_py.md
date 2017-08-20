# 8:利用assert语句发现问题
> ## 断言主要为测试程序服务，能够快速方便地检查程序的异常和发现不恰当的输入，可防止意想不到的情况出现。
> 语法：
>> assert expression1[,expression2]
>>
>> 其中expression1的值返回True or False,False引发AssertionError；expression2常用来传递异常信息
>
> tips:
>> 1.__debug__默认值为True,Python2.7无法修改此值
>>
>> 2.断言对性能有一定的影响，禁用断言需要在运行的脚本前加上 -O
>
> 注意
>> 1.不要滥用断言。
>>
>> 2.如果Python本身的一场能够处理就不需要使用断言。
>>
>> 3.不要使用断言来检查用户的输入。
>>
>> 4.使用断言检查函数的返回值是否合理。
>>
>> 5.当条件是业务逻辑继续下去的先决条件时可以使用断言。

# 9.数据交换值的时候不推荐使用中间变量
> 一般情况下Python表达式的计算是**从左到右**，但遇到**表达式赋值**的时候表达式右边的操作数先于左边的操作数计算。

# 10.充分利用Lazy evaluation的特性
> 1.避免不必要的计算，带来性能上的提升。
>
> 2.节省空间，使得无限循环的数据接口成为可能。例如生成器。

# 12.不推荐使用type来进行类型检查
> 1.基于内建类型拓展的自定义类型，type函数并不能准确返回结果。
>
> 2.对于古典类，任意类对象实例的type()返回结果都是<type 'instance'>。
# 13.尽量转换为浮点类型后再做除法
# 14.警惕eval()的安全漏洞
> 如果使用对象不是信任源，应该尽量避免使用eval，在需要使用eval的地方可用安全性更好的ast.literal_eval替代。
# 15.建议使用enumerate()获取序列迭代的索引和值
# 16.分清==和is的适用场景
> is表示的是对象标示符，x is y 仅当x和y是同一个对象的时候才返回True，x is b 基本相当于 id(x) == id(y)。
>
> ==表示的意思是相等,a==b 相当于a.\_\_eq_\_\(b)。
# 17.考虑兼容性，尽可能使用Unicode
> str和Unicode同是basestring的子类。
>
> 利用codecs模块处理文件开头存在BOM字符的文件。
# 18.构建合理的包层次管理module
> 合理组织代码，便于维护和利用。
>
> 能够有效的避免名称空间冲突。
# 19.有节制地使用from... import ...语句
> ## 注意
>> 1.优先使用import ...
>>
>> 2.有节制地使用from ... import ...
>>
>> 3.尽量避免使用 from ... import *，防止命名空间污染
> ## Python import 机制
>> ###Python 初始化加载一些内建模块到内存中存放在sys.modules中。当加载一个模块，解释器需要做以下操作：
>>> 1.检索sys.modules是否存在模块，存在则导入到当前局部命名空间，加载结束；不存在执行2。
>>>
>>> 2.为需要导入的模块创建一个字典对象，并将该对象信息插入到sys.modules中。
>>>
>>> 3.加载前确认是否需要对模块对应的文件进行编译，如果需要则先进行编译。
>>>
>>> 4.执行动态加载，在当前模块的命名空间中执行编译后的字节码，并将其中所有的对象放入模块对应的字典中。
>>>
>> **需要注意的是，直接使用import和使用from a import B 的形式这两者之间存在一定的差异，后者直接将B暴露于局部空间，而将a加载到sys.modules中。**
# 20.优先使用absolute import来导入模块
# 21.i+=1 不等于 ++i
# 22.使用with自动关闭资源
> ##with语句执行过程
>> 1.计算表达式的值，返回一个上下文管理器对象。
>>
>> 2.加载上下文管理器对象的__exit__()方法以备后用。
>>
>> 3.调用上下文管理器对象的__enter__()方法。
>>
>> 4.如果with语句设置了目标对象，则将__enter__()方法的返回值赋值给目标对象。
>>
>> 5.执行with中的代码块。
>>
>> 6.如果5代码正常结束，调用上下文管理器对象的__exit__()方法，其返回值直接忽略。
>>
>> 7.如果5代码执行过程中发生异常，调用上下文管理器对象的__exit__()方法，并将异常类型、值及tracebac信息作为参数传递给__exit__()方法。如果__exit__()返回值为false，则异常会被重新抛出；如果其返回值为true，异常被挂起，程序继续执行。
> ##上下文管理器对象
>> 定义程序运行时需要建立的上下文，处理程序的进入和退出，实现了上下文管理协议，即在对象中定义__enter__()和__exit__()方法。
>>> __enter__():进入运行时的上下文，返回运行时上下文相关的对象，with语句将这个返回值绑定到目标对象。
>>> __exit__():退出运行时上下文相关的对象，定义在块执行（或终止）之后上下文管理器应该做什么。
# 23.使用else子句简化循环（异常处理）
# 24.遵循异常处理的几点基本原则
# 25.避免finally可能发生的陷阱
> ## 异常屏蔽
>> 当try块中发生异常的时候，如果在except块匹配不到对应的异常，异常将会被临时保存起来，当finaly执行完毕的时候，临时保存的异常将会再次被抛出，但如果**finally语句中产生了新的异常或者执行了return或break语句，那么临时保存的异常将会被丢失，从而导致异常屏蔽**。
# 26.深入理解None,正确判断对象是否为空
> ##Python中以下数据会当做空处理
>> 1.常量None
>> 2.常量False
>> 3.数值类型为零,空序列，空字典
>> 4.自定义类中实现了nonzreo()方法和len()方法，并且该方法返回整数0或者布尔值False的时候。
# 27.连接字符串应优先使用join而不是+
# 28.格式化字符串时尽量使用.format方式而不是%
# 29.区别对待可变对象和不可变对象
# 30.[],()和{}：一致的容器初始化形式
# 31.记住函数传参既不是传值也不是传引用
> Python函数参数既不是传值也不是传引用，应该是传对象或者说传对象的引用。函数参数在传递的过程中将整个对象传入，对可变对象的修改在函数外部以及内部都可见，调用者和被调用者之间共享这个对象；而对于不可变对象，由于并不能真正被修改，因此，修改往往是通过生成一个新对象然后肤质来实现。
# 32.警惕默认参数潜在的问题
> def在Python中是一个可执行的语句，当解释器执行def的时候，默认参数也会被计算，并存在函数的.func_default属性中。由于Python中函数参数传递的是对象，可变对象在调用者和被调用者之间共享。
>
> 避免默认参数所指向的对象在所有的函数调用中被共享，而是在函数调用的过程中动态生成，可以在定义的时候使用None对象作为占位符。
# 33.慎用变长参数\*args和\**kwargs
# 34.深入理解str()和repr()的区别
> 1.str()主要面向用户，其目的是可读性，返回形式为用户友好性和可读性较强的字符串类型；repr()主要面向的是Python解释器，或者说是开发人员，其目的是准确性，其返回值表示Python解释器内部的含义。
>
> 2.解释器中直接输入a默认调用repr()函数，print a则调用str()函数。
>
> 3.repr()的返回值一般可以用eval()函数还原对象，通常存在等式：obj=eval(repr(obj)),若用户重新实现repr()，则等式可能不成立。
>
> 4.一般来说类中都应该定义__repr__()方法，而__str__()方法则为可选。
# 35.分清staticmethod和传classmethod的适用场景
# 36.掌握字符串的基本用法
# 37.按需选择sort()或者sorted()
> **sorted(iterabel[,cmp[,key[,reverse]]]) 作用于任何可迭代的对象
>
> s.sort([cmp[,key[,reverse]]]) 一般作用于列表，内存消耗少，效率高
> 传入参数key比传入参数cmp效率要高。cmp传入的函数在整个排序过程中会调用多次，函数开销较大；而key针对每个元素仅做一次处理。
# 38.使用copy模块深拷贝对象
> **浅拷贝**:构造一个新的复合对象并将从原对象中发现的引用插入该对象中。
>
> **深拷贝**:构造一个新的复合对象，遇到引用会继续递归拷贝其所指向的具体内容，因此产生的对象不受其他引用对象操作的影响。
# 39.使用Counter进行技术统计
# 40.深入掌握ConfigParser
# 41.使用argparse处理命令行参数
# 42.使用pandas处理大型CSV文件
# 43.一般情况下使用ElementTree解析XML
# 44.理解模块pickle优劣
# 45.序列化的另一个不错的选择-Json
# 46.使用traceback获取栈信息
# 47.使用logging记录日志信息
# 48.使用threading模块编写多线程程序
# 49.使用Queue使多线程变得安全
# 50.利用模块实现单例模式
# 51.用mxin模式让程序更加灵活
> Python每个类都有一个**\_\_base__**属性，它是一个用来存放所有基类的元组。Python中的基类在运行中可以动态改变。向其中增加新的基类中，这个类就拥有了新的方法，也就是所谓是混入(mixin)。这种动态性的好处在于代码获得了更丰富的拓展功能。**Python反射技术**
# 52.用发布订阅模式实现松耦合
# 53.用状态模式美化代码
# 54.理解built-in objects
> - Python中一切皆对象，内建类型也是对象；用户定义的类型是对象，object是对象，type也是对象。在新式类中，object是所有内建类型的基类，用户所定义的类可以继承自object也可继承自内建类型。
>
> - object和古典类没有基类，type的基类是object。
>
> - 新式类中type()的值和__class__的值是一样的，但古典类中实例的type为instance，其type()的值和__class__的值不一样。
>
> - 继承自内建类型的用户类对象实例也是object的实例，object是type的实例，type实际上是个元类。
>
> - object和内建类型以及所有基于type构建的用户类都是type的实例。
>
> - 在古典类中，所有用户定义的类的类型都为instance。
>
> ## 古典类与新式类的区别
>
> 不能简单地从定义的形式上来判断一个类是新式类还是古典类，而应当通过元类的类型来确定来确定类的类型：古典类的元类为types.ClassType,新式类的元类为type类。
# 55.\_\_init__()不是构造方法
> ## \_\_new__()与\_\_init__()的区别
>> 1.\_\_new__()是静态方法，而\_\_init__()为实例方法。
>>
>> 2.\_\_new__()方法一般需要返回类的对象，当返回类的对象时将会自动调用\_\_init__()方法进行初始化，如果没有对象返回，\_\_init__()方法不会被调用。\_\_init__()方法不需要显示返回，默认为None，否则会运行时抛出TypeError。
>>
>> 3.\_\_new__控制类的创建，\_\_init__()控制类的初始化。
>>
>> 4.一般情况下不需要覆盖__new__()方法，但当子类继承自不可变类型往往需要覆盖该方法。
>>
>> 5.当需要覆盖__new__()和__init__()方法的时候这两个方法的参数保持一致，如果不一致将导致异常。