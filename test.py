import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# Configurar aparência do CustomTkinter com tema verde
ctk.set_appearance_mode("Dark")  # Modos: "Dark", "Light", "System"

# Criar tema verde personalizado
green_theme = {
    "blue": ["#3B8ED0", "#1F6AA5"],
    "green": ["#2CC985", "#2FA572"],
    "red": ["#FA5F5A", "#BA3732"],
    "yellow": ["#F0D500", "#D4BE00"],
    "orange": ["#FF9800", "#DB8500"]
}

# Aplicar tema verde personalizado


class DashboardApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Dashboard Verde - Analytics")
        self.root.geometry("1400x900")
        
        # Dados de exemplo
        self.data = self.generate_sample_data()
        
        self.setup_ui()
        
    def generate_sample_data(self):
        """Gerar dados de exemplo para o dashboard"""
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
        sales = np.random.normal(1000, 200, len(dates))
        expenses = np.random.normal(600, 150, len(dates))
        
        return pd.DataFrame({
            'date': dates,
            'sales': sales,
            'expenses': expenses,
            'profit': sales - expenses
        })
    
    def setup_ui(self):
        """Configurar a interface do usuário"""
        # Criar layout principal
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#1a1a1a")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Barra lateral
        self.setup_sidebar()
        
        # Área principal
        self.setup_main_area()
        
    def setup_sidebar(self):
        """Configurar barra lateral"""
        self.sidebar = ctk.CTkFrame(self.main_frame, width=200, fg_color="#2d2d2d")
        self.sidebar.pack(side="left", fill="y", padx=(0, 10))
        
        # Título
        title_label = ctk.CTkLabel(self.sidebar, text="🌿 DASHBOARD VERDE", 
                                 font=ctk.CTkFont(size=18, weight="bold"),
                                 text_color="#2CC985")
        title_label.pack(pady=20)
        
        # Botões de navegação
        buttons_info = [
            ("📊 Visão Geral", self.show_overview),
            ("📈 Gráficos", self.show_charts),
            ("📋 Relatórios", self.show_reports),
            ("⚙️ Configurações", self.show_settings)
        ]
        
        for text, command in buttons_info:
            btn = ctk.CTkButton(self.sidebar, text=text, command=command,
                              fg_color="#2CC985", hover_color="#2FA572",
                              text_color="white", font=ctk.CTkFont(weight="bold"))
            btn.pack(pady=5, padx=10, fill="x")
        
        # Separador
        separator = ctk.CTkFrame(self.sidebar, height=2, fg_color="#2CC985")
        separator.pack(fill="x", pady=20)
        
        # Checklist
        self.setup_checklist()
        
        # Switches
        self.setup_switches()
        
        # Formulário simples
        self.setup_form()
        
    def setup_checklist(self):
        """Configurar checklist"""
        checklist_frame = ctk.CTkFrame(self.sidebar, fg_color="#2d2d2d")
        checklist_frame.pack(pady=10, padx=10, fill="x")
        
        checklist_label = ctk.CTkLabel(checklist_frame, text="Filtros:",
                                     text_color="#2CC985")
        checklist_label.pack(anchor="w")
        
        self.check_vars = {}
        options = ["Vendas", "Despesas", "Lucro", "Clientes"]
        
        for option in options:
            var = tk.BooleanVar(value=True)
            self.check_vars[option] = var
            cb = ctk.CTkCheckBox(checklist_frame, text=option, variable=var,
                               command=self.update_filters,
                               fg_color="#2CC985", hover_color="#2FA572",
                               checkmark_color="white")
            cb.pack(anchor="w", pady=2)
    
    def setup_switches(self):
        """Configurar switches"""
        switch_frame = ctk.CTkFrame(self.sidebar, fg_color="#2d2d2d")
        switch_frame.pack(pady=10, padx=10, fill="x")
        
        switch_label = ctk.CTkLabel(switch_frame, text="Opções:",
                                  text_color="#2CC985")
        switch_label.pack(anchor="w")
        
        self.switch_vars = {}
        switches = [
            ("Modo Escuro", self.toggle_dark_mode),
            ("Atualização Automática", self.toggle_auto_update),
            ("Notificações", self.toggle_notifications)
        ]
        
        for text, command in switches:
            var = tk.BooleanVar()
            self.switch_vars[text] = var
            switch = ctk.CTkSwitch(switch_frame, text=text, variable=var,
                                 command=command,
                                 fg_color="#2CC985", progress_color="#2FA572",
                                 button_color="white", button_hover_color="#e6e6e6")
            switch.pack(anchor="w", pady=2)
    
    def setup_form(self):
        """Configurar formulário simples"""
        form_frame = ctk.CTkFrame(self.sidebar, fg_color="#2d2d2d")
        form_frame.pack(pady=10, padx=10, fill="x")
        
        form_label = ctk.CTkLabel(form_frame, text="Configurações Rápidas:",
                                text_color="#2CC985")
        form_label.pack(anchor="w", pady=(0, 10))
        
        # Campo de texto
        self.text_entry = ctk.CTkEntry(form_frame, placeholder_text="Digite algo...",
                                     fg_color="#1a1a1a", border_color="#2CC985",
                                     text_color="white")
        self.text_entry.pack(fill="x", pady=5)
        
        # Dropdown
        self.combo_var = tk.StringVar(value="Opção 1")
        combo = ctk.CTkComboBox(form_frame, values=["Opção 1", "Opção 2", "Opção 3"],
                              variable=self.combo_var,
                              fg_color="#1a1a1a", border_color="#2CC985",
                              button_color="#2CC985", button_hover_color="#2FA572")
        combo.pack(fill="x", pady=5)
        
        # Botão de envio
        submit_btn = ctk.CTkButton(form_frame, text="Aplicar", 
                                 command=self.submit_form,
                                 fg_color="#2CC985", hover_color="#2FA572")
        submit_btn.pack(fill="x", pady=5)
    
    def setup_main_area(self):
        """Configurar área principal"""
        self.main_area = ctk.CTkFrame(self.main_frame, fg_color="#1a1a1a")
        self.main_area.pack(side="right", fill="both", expand=True)
        
        # Abas para diferentes seções
        self.tabview = ctk.CTkTabview(self.main_area, fg_color="#1a1a1a",
                                    segmented_button_fg_color="#2CC985",
                                    segmented_button_selected_color="#2FA572",
                                    segmented_button_selected_hover_color="#2CC985",
                                    text_color="white")
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Criar abas
        self.overview_tab = self.tabview.add("🌿 Visão Geral")
        self.charts_tab = self.tabview.add("📈 Gráficos")
        self.reports_tab = self.tabview.add("📋 Relatórios")
        self.settings_tab = self.tabview.add("⚙️ Configurações")
        
        # Configurar cada aba
        self.setup_overview_tab()
        self.setup_charts_tab()
        self.setup_reports_tab()
        self.setup_settings_tab()
    
    def setup_overview_tab(self):
        """Configurar aba de visão geral"""
        # Métricas principais
        metrics_frame = ctk.CTkFrame(self.overview_tab, fg_color="#1a1a1a")
        metrics_frame.pack(fill="x", padx=10, pady=10)
        
        metrics = [
            ("Total Vendas", "R$ 150.000", "↑ 12%"),
            ("Total Despesas", "R$ 80.000", "↓ 5%"),
            ("Lucro Líquido", "R$ 70.000", "↑ 18%"),
            ("Clientes Ativos", "1.250", "↑ 8%")
        ]
        
        colors = ["#2CC985", "#2FA572", "#26A669", "#1F8C5A"]
        
        for i, ((title, value, change), color) in enumerate(zip(metrics, colors)):
            metric_frame = ctk.CTkFrame(metrics_frame, width=200, height=100,
                                      fg_color=color, corner_radius=10)
            metric_frame.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
            metrics_frame.columnconfigure(i, weight=1)
            
            title_label = ctk.CTkLabel(metric_frame, text=title, 
                                     font=ctk.CTkFont(size=12, weight="bold"),
                                     text_color="white")
            title_label.pack(pady=(10, 5))
            
            value_label = ctk.CTkLabel(metric_frame, text=value,
                                     font=ctk.CTkFont(size=18, weight="bold"),
                                     text_color="white")
            value_label.pack(pady=5)
            
            change_color = "#4CD964" if "↑" in change else "#FF3B30"
            change_label = ctk.CTkLabel(metric_frame, text=change,
                                      text_color=change_color,
                                      font=ctk.CTkFont(weight="bold"))
            change_label.pack(pady=(5, 10))
        
        # Gráfico rápido
        self.create_quick_chart()
    
    def create_quick_chart(self):
        """Criar gráfico rápido para visão geral"""
        chart_frame = ctk.CTkFrame(self.overview_tab, fg_color="#1a1a1a")
        chart_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        fig = Figure(figsize=(8, 4), dpi=100, facecolor='#1a1a1a')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#1a1a1a')
        
        # Dados de exemplo
        months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
        sales = [12000, 15000, 13000, 16000, 17000, 19000]
        expenses = [8000, 9000, 8500, 9500, 10000, 11000]
        
        x = range(len(months))
        ax.bar(x, sales, width=0.4, label='Vendas', align='center', color='#2CC985')
        ax.bar([i + 0.4 for i in x], expenses, width=0.4, label='Despesas', align='center', color='#2FA572')
        
        ax.set_xticks([i + 0.2 for i in x])
        ax.set_xticklabels(months, color='white')
        ax.set_yticklabels(ax.get_yticks(), color='white')
        ax.legend(facecolor='#1a1a1a', labelcolor='white')
        ax.set_title('Vendas vs Despesas - Últimos 6 Meses', color='white')
        ax.grid(True, alpha=0.3, color='#2d2d2d')
        
        # Configurar cores dos eixos
        ax.spines['bottom'].set_color('#2CC985')
        ax.spines['top'].set_color('#2CC985')
        ax.spines['right'].set_color('#2CC985')
        ax.spines['left'].set_color('#2CC985')
        ax.tick_params(colors='white')
        
        canvas = FigureCanvasTkAgg(fig, chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def setup_charts_tab(self):
        """Configurar aba de gráficos"""
        # Controles de gráficos
        controls_frame = ctk.CTkFrame(self.charts_tab, fg_color="#1a1a1a")
        controls_frame.pack(fill="x", padx=10, pady=10)
        
        # Botões para diferentes tipos de gráfico
        chart_types = [
            ("📊 Colunas", self.show_column_chart),
            ("🥧 Pizza", self.show_pie_chart),
            ("📈 Linhas", self.show_line_chart),
            ("🟩 Área", self.show_area_chart)
        ]
        
        for i, (text, command) in enumerate(chart_types):
            btn = ctk.CTkButton(controls_frame, text=text, command=command,
                              fg_color="#2CC985", hover_color="#2FA572")
            btn.grid(row=0, column=i, padx=5, pady=5)
            controls_frame.columnconfigure(i, weight=1)
        
        # Frame para os gráficos
        self.chart_display_frame = ctk.CTkFrame(self.charts_tab, fg_color="#1a1a1a")
        self.chart_display_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Mostrar gráfico inicial
        self.show_column_chart()
    
    def show_column_chart(self):
        """Mostrar gráfico de colunas"""
        self.clear_chart_frame()
        
        fig = Figure(figsize=(10, 6), dpi=100, facecolor='#1a1a1a')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#1a1a1a')
        
        categories = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
        values1 = [23, 45, 56, 78]
        values2 = [34, 40, 52, 65]
        
        x = np.arange(len(categories))
        width = 0.35
        
        ax.bar(x - width/2, values1, width, label='2023', alpha=0.8, color='#2CC985')
        ax.bar(x + width/2, values2, width, label='2024', alpha=0.8, color='#2FA572')
        
        ax.set_xlabel('Categorias', color='white')
        ax.set_ylabel('Valores', color='white')
        ax.set_title('Comparação Anual - Gráfico de Colunas', color='white')
        ax.set_xticks(x)
        ax.set_xticklabels(categories, color='white')
        ax.set_yticklabels(ax.get_yticks(), color='white')
        ax.legend(facecolor='#1a1a1a', labelcolor='white')
        ax.grid(True, alpha=0.3, color='#2d2d2d')
        
        # Configurar cores dos eixos
        for spine in ax.spines.values():
            spine.set_color('#2CC985')
        ax.tick_params(colors='white')
        
        canvas = FigureCanvasTkAgg(fig, self.chart_display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def show_pie_chart(self):
        """Mostrar gráfico de pizza"""
        self.clear_chart_frame()
        
        fig = Figure(figsize=(8, 6), dpi=100, facecolor='#1a1a1a')
        ax = fig.add_subplot(111)
        
        labels = ['Vendas', 'Marketing', 'TI', 'RH', 'Operações']
        sizes = [35, 25, 20, 10, 10]
        colors = ['#2CC985', '#2FA572', '#26A669', '#1F8C5A', '#197A4D']
        
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90,
               textprops={'color': 'white'})
        ax.axis('equal')
        ax.set_title('Distribuição de Orçamento - Gráfico de Pizza', color='white')
        
        canvas = FigureCanvasTkAgg(fig, self.chart_display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def show_line_chart(self):
        """Mostrar gráfico de linhas"""
        self.clear_chart_frame()
        
        fig = Figure(figsize=(10, 6), dpi=100, facecolor='#1a1a1a')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#1a1a1a')
        
        months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        sales_2023 = [120, 150, 130, 160, 170, 190, 200, 210, 190, 220, 230, 250]
        sales_2024 = [140, 160, 150, 180, 190, 210, 220, 230, 210, 240, 250, 270]
        
        ax.plot(months, sales_2023, marker='o', label='2023', linewidth=2, color='#2CC985')
        ax.plot(months, sales_2024, marker='s', label='2024', linewidth=2, color='#2FA572')
        
        ax.set_xlabel('Meses', color='white')
        ax.set_ylabel('Vendas (R$ mil)', color='white')
        ax.set_title('Evolução de Vendas - Gráfico de Linhas', color='white')
        ax.set_xticklabels(months, color='white')
        ax.set_yticklabels(ax.get_yticks(), color='white')
        ax.legend(facecolor='#1a1a1a', labelcolor='white')
        ax.grid(True, alpha=0.3, color='#2d2d2d')
        
        # Configurar cores dos eixos
        for spine in ax.spines.values():
            spine.set_color('#2CC985')
        ax.tick_params(colors='white')
        
        canvas = FigureCanvasTkAgg(fig, self.chart_display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def show_area_chart(self):
        """Mostrar gráfico de área"""
        self.clear_chart_frame()
        
        fig = Figure(figsize=(10, 6), dpi=100, facecolor='#1a1a1a')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#1a1a1a')
        
        x = range(1, 11)
        y1 = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]
        y2 = [2, 4, 3, 5, 4, 6, 5, 7, 6, 8]
        
        ax.fill_between(x, y1, alpha=0.4, label='Produto A', color='#2CC985')
        ax.fill_between(x, y2, alpha=0.4, label='Produto B', color='#2FA572')
        ax.plot(x, y1, linewidth=2, color='#2CC985')
        ax.plot(x, y2, linewidth=2, color='#2FA572')
        
        ax.set_xlabel('Tempo', color='white')
        ax.set_ylabel('Performance', color='white')
        ax.set_title('Performance Comparativa - Gráfico de Área', color='white')
        ax.set_xticklabels(ax.get_xticks(), color='white')
        ax.set_yticklabels(ax.get_yticks(), color='white')
        ax.legend(facecolor='#1a1a1a', labelcolor='white')
        ax.grid(True, alpha=0.3, color='#2d2d2d')
        
        # Configurar cores dos eixos
        for spine in ax.spines.values():
            spine.set_color('#2CC985')
        ax.tick_params(colors='white')
        
        canvas = FigureCanvasTkAgg(fig, self.chart_display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def clear_chart_frame(self):
        """Limpar frame do gráfico"""
        for widget in self.chart_display_frame.winfo_children():
            widget.destroy()
    
    def setup_reports_tab(self):
        """Configurar aba de relatórios"""
        # Tabela de dados
        table_frame = ctk.CTkFrame(self.reports_tab, fg_color="#1a1a1a")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Criar tabela usando Treeview com estilo personalizado
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", 
                       background="#1a1a1a",
                       foreground="white",
                       fieldbackground="#1a1a1a",
                       borderwidth=0)
        style.configure("Treeview.Heading",
                       background="#2CC985",
                       foreground="white",
                       borderwidth=0)
        style.map('Treeview', background=[('selected', '#2FA572')])
        
        columns = ('Data', 'Vendas', 'Despesas', 'Lucro')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15, style="Treeview")
        
        # Definir cabeçalhos
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        # Adicionar dados de exemplo
        for i in range(50):
            date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
            sales = random.randint(800, 1200)
            expenses = random.randint(400, 800)
            profit = sales - expenses
            
            self.tree.insert('', 'end', values=(date, f'R$ {sales}', f'R$ {expenses}', f'R$ {profit}'))
        
        # Scrollbar para a tabela
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def setup_settings_tab(self):
        """Configurar aba de configurações"""
        settings_frame = ctk.CTkFrame(self.settings_tab, fg_color="#1a1a1a")
        settings_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Tema
        theme_frame = ctk.CTkFrame(settings_frame, fg_color="#1a1a1a")
        theme_frame.pack(fill="x", pady=10)
        
        theme_label = ctk.CTkLabel(theme_frame, text="Tema:", 
                                 font=ctk.CTkFont(weight="bold"),
                                 text_color="#2CC985")
        theme_label.pack(anchor="w", pady=(10, 5))
        
        theme_options = ["Dark", "Light", "System"]
        self.theme_var = tk.StringVar(value="Dark")
        
        for option in theme_options:
            rb = ctk.CTkRadioButton(theme_frame, text=option, variable=self.theme_var,
                                  value=option, command=self.change_theme,
                                  fg_color="#2CC985", hover_color="#2FA572")
            rb.pack(anchor="w", pady=2)
        
        # Configurações de atualização
        update_frame = ctk.CTkFrame(settings_frame, fg_color="#1a1a1a")
        update_frame.pack(fill="x", pady=10)
        
        update_label = ctk.CTkLabel(update_frame, text="Atualização:", 
                                  font=ctk.CTkFont(weight="bold"),
                                  text_color="#2CC985")
        update_label.pack(anchor="w", pady=(10, 5))
        
        self.update_freq = ctk.CTkSlider(update_frame, from_=1, to=60, 
                                       number_of_steps=59, command=self.update_frequency,
                                       fg_color="#1a1a1a", progress_color="#2CC985",
                                       button_color="#2CC985", button_hover_color="#2FA572")
        self.update_freq.set(5)
        self.update_freq.pack(fill="x", padx=10, pady=5)
        
        freq_label = ctk.CTkLabel(update_frame, text="Frequência: 5 minutos",
                                text_color="white")
        freq_label.pack(anchor="w", padx=10)
        
        # Botão de exportar
        export_btn = ctk.CTkButton(settings_frame, text="📤 Exportar Dados", 
                                 command=self.export_data,
                                 fg_color="#2CC985", hover_color="#2FA572")
        export_btn.pack(pady=20)
    
    # Métodos de callback
    def show_overview(self):
        self.tabview.set("🌿 Visão Geral")
    
    def show_charts(self):
        self.tabview.set("📈 Gráficos")
    
    def show_reports(self):
        self.tabview.set("📋 Relatórios")
    
    def show_settings(self):
        self.tabview.set("⚙️ Configurações")
    
    def update_filters(self):
        """Atualizar filtros baseados no checklist"""
        active_filters = [key for key, var in self.check_vars.items() if var.get()]
        print(f"Filtros ativos: {active_filters}")
    
    def toggle_dark_mode(self):
        """Alternar modo escuro/claro"""
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
    
    def toggle_auto_update(self):
        """Alternar atualização automática"""
        state = self.switch_vars["Atualização Automática"].get()
        print(f"Atualização automática: {'Ativada' if state else 'Desativada'}")
    
    def toggle_notifications(self):
        """Alternar notificações"""
        state = self.switch_vars["Notificações"].get()
        print(f"Notificações: {'Ativadas' if state else 'Desativadas'}")
    
    def submit_form(self):
        """Processar formulário"""
        text_value = self.text_entry.get()
        combo_value = self.combo_var.get()
        print(f"Formulário enviado - Texto: {text_value}, Combo: {combo_value}")
    
    def change_theme(self):
        """Mudar tema"""
        theme = self.theme_var.get()
        ctk.set_appearance_mode(theme)
    
    def update_frequency(self, value):
        """Atualizar frequência de atualização"""
        print(f"Frequência de atualização alterada para: {int(float(value))} minutos")
    
    def export_data(self):
        """Exportar dados"""
        print("Exportando dados...")
        # Aqui você implementaria a lógica de exportação
    
    def run(self):
        """Executar aplicação"""
        self.root.mainloop()

if __name__ == "__main__":
    app = DashboardApp()
    app.run()