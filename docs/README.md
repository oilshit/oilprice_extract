# Getting current weekly prices

**oilprice_extract** currently has two main functions: `get_blend_info(blend, period)` and `save_to_csv_data(data)`.
- `get_blend_info(blend, period)` will get the prices data based on `blend` (firms or blend) and `period` (time period) params.
    - `blend` keywords is available on [https://oilprice-api.herokuapp.com/blend-list](https://oilprice-api.herokuapp.com/blend-list).
    - `period` keywords following are supported: `daily`, `weekly`, `monthly`, `yearly`, and `max` with supported on each `blend` is availabel on [https://oilprice-api.herokuapp.com/blend-list](https://oilprice-api.herokuapp.com/blend-list).
    - Outputs:
      ```
      {
          prices: str[],
          dates: str[],
          times: str[]
      }
      ```
- `save_to_csv_data(data)` will generate prices data based on `get_blend_info` outputs.
    - `data` argument receives `get_blend_info` output result.
    - Outputs CSV file with filename **blend-period-currentunixtimestamp.csv**.