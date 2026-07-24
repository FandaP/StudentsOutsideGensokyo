# -*- coding: utf-8 -*-
# @title StudentsOutsideGensokyo
# @author FandaP
# 虽然FandaP是代码的编写者与剧情的构造者，但这里的故事是所有初中车万众学习交流群的同学们一起创造的！
# 角色图片：角色名 服装 面部表情 动作 [附加表情] [状态]
# 背景图片：bg 大地点 中地点 [小地点] [状态] 


define I = Character(name="[myName]",color="#aaa")
define FandaP = Character(name="阿P",color="#00f",image="FandaP")
define CirNo = Character(name="琪露锘",color="#68f")
define Shinden = Character(name="Shinden")
define chuge = Character(name="chuge",color="#fff")
define zectbumokhfs = Character(name="zectbumokhfs",color="#383")
define Mom = Character(name="妈妈",image="myMom")
default THCharas = [
    "博丽灵梦", "雾雨魔理沙", "神玉", "魅魔", "菊理", "矜羯罗", 
    "幽幻魔眼", "依莉斯", "萨丽爱尔", "玄爷", "里香", "明罗", 
    "爱莲", "小兔姬", "卡娜·安娜贝拉尔", "朝仓理香子", "北白河千百合", 
    "冈崎梦美", "咪咪号", "留琴", "玛○奇", "苏格拉底", "奥莲姬", 
    "胡桃", "艾丽", "幽香", "梦月", "幻月", "萨拉", "露易兹", 
    "爱丽丝", "雪", "舞", "梦子", "神绮", "露米娅", "大妖精", 
    "琪露诺", "红美铃", "小恶魔", "帕秋莉·诺蕾姬", "十六夜咲夜", 
    "蕾米莉亚·斯卡蕾特", "芙兰朵露·斯卡蕾特", "冴月麟", "蕾蒂·霍瓦特洛克", 
    "橙", "爱丽丝·玛格特洛依德", "莉莉霍瓦特", "露娜萨·普莉兹姆利巴", 
    "梅露兰·普莉兹姆利巴", "莉莉卡·普莉兹姆利巴", "魂魄妖梦", 
    "西行寺幽幽子", "八云蓝", "八云紫", "魂魄妖忌", "蕾拉·普莉兹姆利巴", 
    "伊吹萃香", "莉格露·奈特巴格", "米斯蒂娅·萝蕾拉", "上白泽慧音", 
    "因幡天为", "铃仙·优昙华院·因幡", "八意永琳", "蓬莱山辉夜", 
    "藤原妹红", "梅蒂欣·梅兰可莉", "风见幽香", "小野塚小町", 
    "四季映姬·夜摩仙那度", "秋静叶", "秋穰子", "键山雏", "河城荷取", 
    "犬走椛", "东风谷早苗", "八坂神奈子", "洩矢诹访子", "永江衣玖", 
    "比那名居天子", "大鲶鱼", "琪斯美", "黑谷山女", "水桥帕露西", 
    "星熊勇仪", "古明地觉", "火焰猫燐", "灵乌路空", "古明地恋", 
    "娜兹玲", "多多良小伞", "云居一轮","云山", "村纱水蜜", "寅丸星", 
    "圣白莲", "封兽鵺", "姬海棠果", "幽谷响子", "宫古芳香", "霍青娥", 
    "苏我屠自古", "物部布都", "丰聪耳神子", "二岩猯藏", "秦心", 
    "若鹭姬", "赤蛮奇", "今泉影狼", "九十九弁弁", "九十九八桥", 
    "鬼人正邪", "少名针妙丸", "堀川雷鼓", "宇佐见堇子", "清兰", 
    "铃瑚", "哆来咪·苏伊特", "稀神探女", "克劳恩皮丝", "纯狐", 
    "赫卡提亚·拉碧斯拉祖利", "依神女苑", "依神紫苑", "爱塔妮缇拉尔瓦", 
    "坂田合欢", "高丽野阿吽", "矢田寺成美", "尔子田里乃", "丁礼田舞", 
    "摩多罗隐岐奈", "戎璎花", "牛崎润美", "庭渡久侘歌", "吉吊八千慧", 
    "杖刀偶磨弓", "埴安神袿姬", "骊驹早鬼", "饕餮尤魔", "豪德寺三花", 
    "山城高岭", "驹草山如", "玉造魅须丸", "菅牧典", "饭纲丸龙", 
    "天弓千亦", "姬虫百百世", "孙美天", "三头慧之子", "天火人血枪", 
    "豫母都日狭美", "日白残无", "尘塚姥芽", "封兽魑魅", "道神驯子", 
    "维缦·浅间", "磐永阿梨夜", "渡里贝子", "射命丸文", "森近霖之助", 
    "无名的读书妖怪", "桑尼米尔克", "露娜切露德", "斯塔萨菲雅", 
    "绵月丰姬", "绵月依姬", "Reisen", "嫦娥", "稗田阿求", "茨木华扇", 
    "本居小铃", "宫出口瑞灵", "奥野田美宵","宇佐见莲子","玛艾露贝莉·赫恩","梅丽"
]
default GameCharas = ["FandaP","阿P","琪露锘","zectbumokhfs","古神","鱼干","chuge","憧憬成为囚鸟少女","Shinden","人形废物"]

