#Необходимо создать несколько курьеров и заказов. За каждого из них принять заказ
SELECT c."login" AS courier_login,
    COUNT(o."id") AS delivery_orders_count
FROM "Couriers" c
LEFT JOIN "Orders" o ON c."id" = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c."login";
