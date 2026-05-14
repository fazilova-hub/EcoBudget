import pandas as pd

def calculate_deviations(df):
    """Рассчитывает абсолютные и относительные отклонения."""
    df['abs_deviation'] = df['actual'] - df['planned']
    df['rel_deviation'] = (df['abs_deviation'] / df['planned']) * 100
    return df

def calculate_budget_metrics(df):
    """Рассчитывает коэффициенты выполнения бюджета."""
    total_planned = df['planned'].sum()
    total_actual = df['actual'].sum()
    execution_rate = (total_actual / total_planned) * 100
    return {
        'total_planned': total_planned,
        'total_actual': total_actual,
        'execution_rate': execution_rate
    }
