# Money Opportunity Radar

一个用于监控公开信息中的小额套利 / 转售机会的实验项目。

## 目标

项目尝试从公开来源中收集候选商品或预约机会，并基于价格差、成交活跃度、获取难度和资金占用时间进行整理，生成每日观察报告。

这不是“稳赚项目”清单，也不构成投资或交易建议。挂价不等于成交价，历史溢价也不代表未来仍可实现。

## 当前范围（v0.1）

优先监控：

- 限量 / 联名 / 预约商品
- 上海线下限定商品
- 可网络预约或抢购的商品
- 二手市场存在明显价格差的商品

当前个人执行约束：

- 普通商品单笔成本原则上不超过 1000 元
- 纪念币等货币类可单独处理
- 需要线下购买的项目优先限制为上海
- 优先网络预约、线上购买或可明确核验的官方渠道

## 核心字段

每个候选机会至少记录：

- `name`：项目名称
- `category`：类别
- `retail_price`：官方 / 原始购买成本
- `resale_reference_price`：二手参考价
- `gross_spread`：毛价差
- `gross_margin_pct`：毛价差率
- `liquidity_score`：近期成交活跃度评分（0-5）
- `acquisition_score`：获取难度评分（0-5，分数越高越容易获得）
- `capital_lock_score`：资金占用评分（0-5，分数越高越短）
- `confidence`：证据置信度
- `status`：观察标签
- `source_notes`：来源说明

## v0.1 评分思路

第一版不会只看“挂价高不高”。综合考虑：

1. 实际价差
2. 价差率
3. 近期成交活跃度
4. 获取难度
5. 资金占用时间
6. 数据置信度

结果只用于排序观察优先级，不代表实际利润承诺。

## 目录

```text
money-opportunity-radar/
├── README.md
├── data/
│   └── sample_opportunities.json
├── reports/
│   └── daily/
├── scripts/
│   ├── score.py
│   └── report.py
└── .github/
    └── workflows/
        └── daily-radar.yml
```

## 下一步

v0.1 先验证：

- 数据结构是否够用
- 评分是否符合实际判断
- 日报是否一眼能看懂

之后再逐步接入真实公开数据源。
