# oilprice-extract

[Overview](#overview) | [Requirements](#requirements) | [Project Setup](#project-setup)
 | [How to use](#how-to-use) 

## Overview
This project uses [oilprice-api](https://github.com/oilshit/oilprice-api) initiated by [oilshit](https://github.com/oilshit) to extract oil and gas prices data into tables.

## Requirements
- Python 3

## Project Setup
You have to start the **oilprice-api** server as documented in [oilprice-api repository](https://github.com/oilshit/oilprice-api) before using this project.


## How to use
In your console (**Terminal** on Linux and MacOS, **WSL console** on Windows), just type:

```bash
python3 main.py <blend> <period>
```

with `blend` and `period` arguments can be search in https://oilprice-api.herokuapp.com/blend-list.

### Example

In case of getting **monthly** prices in **WTI** (West Texas Intermediate), you can simply type

```bash
python3 main.py wti montly
```

**Result**: the CSV file with filename **prices-wti-monthly.csv** will be appeared once the script was run. In case of getting other prices data, you can view the blend list via `https://oilprice-api.herokuapp.com/blend-list` in browser.
