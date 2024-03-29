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
# 56.理解名字查找机制
> **Python中的作用域分为局部作用域、全局作用域、嵌套作用域和内置作用域。**
>
> LEGB法则：局部作用域、嵌套作用域、全局作用域、内置作用域
>
> Python中名字查找机制如下:
>> 1.在最内范围内查找，即在locals()里面查找。
>>
>> 2.在模块内查找，即在globals()里面查找。
>>
>> 3.在外层查找，即在内置模块中查找。
# 57.为什么需要self参数
# 58.理解MRO与多继承
> ## 古典类和新式类之间所采取的MRO的实现存在差异
>> 古典类中，MRO搜索采用简单的自左向右的深度优先方法，即按照多继承申明的顺序形成树继承结构，自顶向下采用深度优先的搜索顺序。
>>
>> 新式类采用的是**C3 MRO**搜索方法,算法描述如下
>>> 1.C1C2...CN表示类C1到CN的序列，其中序列头部元素(head)=C1,序列尾部(tail)定义为=C2...CN
>>>
>>> 2.C继承的基类自左向右分别表示为B1,B2,...,BN;
>>>
>>> 3.L[C]表示C的线性继承关系，其中L[object]=object。
>>>> L[C(B1...BN)]=C+merge(L(B1)...L(BN),B1...BN)
>>>> 在L[B1]...L[BN],B1...BN中，取L[B1]的head，如果该元素不在L[B2]...L[BN],B1...BN的尾部序列中，则添加该元素到C的线性继承序列中，同时将该元素在所有列表中删除(该头元素也叫good head),否则取L[B2]的head.继续相同的判断，直到整个列表为空或者没有办法找到任何符合要求的头元素(此时将抛出一个异常)。
>
> **菱形继承十载多重继承机制中应该尽量避免的一个问题。**
# 59.理解描述符机制
> 默认对属性的访问控制是从对象的字典里面(\_\_dict__)中获取(get), 设置(set)和删除(delete)它。举例来说， a.x 的查找顺序是, a.\_\_dict__['x'] , 然后 type(a).\_\_dict__['x'] , 然后找 type(a) 的父类(不包括元类(metaclass)).如果查找到的值是一个描述器, Python就会调用描述器的方法来重写默认的控制行为。这个重写发生在这个查找环节的哪里取决于定义了哪个描述器方法。注意, 只有在新式类中时描述器才会起作用。(新式类是继承自 type 或者 object 的类)
>
> 描述符协议
>>
>> descr.\_\_get__(self, obj, type=None) --> value
>>
>>descr.\_\_set__(self, obj, value) --> None
>>
>>descr.\_\_delete__(self, obj) --> None
>>
>> 资料描述符：同时定义了__get__()和__set__()的对象。
>>
>> 非资料描述器：定义了__get__() 的描述器。
>>
>> 资料描述器和非资料描述器的区别在于：相对于类对象实例的字典的优先级。如果实例字典中有与描述器同名的属性，如果描述器是资料描述器，优先使用资料描述器;如果是非资料描述器，优先使用字典中的属性。
>>
> 描述器的调用
>> 调用的细节取决于 obj 是一个类还是一个实例。另外，描述器只对于新式对象和新式类才起作用。继承于 object 的类叫做新式类。
>>
>>对于对象来讲，方法 object.\_\_getattribute__() 把 b.x 变成 type(b).\_\_dict__['x'].\_\_get__(b, type(b)) 。具体实现是依据这样的优先顺序：资料描述器优先于实例变量，实例变量优先于非资料描述器，\_\_getattr__()方法(如果对象中包含的话)具有最低的优先级。
>>
>> 对于类来讲，方法 type.\_\_getattribute__() 把 B.x 变成 B.\_\_dict__['x'].__get__(None, B) 。
>>
>> 总结:
>>> * 描述器的调用是因为 __getattribute__()
>>> * 重写 __getattribute__() 方法会阻止正常的描述器调用
>>> * \_\_getattribute__() 只对新式类的实例可用
>>> * object.\_\_getattribute__() 和type.\_\_getattribute__()对__get__() 的调用不一样。
>>> * 资料描述器总是比实例字典优先。
>>> * 非资料描述器可能被实例字典重写。(非资料描述器不如实例字典优先)
>>
>> super()返回的对象同样有一个定制的__getattribute__() 方法用来调用描述器。调用 super(B, obj).m() 时会先在obj.\_\_class__.\_\_mro__ 中查找与B紧邻的基类A，然后返回 A.\_\_dict__['m'].\_\_get__(obj, A) 。如果不是描述器，原样返回 m 。如果实例字典中找不到 m ，会回溯继续调用object.\_\_getattribute__() 查找。(译者注：即在__mro__中的下一个基类中查找)
# 60.区别__getattr__()和__getattribute__()方法
>> 1.\_\_getattr__()适用于未定义的属性，即该属性在实例中以及对应的类的基类以及祖先类中都不存在，**\_\_getattribute\_\_()对于所有属性的访问都会调用该方法，但是__getattribute__()仅应用于新式类**。
>>
>> 2.当访问一个不存在的实例属性的时候就会抛出AttributeError异常。这个异常是由内部方法__getattribute__(self,name)抛出的，因为__getattibute__()会被无条件调用，只要是涉及到实例属性的访问就会调用该方法，它要么返回值，要么抛出异常。
>>
>> 3.\_\_getattr__()方法仅在以下情况下会被调用:
>>> * 属性不在实例对象的__dict__中
>>> * 属性不在其基类以及祖先类的__dict__中
>>> * 触发Attribute异常时(\_\_getattribute__()方法或者property中定义的get()方法引发的异常)
>>
>> 4.当两个方法同时被定义的是定义的时候，\_\_getattr__()方法要么在__getattribute__()方法中显示被调用，要么触发AttributeError异常，否则__getattr__()永远不会被调用。
>>
>> 5.\_\_getattribute__()及__getattr__()方法都是object类中定义的默认方法，覆盖这些方法时要注意
>>> 1.避免无穷递归
>>>> ``` python
>>>> def __getattribute__(self,attr):
>>>>     try:
>>>> #        return self.__dict__[attr] # 调用__getattribute__(self,attr)，产生无穷递归
>>>>          return super(A,self).__getattribute__(attr) #return object.__getattribute__(self,attr)
>>>>     except KeyError:
>>>>          return 'default'
>>>> ```
>>> 2.访问未定义的属性
>>>
>>> 3.覆盖了__getattribute__()方法之后，任何属性的访问都会调用用户定义的__getattribute__()方法，性能上会有所损耗，比使用默认的方法要慢。
>>>
>>> 4.覆盖的__getattr__()方法如果支持动态处理事先未定义的属性，可以更好地实现数据隐藏。
# 61.使用更为安全的property
> **property是用来实现属性可管理性的built-in数据类型，其实质是一种特殊的数据描述符。它和普通描述符的区别在于：普通描述符提供的一种较为低级的控制属性访问的机制，而property是它的高级应用**。
>> 数据描述符:同时定义了__get__()和__set__()方法的类对象。
>>
>> 非数据描述符:仅定义了__get__()方法的类对象。
>property的优势：
>> 1.代码更简洁，可读性更强。
>>
>> 2.更好的管理属性的访问。创建一个property实际上就是将其属性的访问与特定的函数关联起来，相当于标准属性的访问。
>>
>> 3.代码的可维护性更好
>>
>> 4.控制属性访问权限，提高数据安全性。
# 62.掌握metaclass
> 元类
>> 1.元类是关于类的类，是类的模板
>>
>> 2.元类是用来控制如何创建类的，正如类是创建对象的模板一样。
>>
>> 3.元类的实例为类，正如类的实例为对象。
>>
> type通过 type(类名,父类的元组(可为空),包含属性的字典(名称和值)) 此类语法创建类对象,所创建的对象的__class__属性为type。type实际上是Python的一个內建元类，用来直接指导类的生成。
> 新式类中当一个类未设置__metaclass__属性的时候，它将使用默认的type元类生成类。而当该属性被设置时查找规则如下：
>> 1) 如果类对象的dict['__metaclass__'],则使用对应的值来构建类；否则使用其父类dict['__metaclass__']中所指定的元类来构建类，当父类中也不存在指定的metaclass的情形下使用默认元类type。
>>
>> 2) 对于古典类，条件1不满足的情况下，如果存在全局变量__metaclass__,则使用该变量所对应的元类来构建类；否则使用types.ClassType。
>
> **元类中所定义的方法为其所创建的类的类方法，并不属于该类的对象。**
>
> **元类用来指导类的生成，元方法可以从元类或者类中调用，不能从类的实例中调用，而类方法可以从类中调用也可以从类的实例中调用。**
> 类对象同时继承自元类C1和C2的时候会抛出异常，这是因为Python解释器并不知道C1和C2是否兼容，因此会发生冲突警告。解决的办法是重新定义一个派生自M1和M2的元类，并在C3中将其__metaclass__属性设置为该派生类。
>> ``` python
>>class M1(type):
>>
>>    def __new__(meta, name, bases, atts):
>>
>>        print 'M1 called for ' + name
>>        return super(M1, meta).__new__(meta, name, bases, atts)
>>
>>
>>class C1(object):
>>    __metaclass__ = M1
>>
>>
>>class SubC1(C1):
>>    pass
>>
>>
>>class M2(type):
>>    def __new__(meta, name, bases, atts):
>>        print 'M2 called for ' + name
>>        return super(M2, meta).__new__(meta, name, bases, atts)
>>
>>
>>class C2(object):
>>    __metaclass__ = M2
>>
>># metaclass conflict
>># class SubC(C1, C2):
>>#     pass
>>
>>class M3(M2, M1):
>>    def __new__(meta, name, bases, atts):
>>        print 'M3 called for ' + name
>>        return super(M3, meta).__new__(meta, name, bases, atts)
>>
>>
>>class C3(C1, C2):
>>    __metaclass__ = M3
>>
>> ```
# 63.熟悉Python对象协议
> 1.用以比较大小的协议：\_\_cmp__()
>
> 2.数值类型相关的协议
>
> 3.容器相关的协议
>
> 4.可调用对象的协议，\_\_call__()
>
> 5.哈希对象协议，\_\_hash__()
>
> 6.上下文协议，\_\_enter__()和\_\_exit__()

