# ARIMA, SARIMA and SARIMAX
Forecasting is applied to daily business performance data (revenue, discount rate, and coupon rate over time). The goal is to predict future revenue based on historical patterns and possibly the influence of pricing strategies like discounts and coupons. A basic approach would use ARIMA to model revenue purely from its past values, capturing trends and short-term dependencies. If your data shows recurring patterns (e.g., weekly or monthly sales cycles), SARIMA would be more appropriate because it accounts for seasonality. Since your dataset also includes variables like discount rate and coupon rate—which directly affect revenue—a SARIMAX model is the most suitable, as it can incorporate these external factors to improve forecast accuracy. This allows you not only to predict future revenue but also to understand how pricing strategies impact sales over time, making it valuable for business planning and optimization.

Jupyter Notebook: [ARIMA, SARIMA and SARIMAX.ipynb](/python/ARIMA,%20SARIMA%20and%20SARIMAX.ipynb)

Dataset files: [daily_revenue.csv](/python/daily_revenue.csv) and [future_regressors.csv](/python/future_regressors.csv)
