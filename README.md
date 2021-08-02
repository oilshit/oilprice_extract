# oilprice-extract

## Overview
This project uses [oilprice-api](https://github.com/oilshit/oilprice-api) initiated by [oilshit](https://github.com/oilshit) to extract oil and gas prices data into tables.

## Requirements
- Python 3
- Node.js, used to activate **oilprice-api** server (you can download it [here](https://nodejs.org/en/))
- [oilprice-api](https://github.com/oilshit/oilprice-api)

## How to use

In your console (**Terminal** on Linux and MacOS, **WSL console** on Windows), just type:

```bash
python3 main.py <blend> <period>
```

with `blend` and `period` arguments can be search in http://localhost:3000/blend-list.

### Example

In case of getting **monthly** prices in **WTI** (West Texas Intermediate), you can simply type

```bash
python3 main.py wti montly
```

**Result**: the CSV file with filename **prices-wti-monthly.csv** will be appeared once the script was run.
