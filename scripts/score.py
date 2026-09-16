def enrich_opportunity(item):
    retail = float(item.get("retail_price", 0) or 0)
    resale = float(item.get("resale_reference_price", 0) or 0)

    gross_spread = round(resale - retail, 2)
    gross_margin_pct = round((gross_spread / retail * 100), 1) if retail > 0 else 0.0

    liquidity = float(item.get("liquidity_score", 0) or 0)
    acquisition = float(item.get("acquisition_score", 0) or 0)
    capital_lock = float(item.get("capital_lock_score", 0) or 0)
    confidence = float(item.get("confidence", 0) or 0)

    margin_score = max(0.0, min(gross_margin_pct / 10.0, 5.0))
    spread_score = max(0.0, min(gross_spread / 40.0, 5.0))

    radar_score = (
        margin_score * 0.25
        + spread_score * 0.20
        + liquidity * 0.20
        + acquisition * 0.15
        + capital_lock * 0.10
        + (confidence * 5.0) * 0.10
    )
    radar_score = round(radar_score, 2)

    if confidence < 0.5:
        status = "证据不足"
    elif gross_spread <= 0:
        status = "暂无价差"
    elif radar_score >= 4.0:
        status = "重点核验"
    elif radar_score >= 3.0:
        status = "值得观察"
    elif radar_score >= 2.0:
        status = "低优先级"
    else:
        status = "暂不关注"

    enriched = dict(item)
    enriched.update({
        "gross_spread": gross_spread,
        "gross_margin_pct": gross_margin_pct,
        "radar_score": radar_score,
        "status": status,
    })
    return enriched
