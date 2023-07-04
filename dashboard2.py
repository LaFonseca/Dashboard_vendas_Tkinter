import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data


plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#354F70", "#2C3E50", "#223142", "#294162"])

# Gráfico 1
fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Vendas por produto R$")
ax1.set_xlabel("Produto")
ax1.set_ylabel("Vendas")
# plt.show()

# Gráfico 2
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Estoque por produto")
ax2.set_xlabel("Estoque")
ax2.set_ylabel("Produto")
# plt.show()

# Gráfico 3
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
ax3.set_title("Percentual Vendas \nTotal Produto")
# plt.show()

# Gráfico 4 
fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Vendas por ano R$")
ax4.set_xlabel("Anos")
ax4.set_ylabel("Vendas")
# plt.show()

# Gráfico 5
fig5, ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(),
                 inventory_month_data.values())
ax5.set_title("Estoque por mês")
ax5.set_xlabel("Mês")
ax5.set_ylabel("Estoque")
# plt.show()

# Janela para os gráficos
root = tk.Tk()
root.title("Dashboard")
root.state('zoomed')

side_frame = tk.Frame(root, bg= "#1F2D3D")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard \nVendas", bg= "#1F2D3D", fg="#FFF", font=18)
label.pack(pady=20, padx=10)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

fig1.set_size_inches(fig1.get_size_inches()[0]*0.7, fig1.get_size_inches()[1]*0.7)
canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

fig4.set_size_inches(fig4.get_size_inches()[0]*0.7, fig4.get_size_inches()[1]*0.7)
canvas2 = FigureCanvasTkAgg(fig4, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

fig3.set_size_inches(fig3.get_size_inches()[0]*0.9, fig3.get_size_inches()[1]*0.9)
canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)


lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

fig2.set_size_inches(fig2.get_size_inches()[0]*0.8, fig2.get_size_inches()[1]*0.8)
canvas4 = FigureCanvasTkAgg(fig2, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

fig5.set_size_inches(fig5.get_size_inches()[0]*0.8, fig5.get_size_inches()[1]*0.8)
canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

root.mainloop()