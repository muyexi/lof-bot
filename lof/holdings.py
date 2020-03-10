from collections import namedtuple

# 南方原油持仓及基准
# 38335 WisdomTree WTI Crude Oil
# 44793 United States 12 Month Oil Fund LP
# 995771 UBS ETF CHCMCI Oil SF USD A-dis https://cn.investing.com/etfs/ubs-cmci-oil-sf-usd
# 44794 United States Oil Fund LP
# 44792 Invesco DB Oil Fund
# 38324 WisdomTree Brent Crude Oil
# 44634 United States Brent Oil Fund LP
# 37450 WisdomTree Brent Crude Oil 1mth
# 1014132 iPath S&P GSCI Crude Oil Total Return Index ETN

# 8833 brent oil
# 8849 wti oil

Info = namedtuple("Info", ["name", "url", "currency"])

infos = {
    "38335": Info(
        "WisdomTree WTI Crude Oil (CRUD)", "etfs/etfs-crude-oil", "USD"
    ),
    "44793": Info(
        "United States 12 Month Oil Fund, LP (USL)",
        "etfs/united-states-12-month-oil",
        "USD",
    ),
    "995771": Info(
        "UBS CMCI Oil SF (OILUSA)", "etfs/ubs-cmci-oil-sf-usd", "USD"
    ),
    "44794": Info(
        "United States Oil Fund, LP (USO)", "etfs/united-states-oil-fund", "USD"
    ),
    "44792": Info(
        "Invesco DB Oil Fund (DBO)", "etfs/powershares-db-oil-fund", "USD"
    ),
    "38324": Info(
        "WisdomTree Brent Crude Oil (BRNT)", "etfs/etfs-brent-crude", "USD"
    ),
    "44634": Info(
        "United States Brent Oil Fund, LP (BNO)",
        "etfs/united-states-brent-oil-fund-lp",
        "USD",
    ),
    "37450": Info(
        "WisdomTree Brent Crude Oil 1 month (OILB)",
        "etfs/etfs-brent-1mth-uk",
        "USD",
    ),
    "1014132": Info(
        "iPath® S&P GSCI® Crude Oil Total Return Index ETN (OIL)",
        "etfs/ipath-series-b-sp-gsci-crd-oil-tr",
        "USD",
    ),
    "8833": Info("伦敦布伦特原油期货", "commodities/brent-oil", "USD"),
    "8849": Info("WTI原油期货", "commodities/crude-oil", "USD"),
    "38284": Info(
        "SPDR® S&P Oil & Gas Exploration & Production ETF (XOP)",
        "etfs/spdr-s-p-oil--gas-explor---product",
        "USD",
    ),
    "1010825": Info(
        "S&P Oil & Gas Exploration & Production Select Industry TR (SPSIOPTR)",
        "indices/s-p-oil-gas-exploration-product-tr",
        "USD",
    ),
    # no valid realtime data and historical data update is not immediate. 9.00am BJ time is not enough to check yesterday value
    "14218": Info(
        "ProShares Ultra Bloomberg Crude Oil (UCO)",
        "etfs/proshares-ultra-dj-ubs-crude-oil",
        "USD",
    ),
    "37471": Info(
        "Invesco DB US Dollar Index Bullish Fund (UUP)",
        "etfs/powershares-db-usd-index-bullish",
        "USD",
    ),
    "44798": Info(
        "VelocityShares 3x Long Crude Oil ETNs linked to the S&P GSCI® Crude Oil Index ER New (UWT)",
        "etfs/velocityshares-3x-long-crude-oil",
        "USD",
    ),
    "44718": Info(
        "Invesco DB Precious Metals Fund (DBP)",
        "etfs/powershares-db-precious-metals",
        "USD",
    ),
    "9236": Info(
        "iShares Silver Trust (SLV)", "etfs/ishares-silver-trust", "USD"
    ),
    "1122426": Info(
        "S&P GSCI Crude Oil Index Excess Return (SPGSCLP)",
        "indices/s-p-gsci-crude-oil-er-historical-data",
        "USD",
    ),  # no valid realtime data
    "953362": Info("Simplex WTI (1671)", "etfs/simplex-wti", "100JPY"),
    "953293": Info(
        "NEXT FUNDS Nomura Crude Oil Long (1699)",
        "etfs/next-funds-nomura-crude-oil-long",
        "100JPY",
    ),
}


holdings = {}

# 2019 第四季度季报披露
# reference: http://pdf.dfcfw.com/pdf/H2_AN202001191374337197_1.pdf
holdings_501018_19s3 = {
    "37450": 15.31,
    "44792": 13.64,
    "44794": 13.46,
    "44634": 12.48,
    "38335": 11.73,
    "38324": 9.45,
    "995771": 6.53,
    "44793": 6.02,
    "1014132": 5.42,
}
# 2019 第三季度季报披露
# reference: http://pdf.dfcfw.com/pdf/H2_AN201910241369695857_1.pdf
holdings_501018_19s4 = {
    "38335": 7.34,
    "44793": 8.14,
    "995771": 8.68,
    "44794": 9.63,
    "44792": 11.6,
    "38324": 15.04,
    "44634": 15.42,
    "37450": 17.51,
    "1014132": 0.06,
}
holdings_501018_bc_cash = {"8849": 52.8, "8833": 35.2}
# holdings_bc = {"8849": 60, "8833": 40}

# 2019 第四季度季报披露
# reference: http://pdf.dfcfw.com/pdf/H2_AN202001161374256079_1.pdf
holdings_160216_19s4 = {
    "44794": 16.9,
    "14218": 14.03,
    "44634": 11.77,
    "37471": 10.98,
    "44792": 9.1,
    "44798": 7.82,
    "1014132": 7.76,
    "44793": 2.25,
    "44718": 0.01,
    "9236": 0,
}

# 华宝油气直接按持仓跟踪指数模拟，实际其直接持仓成分股
holdings_162411_19s4 = {"1010825": 91}

# 华安标普全球石油指数
# reference: http://pdf.dfcfw.com/pdf/H2_AN202001201374395365_1.pdf
holdings_160416_19s4 = {}
# couldn't find the benchmark index as investing.com: S&P Global Oil Index Net Total Return

# 易方达原油
# reference http://pdf.dfcfw.com/pdf/H2_AN202001171374296729_1.pdf
holdings_161129_19s4 = {
    "38335": 18.96,
    "44794": 18.81,
    "44634": 18.63,
    "44792": 18.39,
    "953362": 10.26,
    "44793": 4.18,
    "953293": 3.6,
    "37450": 1.64,
}
holdings_161129_bc_cash = {"1122426": 90.92}

# 嘉实原油
# reference: http://pdf.dfcfw.com/pdf/H2_AN202001201374377449_1.pdf
# 一个跟踪基准100% WTI 的基金为何买了这么多跟踪 brent 的基金。。。
holdings_160723_19s4 = {
    "38324": 18.96,
    "44792": 16.65,
    "37450": 14.87,
    "44793": 14.48,
    "44634": 13.79,
    "38335": 13.32,
    "44794": 6.47,
}
holdings_160723_bc_cash = {"8849": 93.55}

holdings["501018"] = holdings_501018_19s4
holdings["160216"] = holdings_160216_19s4
holdings["162411"] = holdings_162411_19s4
holdings["161129"] = holdings_161129_19s4
holdings["160723"] = holdings_160723_19s4

holdings["oil_rt"] = {
    "commodities/brent-oil": 40 * 0.9,
    "commodities/crude-oil": 60 * 0.9,
}