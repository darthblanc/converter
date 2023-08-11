import tkinter as tk
from tkinter import LEFT, BOTTOM, RIGHT, CENTER
from temperature_converter import temp_lobby
from distance_converter import convert_within_metric, convert_within_systemic, metric_to_systemic, systemic_to_metric
from currency_converter import convert_currency


def render_temp_window():
    temp = tk.Tk()
    temp.geometry("250x200")

    temp_value = tk.StringVar(temp)
    temp_value_prompt = tk.Label(temp, text="Temperature: ", font=("Ariel", 10))
    temp_value_entry = tk.Entry(temp, textvariable=temp_value, font=("Ariel", 10))
    temp_value_prompt.grid(row=0, column=0)
    temp_value_entry.grid(row=0, column=1)

    temp_unit_from = tk.StringVar(temp)
    temp_unit_in_prompt = tk.Label(temp, text="Unit from: ", font=("Ariel", 10))
    temp_unit_in = tk.Entry(temp, textvariable=temp_unit_from, font=("Ariel", 10))
    temp_unit_in_prompt.grid(row=1, column=0)
    temp_unit_in.grid(row=1, column=1)

    temp_unit_to = tk.StringVar(temp)
    temp_unit_out_prompt = tk.Label(temp, text="Unit to: ", font=("Ariel", 10))
    temp_unit_out = tk.Entry(temp, textvariable=temp_unit_to, font=("Ariel", 10))
    temp_unit_out_prompt.grid(row=2, column=0)
    temp_unit_out.grid(row=2, column=1)

    def collect_temp_info():
        output = tk.Text(temp, font=("Ariel", 18), height=1, width=7)
        value_in = temp_value
        unit_in = temp_unit_from
        unit_out = temp_unit_to
        value_out, _ = temp_lobby(value_in=value_in.get(), unit_in=unit_in.get(), unit_out=unit_out.get())
        output.insert(tk.END, f"{value_out} {unit_out.get()}")
        output.grid(row=4, column=1)

    temp_enter = tk.Button(temp, font=("Ariel", 10), text="ENTER", command=collect_temp_info)
    temp_enter.grid(row=3, column=1)
    temp.mainloop()


