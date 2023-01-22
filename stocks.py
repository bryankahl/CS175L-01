COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

amountPaidForStock = NUM_SHARES * PURCHASE_PRICE

purchaseCommission = COMMISSION_RATE * amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission

stockSoldFor = NUM_SHARES * SELLING_PRICE

sellingCommission = COMMISSION_RATE * stockSoldFor

totalReceived = stockSoldFor - sellingCommission

profitOrLoss = totalReceived - totalPaid

print(f'Amount paid for stock: ${amountPaidForStock:,.2f}')

print(f'Commission paid on the purchase: ${purchaseCommission:,.2f}')

print(f'Amount the stock sold for: ${stockSoldFor:,.2f}')

print(f'Sommission paid on the sale: ${sellingCommission:,.2f}')

print(f'Profit (or loss if negative): ${profitOrLoss:,.2f}')


