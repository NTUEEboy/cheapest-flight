# 610741001 郭明儒
# 610502009 李育綺

import test_cases

def findCheapestPrice(n: int, flights: [[int]], src: int, dst: int, k: int) -> int:
        """
        Initialize the n X 1 price list.
        The price of nodes(cities) other than source are infinity.
        The price of source is 0.
        """
        prices = [float("inf")] * n # n x 1 list
        prices[src] = 0 # The price of source = 0
        
        
        # Run k + 1 time(s) if the flight go at most k stop(s)
        for i in range(k + 1):
            temPrices = prices.copy() # copy the original price list.
            
            """
            Traverse every edge
            Update the price if the price is smaller than previous result
            """
            for source, destination, price in flights:
                # BFS, the traveral haven't reached the node than skip this edge
                if prices[source] == float("inf"):
                    continue

                # Update the result if it's better than previous one 
                if prices[source] + price < temPrices[destination]: 
                    temPrices[destination] = prices[source] + price
                
            
            prices = temPrices # Update the price to original list and traverse again if applicable
        
        # Retrun -1 if there's no any route to destination
        # Otherwise return the price of destination
        return -1 if prices[dst] == float("inf") else prices[dst]

def main():
    # Test case
    case = test_cases.case1 # You can add test cases in test_cases.py
    n = case["n"]
    flights = case["flights"]
    src = case["src"]
    dst = case["dst"]
    k = case["k"]

    price = findCheapestPrice(n, flights, src, dst, k)

    print(price)
    

if __name__ == "__main__":
    main()