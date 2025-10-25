'''
---

### **Rephrased Problem**

You go to a shop with **n items for sale**.

* You are given an array `A` of length `n`, where `A[i]` represents the **cost of the i-th item**.
* You have a total of `k` units of currency.

The shop has **limited stock for each item**:

* The first item can be bought at most `n` times.
* The second item can be bought at most `n-1` times.
* The third item at most `n-2` times.
* … and so on, until the last item, which can be bought at most **1 time**.

Your goal is to **maximize the total number of items you can buy** without exceeding your budget `k`.

**Input:**

* `A`: an array of length `n` representing item costs.
* `k`: total currency you have.

**Output:**

* Maximum number of items you can buy.

---

### **Example (for clarity)**

```
A = [3, 2, 1]
k = 7
```

Stock limits:

* Item 1 → max 3

* Item 2 → max 2

* Item 3 → max 1

* You can buy: 1 of item 3 (cost 1), 2 of item 2 (cost 4), 1 of item 1 (cost 3) → total cost 1+4+3=8 ❌ exceeds k

* Optimal: 1 of item 3 (1), 1 of item 2 (2), 2 of item 1 (6) → total cost 9 ❌

* Actually the **best is**: 1 of item 3 (1), 1 of item 2 (2), 1 of item 1 (3) → total cost 6 ✅

* Maximum items bought = 3

'''