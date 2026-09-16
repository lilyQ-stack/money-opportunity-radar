import json
from datetime import datetime
from pathlib import Path

from score import enrich_opportunity

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "sample_opportunities.json"
REPORT_DIR = ROOT / "reports" / "daily"


def load_items():
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def money(value):
    return f"¥{value:.2f}"


def main():
    items = [enrich_opportunity(x) for x in load_items()]
    items.sort(key=lambda x: x["radar_score"], reverse=True)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    target = REPORT_DIR / f"{today}-opportunities.md"

    lines = [
        f"# Money Opportunity Radar — {today}",
        "",
        "> 当前为 v0.1 演示数据报告。挂价不等于成交价，结果仅用于观察和核验。",
        "",
        "| 项目 | 成本 | 二手参考价 | 毛价差 | 毛价差率 | 雷达分 | 状态 |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]

    for item in items:
        lines.append(
            f"| {item['name']} | {money(item['retail_price'])} | "
            f"{money(item['resale_reference_price'])} | {money(item['gross_spread'])} | "
            f"{item['gross_margin_pct']:.1f}% | {item['radar_score']:.2f} | {item['status']} |"
        )

    lines += ["", "## 核验细节", ""]

    for item in items:
        lines += [
            f"### {item['name']}",
            f"- 类别：{item.get('category', '')}",
            f"- 流动性：{item.get('liquidity_score', 0)}/5",
            f"- 获取便利度：{item.get('acquisition_score', 0)}/5",
            f"- 资金占用：{item.get('capital_lock_score', 0)}/5",
            f"- 证据置信度：{float(item.get('confidence', 0)):.0%}",
            f"- 来源说明：{item.get('source_notes', '')}",
            "",
        ]

    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
