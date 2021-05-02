import sys
sys.path.append('..//..//')
print(sys.path)
import Examples.Python_Trading.run as Run
import threading
import time

def worker(symbol="BTCUSDT", typeMarket="future", intervalo=3, ini="1 Ago, 2020", fin="1 Mar, 2021",
                         individues=300, individuesSize=50, gen=10000):

    run = Run.Run()
    #run.createPhenotypes(symbol="BTCUSDT", typeMarket="future", intervalo=3, ini="1 Ago, 2020", fin="1 Mar, 2021",individues=300, individuesSize=50, gen=10000)
    run.createPhenotypes(symbol, typeMarket, intervalo, ini, fin,
                         individues, individuesSize, gen)


#threads = []
#t = threading.Thread(target=worker, args=( "BTCUSDT", "future", 2, "1 Ago, 2020", "1 Mar, 2021", 200, 50, 10000))
#threads.append(t)
#t.start()
#time.sleep(5)
#t = threading.Thread(target=worker,args=("BTCUSDT", "future", 3, "1 Ago, 2020", "1 Mar, 2021",200, 50, 10000))
#threads.append(t)
#t.start()
#time.sleep(5)
#t = threading.Thread(target=worker, args=( "BTCUSDT", "future", 4, "1 Ago, 2020", "1 Mar, 2021", 200, 50, 10000))
#threads.append(t)
#t.start()
#time.sleep(5)


#1: Client.KLINE_INTERVAL_1MINUTE,
#2: Client.KLINE_INTERVAL_3MINUTE,
#3: Client.KLINE_INTERVAL_5MINUTE,
#4: Client.KLINE_INTERVAL_15MINUTE,
#5: Client.KLINE_INTERVAL_30MINUTE,
#6: Client.KLINE_INTERVAL_1HOUR,
#7: Client.KLINE_INTERVAL_2HOUR,
#8: Client.KLINE_INTERVAL_4HOUR,
run = Run.Run()
#run.createPhenotypes(symbol="BTCUSDT", typeMarket="future", intervalo=2, ini="1 Ago, 2020", fin="1 Mar, 2021",individues=300, individuesSize=50, gen=10000)
#run.createPhenotypes(symbol="BTCUSDT", typeMarket="future", intervalo=3, ini="1 Ago, 2020", fin="1 Mar, 2021",individues=300, individuesSize=50, gen=10000)
run.createPhenotypes(symbol="BTCUSDT", typeMarket="spot", intervalo=4, ini="1 Ago, 2020", fin="1 Mar, 2021",individues=300, individuesSize=50, gen=10000)
