
titles = "本周的金枪鱼之夜，" \
         "我们邀请了计算机系高性能所的陈康副教授给大家讲授关于分布式系统的基础知识，" \
         "以及著名的分布式一致性算法 Paxos 协议。"

title_list = titles.split('，')
title_list = set(title_list)

keyword = '分布式 Paxos'  # 分词暂不考虑

for title in title_list:
    ifmatch = True
    for word in keyword.split():
        title = title.replace(word, ' #{}# '.format(word))
        if word not in title:
            ifmatch = False

    if ifmatch:
        print(title)

