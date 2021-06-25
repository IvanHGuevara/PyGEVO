import sys
sys.path.append('..//..//')
print(sys.path)
import examples.Python_Trading.run as Run

run = Run.Run()
run.createPhenotypes(symbol="BTCUSDT", typeMarket="future", intervalo=5, ini="1 Jan, 2020", fin="1 Jan, 2021",individues=300, individuesSize=50, gen=10000)