label start:
    $ myName = "？？？"
    "游戏名：幻想乡外面的同学们\n作者  ：FandaP"
    "本游戏的剧情实际上是对“初中车万众学习交流群”的同学们的neta创作，本质以娱乐为主。与现实世界中的其他人员并无特殊关联。若您发现了部分剧情可能与您或您身边的人有关，纯属巧合。"
    "本作虽然会出现少量的东方Project要素，但本游戏并非东方Project的二次同人创作。请在讨论时注意。"
    "若您对诸如性别淡化，以及未成年人之间的友谊等要素感到不适，请退出此游戏。"
    menu:
        "那么，你现在要进入游戏吗？"
        "开始游戏":
            "那么，游戏开始了。"
            window hide
            jump main0
        "我无法接受本游戏的要素，退出":
            $ renpy.quit()
        
label main0:
    window show
    "我曾经有一段别样的经历。"
    "也是我和外面世界的朋友们之间发生的事情。"
    "故事还得从我三个月前来到外面世界说起。"
    with fade
    "2026年5月10日，在一处让我非常陌生的地方。"
    I "好痛……"
    I "我这是在哪……"
    scene bg outside street night
    $ myName = "我"
    "夜晚的街头，路灯正在闪烁着。"
    "这里除了我，貌似一个人也没有。"
    I "我是……谁来着？"
    "一阵强劲的音乐传来。"
    I "好熟悉……虽然没听过但总觉得好熟悉……"
    "音乐声越来越大。"
    # 黑影阿P从屏幕右边出现并移到中间
    show FandaP uniform none normal inshadow with moveinright
    "一个年龄和我相仿的男孩向我走来，他的手中紧握着一个方形的盒子。"
    menu:
        I "这里好像也没别人了，只能求助于他了……"
        "……你好？":
            jump main1a
        "……":
            jump main1b

label main1a:
    I "……你好？"
    # 阿P身着校服，身影亮了起来
    show FandaP uniform happy normal with dissolve
    FandaP "嗯嗯，什么事情？"
    I "就是说，你放的那首歌，是……"
    FandaP "是“东方Project”的曲子啦。"
    menu:
        "东方Project？":
            pass
    I "东方Project？"
    FandaP "东方Project可是一个游戏漫画小说动画集合在一起的世界观，大概就是一群人类和妖怪在幻想乡瞎闹的故事。"
    "听到幻想乡这个地名，我的记忆突然涌上来。"
    "我的思绪飘到了很久以前……"
    jump main2

