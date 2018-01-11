# HW07
## 作業名稱:Quantopian策略建構

策略績效:
* Return = 103.9%
* Alpha = 0.1
* Beta = 0.92
* Sharpe = 0.80
* Drawdown = -36.18%


程式碼:

def initialize(context):

    #選擇使用的股票
    context.securities = [sid(24),sid(16841),sid(25006),sid(13835)]

    #設定條件
    schedule_function(rebalance, date_rule=date_rules.every_day())

def rebalance(context, data):

    #使用迴圈概念，讓使用的股票每一檔都可以跑
    for stock in context.securities:

        #設定價格的歷史資料條件
        price_history = data.history(
            stock,
            fields='price',
            bar_count=5,
            frequency='1d'
        )

        #設定交易量的歷史資料條件
        volume_history = data.history(
            stock,
            fields='volume',
            bar_count=1,
            frequency='1d'
        )

        #計算平均價格與平均交易量
        average_price = price_history.mean()
        average_volume = volume_history.mean()

        #取得目前在可以使用的價格與交易量
        current_price = data.current(stock, 'price')
        current_volume = data.current(stock, 'volume')

        #設定進出場策略，若目前價格高於平均價格的1.01倍，買入一單位
        #設定進出場策略，若目前交易量高於平均交易量，買入一單位
        if data.can_trade(stock):

            if current_price > (1.01 * average_price):
                order_target_percent(stock, 1)
                log.info("Buying %s" % (stock.symbol))

            elif current_price < average_price:
                order_target_percent(stock, 0)
                log.info("Selling %s" % (stock.symbol))

            if current_volume >  average_volume:
                order_target_percent(stock, 1)
                log.info("Buying %s" % (stock.symbol))

            elif current_volume < average_volume:
                order_target_percent(stock, 0)
                log.info("Selling %s" % (stock.symbol))

    #紀錄目前價格，平均價格，目前交易量，平均交易量
    record(current_price=current_price, average_price=average_price)
    record(current_volume=current_volume, average_volume=average_volume)
