#1
def StockBuyandSell(arr: list) -> int:

    return maxProfit(arr, 0, len(arr))


def maxProfit(a, start, end):
    if end <= start or start < 0 or end < 0 or start > len(a) or end > len(a):
        return 0
    profit = 0
    for i in range(start, end - 1):
        for j in range(i + 1, end):
            if a[j] > a[i]:
                current_profit = a[j] - a[i] + maxProfit(
                    a, start, i - 1) + maxProfit(a, j + 1, end)
                profit = max(profit, current_profit)
    return profit


print(StockBuyandSell([1, 5, 3, 8, 12]))