label main1b:
    # 身着校服的阿P疑惑地看着我
    show FandaP uniform doubtful normal with dissolve
    I "……？"
    "那个男孩打量了我一眼，随后开口说道："
    FandaP "今天……是有什么展会吗？"
    I "展会？什么是展会？"
    FandaP "你穿成这个样子，很明显是有ACGN展吧……哦，不好意思，我平时不喜欢说“漫展”这个词。"
    I "但是……我平时就穿的这个衣服啊。"
    FandaP "啊？！"
    pause 0.5
    extend "\n你平时怎么可能穿这个？魔怔了？"
    "低头看看妈妈亲手给我做的衣服，我的记忆突然涌上来。"
    "我的思绪飘到了很久以前……"
    jump main2

label main2:
    scene bg gensokyo humanvillage night
    "2012年1月，我出生于人类村落里。"
    "从小，我的父母就和我讲述幻想乡的故事。"
    # scene 我家
    scene bg gensokyo humanvillage myhome night
    # 我妈开心地笑
    show mymom normal happy reading 
    with dissolve
    Mom "数百年前，妖怪们为了保留自己的栖息地，建立了结界。"
    Mom "结节将幻想乡与外界隔离开来，这里成为了妖怪最后的乐园。"
    I "那……人类呢？人类在幻想乡里安全吗？"
    Mom "只要遵守规则，不随意闯入妖怪的领地，人类村落是受到保护的。"
    Mom "毕竟，博丽巫女会维持着人与妖怪之间的平衡。"
    I "博丽巫女……听起来好厉害的样子。"
    Mom "是啊，她是幻想乡的守护者，也是解决异变的关键。"
    I "那这样，人类的生存就有保障了。"
    I "……对吧？"
    # 我妈严肃
    show mymom normal serious none with dissolve
    Mom "你应该不会去招惹外面的妖怪吧？"
    I "肯定不会的！我保证！"
    # 我妈又开心了
    show mymom normal happy reading with dissolve
    Mom "嗯，那就好~"
    scene black with dissolve
    "这就是我的故事。"
    jump main3

label main3:
    # scene 夜晚的街头
    scene bg outside street night
    "记忆的潮水退去，我回到了现实的街头。"
    # 阿P的身影再次出现在屏幕中央
    show FandaP uniform doubtful normal
    FandaP "——喂，说话啊！"
    I "哦哦，那个……"
    I "我是从幻想乡来的，我叫……"
    # 阿P震惊
    show FandaP uniform shock normal with hpunch
    FandaP "你说什么？！" 
    pause 0.5
    extend "你是从幻想乡来的？！"
    I "呃……怎么了？"
    FandaP "你不说你不知道东方Project吗？"
    I "幻想乡的人类村落啊……还有，什么东方西方的？"
    with hpunch
    FandaP "你……真的不知道东方Project？"
    I "你别管这个了……这是什么地方，怎么这么多这么怪异的建筑？"
    FandaP "这不就普通的高楼吗……小康社会都全面实现了，怎么还有人连高楼都没见过……"
    # 阿P疑惑
    show FandaP uniform doubtful normal questionmark with dissolve
    FandaP "不对啊，你都知道幻想乡了，怎么还没见过高楼大厦，刷手机也没见到过吗？"
    I "？？？手机？"
    I "手机是啥？"
    with hpunch 
    pause 2
    # 阿P流汗
    show FandaP uniform smile normal sweat with dissolve
    FandaP "……" 
    pause 1
    extend "\n你真是幻想乡来的？"
    I "对啊，怎么了？"
    FandaP "……你叫什么，我带你熟悉一下外面世界"
    I "哦对对，我刚刚要说名字来着，我的名字叫……"

