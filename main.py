import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from data_loader import load_data
from data_validation import validate_data
from analysis import calculate_deviations, calculate_budget_metrics
from trend_analysis import analyze_trends
from visualization import create_visualizations
from recommendations import generate_recommendations
from export_pdf import export_to_pdf
from export_excel import export_to_excel

def main():
    root = tk.Tk()
    root.title("EcoBudget — Анализ бюджетных данных")
    root.geometry("400x300")

    def load_and_analyze():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        try:
            df = load_data(file_path)
            validation_result = validate_data(df)
            if not validation_result['is_valid']:
                messagebox.showerror("Ошибка", f"Ошибки в данных: {validation_result['errors']}")
                return

            deviations = calculate_deviations(df)
            metrics = calculate_budget_metrics(deviations)
            trends = analyze_trends(df)
            recommendations = generate_recommendations(metrics, trends)

            create_visualizations(deviations, trends)
            export_to_pdf(deviations, metrics, recommendations, "report.pdf")
            export_to_excel(deviations, "budget_analysis.xlsx")

            messagebox.showinfo("Успех", "Анализ завершён! Отчёты сохранены.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    btn_load = tk.Button(root, text="Загрузить CSV и запустить анализ", command=load_and_analyze)
    btn_load.pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()
