//+------------------------------------------------------------------+
//|                                                     TradeManagerEA.mq4 |
//|                        Copyright 2024, MetaTrader User            |
//|                                       https://www.mql5.com        |
//+------------------------------------------------------------------+
#property strict

// Input parameters
input string TradeSizes = "0.01,0.03,0.05,0.08";  // Lot sizes for the trades to manage
input bool CheckOnCloseOfBar = true;             // Check on close of bar
input bool MoveToBreakEven = true;               // Move to break-even option
input double BreakEvenPips = 4.0;                // Pips in profit to move to break-even
input bool CloseTrade = false;                   // Close trade option

// Arrays to store trade sizes
double TradeSizesArray[];

int OnInit()
{
    // Initialize the array with trade sizes
    int count = StringToArray(TradeSizesArray, TradeSizes, ',');
    if (count < 1)
    {
        Print("Invalid trade sizes");
        return INIT_FAILED;
    }
    return INIT_SUCCEEDED;
}

void OnTick()
{
    // Check if the current bar has closed
    static datetime lastTime = 0;
    if (CheckOnCloseOfBar && lastTime == Time[0])
        return;

    lastTime = Time[0];

    // Iterate over all open trades
    for (int i = OrdersTotal() - 1; i >= 0; i--)
    {
        if (OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
        {
            double lotSize = OrderLots();

            // Check if the trade lot size is in the managed list
            if (ArrayBinarySearch(TradeSizesArray, lotSize) >= 0)
            {
                ManageTrade();
            }
        }
    }
}

void ManageTrade()
{
    // Move to break-even
    if (MoveToBreakEven && OrderProfit() > BreakEvenPips * Point)
    {
        double newStopLoss = OrderOpenPrice();
        if (OrderStopLoss() < newStopLoss)
        {
            OrderModify(OrderTicket(), OrderOpenPrice(), newStopLoss, OrderTakeProfit(), 0, clrNONE);
            Print("Trade moved to break-even: ", OrderTicket());
        }
    }

    // Close trade
    if (CloseTrade)
    {
        OrderClose(OrderTicket(), OrderLots(), MarketInfo(OrderSymbol(), MODE_BID), 3, clrNONE);
        Print("Trade closed: ", OrderTicket());
    }
}
