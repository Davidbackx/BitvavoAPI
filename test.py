# import matplotlib.pyplot as plt
# from datetime import datetime
# # from bitvavo_api import data
# data = [{'ema': 0.4659, 'time': 1657718150337}, {'ema': 0.4587, 'time': 1657801849344}, {'ema': 0.4599, 'time': 1658133987379}, {'ema': 0.4616, 'time': 1658216452802}, {'ema': 0.4681, 'time': 1658341792800}, {'ema': 0.4703, 'time': 1658391227489}, {'ema': 0.4704, 'time': 1658519502210}, {'ema': 0.4712, 'time': 1658593679981}, {'ema': 0.4789, 'time': 1658655431893}, {'ema': 0.4795, 'time': 1658748692981}, {'ema': 0.4754, 'time': 1658856744808}, {'ema': 0.4733, 'time': 1658911517884}, {'ema': 0.4762, 'time': 1658993508318}, {'ema': 0.4823, 'time': 1659102289392}, {'ema': 0.4899, 'time': 1659194526392}, {'ema': 0.4943, 'time': 1659271354983}, {'ema': 0.4932, 'time': 1659648022925}, {'ema': 0.4941, 'time': 1659685534104}, {'ema': 0.4962, 'time': 1659859192406}, {'ema': 0.5019, 'time': 1659952490002}, {'ema': 0.5015, 'time': 1660127268944}, {'ema': 0.5046, 'time': 1660296493508}, {'ema': 0.5117, 'time': 1660590834894}, {'ema': 0.5191, 'time': 1660640962310}, {'ema': 0.5246, 'time': 1660683099995}, {'ema': 0.5283, 'time': 1660727293394}, {'ema': 0.5178, 'time': 1660982544857}, {'ema': 0.5089, 'time': 1661070460328}, {'ema': 0.5002, 'time': 1661195575023}, {'ema': 0.4933, 'time': 1661240773449}, {'ema': 0.4885, 'time': 1661332383640}, {'ema': 0.4819, 'time': 1661869965936}, {'ema': 0.4775, 'time': 1661900600038}, {'ema': 0.4741, 'time': 1662145600432}, {'ema': 0.4737, 'time': 1662197811948}, {'ema': 0.4731, 'time': 1662198093621}, {'ema': 0.4765, 'time': 1663001512332}, {'ema': 0.4796, 'time': 1663057948825}, {'ema': 0.4788, 'time': 1663139840941}, {'ema': 0.4791, 'time': 1663173880038}, {'ema': 0.4795, 'time': 1663174150453}, {'ema': 0.4793, 'time': 1663227786650}, {'ema': 0.4787, 'time': 1663247482610}, {'ema': 0.477, 'time': 1663257279206}, {'ema': 0.4755, 'time': 1663314326787}, {'ema': 0.4756, 'time': 1663414931607}, {'ema': 0.476, 'time': 1663495958112}]
# val = ([data[idx]["ema"] for idx,_ in enumerate(data)])
# print(val)
market = {"market": "CMT-EUR", "open": None, "high": None, "low": None, "last": None, "volume": None, "volumeQuote": None, "bid": "0.027029", "bidSize": "16483.49067479", "ask": "0.029029", "askSize": "47.06205", "timestamp": 1663858397503}


# if '-BTC' not in market["market"]:
#     has_none_values = False
#     for item in market.items():
#         if item == None:
#             print(item)
#             has_none_values = True
#             break
#     if has_none_values:
#         str_market = str(market)
#         changed = str_market.replace("'","\"")
#         print(changed)
if '-BTC' not in market["market"]:
    values = ([item for item in market.values()])
    if None not in values:
        print("good data")
    else:
        print("Bad Data")
