# -*- coding: utf-8 -*


def evaluation(pe, total,
               asset_liability_ratio,
               operational_capacity,
               profit_ability):

    net_per_share = (asset_liability_ratio.latest_equity() / total)

    return profit_ability.net_profit_rate()[0] * \
           operational_capacity.total_asset_turnover()[0] *\
           net_per_share * \
           asset_liability_ratio.equity_multiplier()[0] *\
           pe


