COMMISSION_RATE = float(input("What is the commission rate?: "))
NUM_SHARES = float(input("What is the numuber of shares purchased?: "))
PURCHASE_PRICE = float(input("What is the price per share?: "))
SELLING_PRICE = float(input("WHat is the price the stock was sold at?: "))

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
