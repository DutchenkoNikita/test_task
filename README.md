# test_task

1. 
Consider influenza epidemics for 2-person families. The probability is 21% that at least one
has disease. The probability that the husband has contracted influenza is 15% while the
probability that both the wife and husband have contracted the disease is 10%. What is the
probability that the wife has influenza?

     X=husband, B = wife
     P(X | Y)=21%, P(X)=15%, P(X & Y)=10%. 
     Since we know P(AuB)=P(A)+P(B)-P(AnB), therefore P(A)=P(AuB)-P(B)+P(AnB)
     P(Y) = P(X | Y) - P(X) + P(X & Y)
     P(Y) = 0.21 - 0.15 + 0.10 = 0.16

     The probability that the wife has influenza is 16%.



2. 
 2.1. How many tons worth of fruit does an average seller have?
 
     Select seller_id, AVG(fruit_weight) from seller_info
     group by seller_id order by seller_id

 2.2. How many sellers have at least one client who purchased their fruit?

     select count(seller_id) from(
     select seller_id, count(client_id) from consumption_info
     group by seller_id
     having count(client_id) > 0) table_final
