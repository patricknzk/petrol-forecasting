library(lubridate)
prices = read.csv("eleven-7_endeavourhills_prices.csv")
prices$timestamp = parse_date_time(prices$timestamp, orders = c("d/m/Y H:M", "Y-m-d H:M:S"))
plot(prices$timestamp, prices$price.91)