label main4:
    # 阿P闭眼笑
    show FandaP uniform laugh normal with dissolve
    $ myName = renpy.input("我的名字叫").strip()
    if myName in THCharas:
        "我" "我的名字叫[myName]"
        FandaP "别开玩笑啦，你怎么可能是[myName]，你到底叫什么？"
        jump main4
    elif myName in GameCharas:
        "我" "我的名字叫[myName]"
        FandaP "虽然我知道你很想起这个名字，但是这是这个游戏的剧情角色，所以你只换一个名字啦~"
        jump main4
    else:
        if not myName:
            # 阿P震惊
            show FandaP uniform shock normal with hpunch
            FandaP "你的名字是棍母？！"
            jump main5
        FandaP "[myName]，真是个奇怪的名字，不过细想也是个好名字。"

    FandaP "哦对了，我的名字叫FandaP。当然，他们都叫我阿P。\n你就叫我阿P就行了。"
    FandaP "要不要去我家玩，我家还蛮大的。欢迎你来我家玩，玩累了就直接睡觉，没问题的！"
    I "呃……我觉得……"
    FandaP "走啦走啦（推）"
    menu:
        "前往FandaP的家":
            I "怎么感觉不太对劲呢……"
        "等下，我为什么要和你走？":
            I "等下，我为什么要和你走？"
            FandaP "反正不会把你怎么样的。走啦~"
            I "那也不对啊，我凭啥信你？"
            FandaP "你现在面临着十分复杂的情况，我必须给你讲解清楚。"
            I "那你在这儿讲不得了，上你家干嘛？"
            FandaP "你不嫌热吗？"
            "诚然，这里热的不行。\n想了想，我还是跟着阿P走了"
            FandaP "你快走吧，已经晚上十一点半了"
    hide FandaP
    "就这样，我们前往了阿P的家。"
    # scene 阿P家起居室
    scene bg outside phome livingr
    # 阿P出现
    show FandaP uniform smile normal with hpunch
    FandaP "你等会，我马上就回来了，你在这坐会儿先啦。"
    # 阿P消失
    hide FandaP
    I "没想到果然还是来了啊……"
    I "话说，我来之前是怎么回事来着？"
    "记忆，又开始涌来。"
    jump main5

label main5:
    # scene 博丽大结界
    scene bg gensokyo shirine 
    "5月10日，博丽神社。"
    "我只是去神社四周逛逛，没想到却遇到了两个行踪诡异的人。"
    # 琪露锘 出现于画面左部
    show CirNo at left
    CirNo "我们现在，貌似是出不去了啊……"
    show zectbumokhfs at right
    zectbumokhfs "没事的，我还有两枚核弹，把大结界炸了就好了。"
    CirNo "我去这么聪明<('o')>"
    "此时，我想到妈妈和我说过的，"
    # scene 我家
    scene bg gensokyo humanvillage myhome night
    show mymom normal serious none
    Mom "博丽大结界是幻想乡最重要的东西。如果结界没了，幻想乡将不复存在。"
    # scene 博丽大结界
    scene bg gensokyo shirine
    "为此，我要上去阻止他们。我不想要这么美好的幻想乡被破坏。"
    # 琪露锘、古神 出现于画面左部、右部
    show CirNo at left
    show zectbumokhfs at right

    I "你们，要干什么！" 
    with hpunch
    CirNo "呃，你谁啊？"
    zectbumokhfs "一个杂鱼，和大结界一起炸了就好了。"
    with hpunch
    
    I "（察觉到不对）等等，你说啥？"
    CirNo "反正，炸死了也没人管。"
    zectbumokhfs "（丢出核弹）"
    I "你们干什么，不许……"
    # 琪露诺 古神分别从画面左右溜了出去
    hide CirNo with moveinright
    hide zectbumokhfs with moveinleft
    
    # 核弹爆炸
    scene white with dissolve
    pause 4
    scene black with dissolve
    
    I "。……？"
    CirNo "怎么没炸开啊，古神你行不行啊？" # Another Views
    zectbumokhfs "卧槽这大结界怎么这么坚固，算了我去找点反物质去。"
    I "（意识逐渐模糊）你们。。怎么能炸大结界。。。"
    extend "\n饿啊！（彻底失去意识）"
    
    "好像是个不咋光彩的牺牲……"
    jump main6


