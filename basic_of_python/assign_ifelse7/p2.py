"""5. Smart Warehouse Dispatch System
A warehouse decides dispatch strategy based on stock
 availability, priority level, and delivery distance.
If stock is at least 100, then check priority. If high priority,
 then check distance. If distance is up to 200, dispatch 
immediately; otherwise use fast courier. If priority is not high,
 then check if stock is at least 300. If yes,
 bulk dispatch; otherwise normal dispatch.
  If stock is less than 100, then check if stock is at
  least 50. If yes, and priority is high, partially dispatch;
   otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier"""

s = int(input("Enter stock: "))
p = input("Enter priority: ")
d = int(input("Enter distance: "))
if s >= 100:
    if p == "high":
        if d <= 200:
            st = "Dispatch Immediately"
        else:
            st = "Dispatch via Fast Courier"
    else:
        if s >= 300:
            st = "Bulk Dispatch"
        else:
            st = "Normal Dispatch"
else:
    if s >= 50:
        if p == "high":
            st = "Partially Dispatch"
        else:
            st = "Hold"
    else:
        st = "Out of Stock"

print("Dispatch Status =", st)