# 64.利用操作符重载实现中缀语法
# 65.熟悉Python的迭代器协议
> 迭代器(一个带状态的对象，在调用next()方法的时候返回容器中的下一个值，任何实现了__iter__和__next__()（python2中实现next()）方法的对象都是迭代器)。
>
>> iter()函数返回一个迭代器对象，接收的参数是一个实现了__iter__()方法的容器或者迭代器(支持仅有__getitem__()方法的容器)。对于容器而言，\_\_iter__()方法返回一个迭代器对象；而对于迭代器对象而言，它的__iter__()方法返回其自身。
>
> 迭代器协议
>
>> 1) 实现__iter__()方法，返回一个迭代器。**实现此方法的对象为可迭代对象。
>> 2) 实现next()方法，返回当前的元素，并指向下一个元素的位置，如果当前位置已无元素，则抛出StopIteration异常。Python2中实现此协议的对象即为迭代器。
>
> **可迭代的类中，一般实现以下两个方法，\_\_iter__()以及__next()__方法，\_\_iter__()方法返回self。**
# 66.熟悉Python生成器
> 生成器其实就是一种特殊的迭代器。它使一种更为高级、更为优雅的迭代器。使用生成器让我们可以以一种更加简洁的语法来定义迭代器。
>> 1.任意生成器都是迭代器（反过来不成立）
>>
>> 2.任意生成器，都是一个可以延迟创建值的工厂
>
> 在Python中两种类型的生成器：生成器函数以及生成器表达式。生成器函数就是包含yield参数的函数。生成器表达式与列表解析式类似。
>>
>> 当调用生成器函数时，它返回一个迭代器对象，不过这个迭代器是以生成器对象的形式出现的。
>>
>> 每一个生成器函数调用之后，它的函数体并不执行，而是第一次调用next()的时候才执行。当第一次调用next()方法时，生成器函数开始执行，执行到yield表达式为止。
>>
>> send()是全功能版的next(arg),或者说next()是send(arg)的快捷方式，相当于send(None)。send(arg)可以控制返回值，使得yield表达式的返回值就是它的实参。
>
> 生成器的用处
>> 1.实现with语句的上下文管理器协议。利用的是调用生成器函数时函数体并不执行，当第一次调用next()方法是才开始执行，并执行到yield表示是后中止，直到下一次调用next()方法这个特性。
>>
>> ```python
>>from contextlib import contextmanager
>>@contextmanager
>>def tag(name):
>>    print "<%s>" % name
>>    yield
>>    print "<%s>" % name
>>
>>with tag('h1'):
>>    print 'foo'
>> ```
>>
>> 2.实现协程
# 67.基于生成器的协程及greenlet
> 协程，又称微线程和纤程。协程往往实现在语言的运行时或虚拟机中，操作系统对其存在一无所知，所以又被称为用户空间线程或绿色线程。大部分的协程的实现是协作式而非抢占式，需要用户自己去调度，所以通常无法利用多核，但用来执行协作式多任务非常合适。
# 68.理解GIL(全局解释锁)的局限性
# 69.对象的管理与垃圾回收
> **Python内存管理方式：引用计数器**,即针对每一个对象维护一个引用计数值来表示该对象当前有多少个引用。该对象被引用则引用值+1，该对象的引用被删除则引用值-1。只有当引用计数值为0的时候该对象才会被垃圾收集器回收。引用计数算法最明显的缺点是无法解决**循环引用问题**，及两个对象互相引用，从而导致内存泄漏。
>
>> Python自带一个gc模块，用来跟踪对象的"入引用"和"出引用",并找出复杂数据结构之间的循环引用，同时回收内存垃圾。有两种方式触发垃圾回收：显示调用gc.collect()进行垃圾回收；创建新对象为其分配内存的时候，判断是否超过threshold阈值，超过自动进行垃圾回收。
# 84.掌握循环优化的基本技巧
> 1)减少循环内部的计算。
> 2)将显示循环变为隐式循环，可能会牺牲代码的可读性。
> 3)在循环中尽量引用局部变量。局部变量的查询比全局变量要快。
> 4)关注内部嵌套循环。在多层嵌套循环中，尽量将内层循环的计算往上层移。
