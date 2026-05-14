from sklearn.linear_model import LinearRegression
import numpy as np

def analyze_trends(df):
    """Анализирует тренды с помощью линейной регрессии и скользящего среднего."""
    X = np.arange(len(df)).reshape(-1, 1)
    y = df['actual'].values
    model = LinearRegression().fit(X, y)
    trend_line = model.predict(X)

    df['rolling_avg'] = df['actual'].rolling(window=3).mean()

    return {
        'trend_line': trend_line,
        'rolling_avg': df['rolling_avg'].tolist()
    }