label main6:
    scene bg outside phome livingr
    "思索间，浴室传来了哗啦啦的流水声。"
    I "这不是五楼吗，哪来的水声？"
    "当时的我貌似并不知道外乡的现代科技已经可以用水泵把水送到几十层的高度了，更别说五楼。\n不知其所以然的我站起来走向了水声来源的方向。"
    scene bg outside phome bathro with moveinright
    "浴室里" "（水声）"
    I "阿P，你在里面吗？"
    FandaP "啊拉，干什么啊？\n你先回去坐着呗，我等会就来了。"
    I "你在里面干什么啊，这五楼怎么会有水声啊？"
    FandaP "欸，五楼有水声……\n你现在先坐回去啦，我等会再告诉你为什么有水声，行吧？"
    I "你还没回答呢，你在里面干什么呢？"
    "然而，回答我的却是持久的沉默。"
    FandaP "（关掉水龙头）"
    "随后，连水声都消失了。"  
    "面对阿P如此沉默的回应，你打算？"
    menu :
        "还是听阿P的话，回去坐着吧。":
            jump main7b
        "阿P这是在洗澡？哇多么好的机会啊":
            jump main7a


label main7a:
    "你打开了浴室门。"
    # scene 浴室里面
    scene bg outside phome bathri with dissolve
    # 阿P身着浴衣，伴之以轻蔑的目光
    show FandaP bathrobe contemptuous normal sweat
    "然而，阿P却以一种奇怪的眼神打量着你。"
    I "呃，阿P你是在洗澡吗？不好意思我先出……"
    "这时候，阿P却开口说话了。"
    FandaP "哇啊啊，真是变态呢。"
    pause 0.5
    show FandaP bathrobe smile normal angry
    FandaP "你个死变态！这才哪到哪啊，你就想看隐藏CG？"
    FandaP "我说，[myName]你是不是有点太恶心了点？"
    # 阿P 浴衣带血 微笑 生气
    show FandaP bathrobe laugh holdknife none with vpunch
    "说着，一把刀插进了我的心脏。"
    I "不是姐，你去干那个控制我的人啊，关我什么事？"
    # 阿P 浴衣带血 微笑 流汗
    show FandaP bathrobe smile holdknife sweat
    FandaP "……我会给TA惩罚的。"
    "我绝望地闭上了眼睛。"
    scene black with easeintop
    "但是，想象中的疼痛与死亡并没有出现。"
    "反而是阿P的笑声突兀地出现了。"
    scene bg outside phome bathri with easeinbottom
    show FandaP bathrobe laugh normal none with dissolve
    FandaP "噗嗤，哈哈哈哈哈哈哈，你——哈哈哈哈哈哈哈——"
    I "额，我……"
    "我低头看了看身上，一道伤口也没有。"
    "而阿P的手中，是一把塑料制的匕首。"
    I "搞什么嘛……"
    show FandaP bathrobe contemptuous holdknife angry with zoomin
    FandaP "幸亏你不知道我在洗澡，否则这可是一把真正的匕首了。"
    show FandaP bathrobe laugh normal none with zoomout
    FandaP "这怎么可能呢，持有管制刀具可是违法的。。。"
    "阿P走出了浴室。"


label main7b:
    I "诶，不理我吗？"
    I "你这样我可要回去了。"
    "就在我准备回去的时候，阿P突然说话了。"
    FandaP "你等会儿，我马上出来了。"
    show FandaP bathrobe smile normal with dissolve
    "阿P裹着浴袍，从中走了出来。"
    I "所以，你到底在干什么啊。"
    FandaP "在洗澡啦，怎么？"
    I "原来如此……"
    FandaP "本来想着，像你这个年龄的人，多少会闯进去的。"
    FandaP "如果你是一个偷窥狂的话，那你可不能活着离开了。"
    # if peekTimes:
    #     scene black
    #     show FandaP bathrobe smile holdknife with dissolve
    #     FandaP "还是说你本来就是呢？"
    scene bg outside phome livingr 
    show FandaP bathrobe smile normal with dissolve
    with dissolve
    "听到这里，我毛骨悚然。我突然后悔来到这里了。"
    pause 0.5
    extend "\n但是一旁的阿P看见我的样子，不禁笑了起来。"
    FandaP "你呀，果然还是Too young！"

