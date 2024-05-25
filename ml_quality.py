import numpy as np
def forecast_quality_predict(history, horizon=10, alpha=0.3, beta=0.1):
    n = len(history)
    level = history[0]; trend = 0
    fitted = []
    for t in range(n):
        prev_level = level
        level = alpha*history[t] + (1-alpha)*(level+trend)
        trend = beta*(level-prev_level) + (1-beta)*trend
        fitted.append(round(level+trend, 1))
    forecasts = []
    for h in range(1, horizon+1):
        forecasts.append(round(level + trend*h, 1))
    residuals = np.array(history) - np.array(fitted)
    rmse = round(np.sqrt(np.mean(residuals**2)), 2)
    return {{"forecasts": forecasts, "rmse": rmse, "last_level": round(level,1),
            "trend_per_period": round(trend,2), "fitted_last5": fitted[-5:]}}
if __name__=="__main__":
    np.random.seed(42)
    hist = (np.cumsum(np.random.normal(-0.1, 1, 60)) + 98).tolist()
    r = forecast_quality_predict(hist)
    print(f"RMSE: {{r['rmse']}}, Trend: {{r['trend_per_period']}}")
    print(f"Forecast: {{r['forecasts']}}")