def render_dist_window():
    dist = tk.Tk()
    dist.geometry("200x120")

    def convert_in_metric():
        metric_conv = tk.Tk()
        value_in = tk.StringVar(metric_conv)
        value_entry_prompt = tk.Label(metric_conv, text="Distance: ", font=("Ariel", 10))
        value_entry = tk.Entry(metric_conv, textvariable=value_in, font=("Ariel", 10))
        value_entry_prompt.grid(row=0, column=0)
        value_entry.grid(row=0, column=1)

        unit_in = tk.StringVar(metric_conv)
        unit_in_entry_prompt = tk.Label(metric_conv, text="Unit from: ", font=("Ariel", 10))
        unit_in_entry = tk.Entry(metric_conv, textvariable=unit_in, font=("Ariel", 10))
        unit_in_entry_prompt.grid(row=1, column=0)
        unit_in_entry.grid(row=1, column=1)

        unit_out = tk.StringVar(metric_conv)
        unit_out_entry_prompt = tk.Label(metric_conv, text="Unit to: ", font=("Ariel", 10))
        unit_out_entry = tk.Entry(metric_conv, textvariable=unit_out, font=("Ariel", 10))
        unit_out_entry_prompt.grid(row=2, column=0)
        unit_out_entry.grid(row=2, column=1)

        def collect_dist_info():
            output = tk.Text(metric_conv, font=("Ariel", 10), height=1, width=7)
            value_out, _ = convert_within_metric(value_in=int(value_in.get()), unit_in=unit_in.get(),
                                                 unit_out=unit_out.get())
            output.insert(tk.END, f"{value_out} {unit_out.get()}")
            output.grid(row=3, column=1)

        button = tk.Button(metric_conv, text="convert", font=("Ariel", 10), command=collect_dist_info)
        button.grid(row=3, column=0)

    def convert_in_systemic():
        metric_conv = tk.Tk()
        value_in = tk.StringVar(metric_conv)
        value_entry_prompt = tk.Label(metric_conv, text="Distance: ", font=("Ariel", 10))
        value_entry = tk.Entry(metric_conv, textvariable=value_in, font=("Ariel", 10))
        value_entry_prompt.grid(row=0, column=0)
        value_entry.grid(row=0, column=1)

        unit_in = tk.StringVar(metric_conv)
        unit_in_entry_prompt = tk.Label(metric_conv, text="Unit from: ", font=("Ariel", 10))
        unit_in_entry = tk.Entry(metric_conv, textvariable=unit_in, font=("Ariel", 10))
        unit_in_entry_prompt.grid(row=1, column=0)
        unit_in_entry.grid(row=1, column=1)

        unit_out = tk.StringVar(metric_conv)
        unit_out_entry_prompt = tk.Label(metric_conv, text="Unit to: ", font=("Ariel", 10))
        unit_out_entry = tk.Entry(metric_conv, textvariable=unit_out, font=("Ariel", 10))
        unit_out_entry_prompt.grid(row=2, column=0)
        unit_out_entry.grid(row=2, column=1)

        def collect_dist_info():
            output = tk.Text(metric_conv, font=("Ariel", 10), height=1, width=7)
            value_out, _ = convert_within_systemic(value_in=int(value_in.get()), unit_in=unit_in.get(),
                                                   unit_out=unit_out.get())
            output.insert(tk.END, f"{value_out} {unit_out.get()}")
            output.grid(row=3, column=1)

        button = tk.Button(metric_conv, text="convert", font=("Ariel", 10), command=collect_dist_info)
        button.grid(row=3, column=0)

    def convert_metric_symmetric():
        metric_conv = tk.Tk()
        value_in = tk.StringVar(metric_conv)
        value_entry_prompt = tk.Label(metric_conv, text="Distance: ", font=("Ariel", 10))
        value_entry = tk.Entry(metric_conv, textvariable=value_in, font=("Ariel", 10))
        value_entry_prompt.grid(row=0, column=0)
        value_entry.grid(row=0, column=1)

        unit_in = tk.StringVar(metric_conv)
        unit_in_entry_prompt = tk.Label(metric_conv, text="Unit from: ", font=("Ariel", 10))
        unit_in_entry = tk.Entry(metric_conv, textvariable=unit_in, font=("Ariel", 10))
        unit_in_entry_prompt.grid(row=1, column=0)
        unit_in_entry.grid(row=1, column=1)

        unit_out = tk.StringVar(metric_conv)
        unit_out_entry_prompt = tk.Label(metric_conv, text="Unit to: ", font=("Ariel", 10))
        unit_out_entry = tk.Entry(metric_conv, textvariable=unit_out, font=("Ariel", 10))
        unit_out_entry_prompt.grid(row=2, column=0)
        unit_out_entry.grid(row=2, column=1)

        def collect_dist_info():
            output = tk.Text(metric_conv, font=("Ariel", 10), height=1, width=7)
            value_out, _ = metric_to_systemic(value_in=int(value_in.get()), unit_in=unit_in.get(),
                                              unit_out=unit_out.get())
            output.insert(tk.END, f"{value_out} {unit_out.get()}")
            output.grid(row=3, column=1)

        button = tk.Button(metric_conv, text="convert", font=("Ariel", 10), command=collect_dist_info)
        button.grid(row=3, column=0)

    def convert_symmetric_metric():
        metric_conv = tk.Tk()
        value_in = tk.StringVar(metric_conv)
        value_entry_prompt = tk.Label(metric_conv, text="Distance: ", font=("Ariel", 10))
        value_entry = tk.Entry(metric_conv, textvariable=value_in, font=("Ariel", 10))
        value_entry_prompt.grid(row=0, column=0)
        value_entry.grid(row=0, column=1)

        unit_in = tk.StringVar(metric_conv)
        unit_in_entry_prompt = tk.Label(metric_conv, text="Unit from: ", font=("Ariel", 10))
        unit_in_entry = tk.Entry(metric_conv, textvariable=unit_in, font=("Ariel", 10))
        unit_in_entry_prompt.grid(row=1, column=0)
        unit_in_entry.grid(row=1, column=1)

        unit_out = tk.StringVar(metric_conv)
        unit_out_entry_prompt = tk.Label(metric_conv, text="Unit to: ", font=("Ariel", 10))
        unit_out_entry = tk.Entry(metric_conv, textvariable=unit_out, font=("Ariel", 10))
        unit_out_entry_prompt.grid(row=2, column=0)
        unit_out_entry.grid(row=2, column=1)

        def collect_dist_info():
            output = tk.Text(metric_conv, font=("Ariel", 10), height=1, width=7)
            value_out, _ = systemic_to_metric(value_in=int(value_in.get()), unit_in=unit_in.get(),
                                              unit_out=unit_out.get())
            output.insert(tk.END, f"{value_out} {unit_out.get()}")
            output.grid(row=3, column=1)

        button = tk.Button(metric_conv, text="convert", font=("Ariel", 10), command=collect_dist_info)
        button.grid(row=3, column=0)

    dist_metric = tk.Button(dist, text="Convert within metric system", command=convert_in_metric)
    dist_metric.grid(row=0, column=0)
    dist_systemic = tk.Button(dist, text="Convert within systemic system", command=convert_in_systemic)
    dist_systemic.grid(row=1, column=0)
    dist_metric_systemic = tk.Button(dist, text="Convert from metric to systemic", command=convert_metric_symmetric)
    dist_metric_systemic.grid(row=2, column=0)
    dist_systemic_metric = tk.Button(dist, text="Convert from systemic to metric", command=convert_symmetric_metric)
    dist_systemic_metric.grid(row=3, column=0)

    dist.mainloop()


