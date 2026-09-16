# Secondary-market validation rules

The radar must not treat a single asking price as evidence of profit.

## Evidence levels

- `E0`: official release information only; no secondary-market evidence.
- `E1`: one or more asking prices found; no evidence of a completed transaction.
- `E2`: multiple independent asking/bid observations or a credible media report describing a market price range.
- `E3`: completed transaction evidence with quantity/time/price, or multiple credible transaction observations.

## Price fields

For each candidate, store separately when available:

- `retail_price`: official acquisition cost.
- `asking_price_low`, `asking_price_median`, `asking_price_high`: seller asking-price observations.
- `bid_price`: observable buyer/acquirer price where available.
- `transaction_price`: completed transaction evidence.
- `fees_estimate`: platform, shipping and other expected selling costs.
- `net_spread_estimate`: use transaction/bid evidence preferentially; never use the highest asking price as the default resale value.

## Risk flags

- `pre_release`: physical goods are not yet available; secondary listings may be speculative pre-sales.
- `thin_market`: too few independent observations.
- `asking_only`: no completed-sale evidence.
- `hype_spike`: large short-term attention increase without matching transaction evidence.
- `supply_release_risk`: substantial supply is about to enter the market after reservation/exchange/launch.
- `condition_sensitive`: value depends heavily on serial number, condition, packaging or variant.

## MVP decision rule

The radar does not output BUY/SELL instructions. It outputs evidence status:

- `DISCOVERED`: scarcity/release signal found.
- `VERIFY_MARKET`: asking-price or attention signal exists but transaction evidence is insufficient.
- `PRICE_CONFIRMED`: credible transaction/bid evidence exists and acquisition cost is known.
- `MONITOR`: evidence exists but spread/liquidity/risk needs more observations.
- `EXPIRED`: acquisition window has closed or the signal is stale.

For the initial experiment, opportunities should normally remain below `PRICE_CONFIRMED` until at least E2 evidence is available, and preferably E3 before estimating executable net profit.