label main8:
    "然后，阿P把我带到书桌前。"
    scene bg outside phome desk supportpaper
    show FandaP uniform smile normal
    with dissolve
    FandaP "你是幻想乡来的。"
    I "对，有什么问题吗？"
    FandaP "那我可要给你好好解释一下了。"
    FandaP """在这个世界，有一个神人，名字叫太田顺也。

    他创造了一个世界观，名为“东方”。

    在这个世界观里，妖怪们为了维护自身的稳定，建立了幻想乡。"""
    I "我知道啊，幻想乡的故事，我从小听到大的。"
    FandaP "这样啊……"
    show FandaP uniform thought normal lookinme with dissolve 
    "阿P手托着腮，一双眼睛盯着我。"
    FandaP "事情开始变的有趣起来了呢……"
    I "这个幻想乡对我而言是真实的，对你而言却是虚构的？"
    FandaP "是这样的呢……"
    show FandaP uniform thought normal eyesclose with dissolve
    "我和阿P大眼瞪着小眼，空气一时间凝固了下来。"
    I "所以？"
    FandaP "……"
    show FandaP uniform thought normal lookinme with dissolve
    "阿P就这样继续盯着我。"
    pause 0.5
    extend "过了一会，阿P重新开口。"
    FandaP "我带你去找两个人。"
    I "休息一下吧，现在是晚上了嘛。"
    FandaP "额，那，就明天吧……"
    I "我们这是要去找谁啊？"
    FandaP "去找……两个犯了事的家伙。"


label main9:
    scene bg outside 
    show FandaP uniform smile normal
    with Fade(0.5,3,0.5)
    I "咳咳……"
    "风刮在我的脸上，漫天的灰尘涌来。"
    pause 0.5
    extend "\n我感到肺一阵瘙痒。"
    "我不禁把眼睛眯了起来。"
    I "呃……"
    "我指着这一片钢筋，抬起头望向阿P："
    I "你确定TA住这?"
    FandaP "欸……？"
    "阿P低下头，扫了一眼手中发光的板砖，嘟囔着："
    FandaP "对啊……导航显示就在这啊……"
    "阿P抬头望向周围，在水泥地中穿梭。"
    "阿P一会儿蹲下身，翻起随意堆砌的的砖头，一会儿跑到造了一半的大楼里，张开嘴，不知道在喊着什么。"
    "我在远处看着阿P。太阳都挂到顶头了，阿P才垂着脑袋，拖着一双腿，又站到了我的面前。"
    show FandaP uniform dissapoint normal with dissolve
    FandaP "这小子……\n明明发的地位就是这里，现在却没了人影。"
    I "有没有可能……"
    I "你说那个人，压根就不住在这里……"
    FandaP "不可能！我找路从来没错过！"
    "？？？" "えっ？牢P你怎么在这？"
    "我转过头，看见一个带着奇怪面罩的人走了过来。"
    I "卧槽!"
    "我一哆嗦，忍不住向后退了一步。"
    "阿P眉头一蹙，指着他的鼻子，破口骂道："
    FandaP "我靠，古神你tm死哪去了？"
    zectbumokhfs "蛤？"
    "古神一愣，指着自己，反问道："
    zectbumokhfs "我又怎么了？"
    FandaP "你说你早上在你家门口等我，你看看现在什么时候了！"
    zectbumokhfs "蛤？"
    "古神茫然地睁大了眼睛，看了看我，又看了看阿P，道："
    zectbumokhfs "我家是住对面小区啊……"
    FandaP "啊？"
    "阿P缓缓转头看向了我，抿着嘴，打岔道："
    FandaP "好了好了……既然人已经找到了，那我们就说事吧……"
    I "啧。"
    "我鄙夷地看了阿P一眼，但也没计较。"
    "阿P清了清嗓子，走到对方身旁，拍了拍他的肩膀，介绍道："
    FandaP "这位就是扎克得布莫柯赫佛斯（zectbumokhfs)，你可以叫他古神。"

