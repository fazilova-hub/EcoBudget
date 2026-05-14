import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df, trends):
    """Создаёт графики и диаграммы."""
    plt.figure(figsize=(12, 8))

    # Столбчатая диаграмма отклонений
    plt.subplot(2, 2, 1)
    plt.bar(df['category'], df['rel_deviation'])
    plt.title('Относительные отклонения по статьям')
    plt.xlabel('Статьи бюджета')
    plt.ylabel('Отклонение (%)')

    # Линейный график тренда
    plt.subplot(2, 2, 2)
    plt.plot(df['period'], df['actual'], label='Фактические')
    plt.plot(df['period'], trends['trend_line'], label='Тренд (линейная регрессия)')
    plt.title('Динамика фактических расходов и тренд')
    plt.legend()


    # Круговая диаграмма структуры бюджета
    plt.subplot(2, 2, 3)
    plt.pie(df['actual'], labels=df['category'], autopct='%1.1f%%')
    plt.title('Структура бюджета по статьям')

    # Тепловая карта отклонений
    plt.subplot(2, 2, 4)
    sns.heatmap(df[['rel_deviation']].T, annot=True, cmap='coolwarm', center=0)
    plt.title('Тепловая карта отклонений')


    plt.tight_layout()
    plt.savefig('visualizations.png')
    plt.show()
8. Файл recommendations.py
python
def generate_recommendations(metrics, trends):
    """Генерирует текстовые рекомендации на основе анализа."""
    recommendations = []

    if metrics['execution_rate'] < 90:
        recommendations.append("Бюджет выполняется менее чем на 90%. Рекомендуется пересмотреть статьи с наибольшими отклонениями.")
    if metrics['execution_rate'] > 110:
        recommendations.append("Перерасход бюджета более 10%. Проанализируйте причины перерасхода.")

    trends_rising = any(trends['trend_line'][i] > trends['trend_line'][i-1] for i in range(1, len(trends['trend_line'])))
    if trends_rising:
        recommendations.append("Наблюдается рост расходов. Рассмотрите возможность оптимизации.")

    return recommendations