def render_curr_window():
    curr = tk.Tk()
    currency_value = tk.IntVar(curr)
    currency_value_prompt = tk.Label(curr, text="Enter the amount: ", font=("Arial", 10))
    currency_value_entry = tk.Entry(curr, textvariable=currency_value, font=("Arial", 10))
    currency_value_prompt.grid(row=0, column=0)
    currency_value_entry.grid(row=0, column=1)

    currency_in = tk.StringVar(curr)
    currency_in_prompt = tk.Label(curr, text= "Convert from: ", font=("Arial", 10))
    currency_in_entry = tk.Entry(curr, textvariable=currency_in, font=("Arial", 10))
    currency_in_prompt.grid(row=1, column=0)
    currency_in_entry.grid(row=1, column=1)

    currency_out = tk.StringVar(curr)
    currency_out_prompt = tk.Label(curr, text="Convert to: ", font=("Arial", 10))
    currency_out_entry = tk.Entry(curr, textvariable=currency_out, font=("Arial", 10))
    currency_out_prompt.grid(row=2, column=0)
    currency_out_entry.grid(row=2, column=1)

    def collect_info():
        output = tk.Text(curr, font=("Ariel", 10), height=1, width=7)
        print(currency_value.get(), currency_in.get())
        value_out, _ = convert_currency(value_in=currency_value.get(), unit_in=currency_in.get(), unit_out=currency_out.get())
        output.insert(tk.END, f"{value_out} {currency_out.get()}")
        output.grid(row=4, column=0)

    button = tk.Button(curr, text="ENTER", font=("Ariel", 10), command=collect_info)
    button.grid(row=3, column=0)
    curr.mainloop()


root = tk.Tk()
root.geometry("500x100")
frame = tk.Frame(root)
frame.pack()

label = tk.Label(root, text="Converter Suite v1.0", font=("Arial", 18))
label.pack()

# text = tk.Text(root, font=("Ariel", 18))
# print(text.get("1.0", tk.END))
# text.pack()

buttonFrame = tk.Frame(root)
buttonFrame.pack(side=BOTTOM)
temp_button = tk.Button(buttonFrame, text="Temperature", font=("Arial", 18), command=render_temp_window)
dist_button = tk.Button(buttonFrame, text="Distance", font=("Arial", 18), command=render_dist_window)
currency_button = tk.Button(buttonFrame, text="Currency", font=("Arial", 18), command=render_curr_window)
temp_button.pack(side=LEFT)
dist_button.pack(side=LEFT)
currency_button.pack(side=LEFT)

root.mainloop()
