import timeit
import statistics

# local module
import thingtotest

def test1():
    results = timeit.repeat (stmt="thingtotest.main()", number=100, globals=globals())
    minresult = min (results)
    maxresult = max (results)
    meanresult = statistics.mean (results)
    print ("RESULTS:", results)
    print ("MIN:", minresult)
    print ("MEAN:", meanresult)
    print ("MAX:", maxresult)
    print ()

if __name__ == "__main__":
    test1()
