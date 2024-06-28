import tkinter as tk  
from tkinter import simpledialog, messagebox  
  
def perform_xor_operation(m, t):  
    results = []  
    for x in range(256):  
        for a in range(256):  
            m1 = (m & 0xff)  
            m2 = ((m >> 8) & 0xff)  
            m3 = ((m >> 16) & 0xff)  
            m4 = ((m >> 24) & 0xff)  
              
            t1 = (t & 0xff)  
            t2 = ((t >> 8) & 0xff)  
            t3 = ((t >> 16) & 0xff)  
            t4 = ((t >> 24) & 0xff)  
              
            if m1 == (t1 + a & 0xff) ^ x and m2 == (t2 + a & 0xff) ^ x and m3 == (t3 + a & 0xff) ^ x and m4 == (t4 + a & 0xff) ^ x:  
                results.append(f"xor {x:02X} add {(0x100 - a & 0xff):02X}")  
            if m1 == ((t1 ^ x) + a & 0xff) and m2 == ((t2 ^ x) + a & 0xff) and m3 == ((t3 ^ x) + a & 0xff) and m4 == ((t4 ^ x) + a & 0xff):  
                results.append(f"add {(0x100 - a & 0xff):02X} xor {x:02X}")  
    return results  
  
def on_calculate():  
    try:  
        m_value = int(m_entry.get(), 16)  
        t_value = int(t_entry.get(), 16)  
        results = perform_xor_operation(m_value, t_value)  
        result_text.delete('1.0', tk.END)  
        for result in results:  
            result_text.insert(tk.END, result + '\n')  
    except ValueError:  
        messagebox.showerror("错误", "请输入有效的十六进制数！")  
  
root = tk.Tk()  
root.title("二次异或解密工具")  
  
m_label = tk.Label(root, text="密文m (十六进制):")  
m_label.pack()  
m_entry = tk.Entry(root)  
m_entry.pack()  
  
t_label = tk.Label(root, text="明文t (十六进制):")  
t_label.pack()  
t_entry = tk.Entry(root)  
t_entry.pack()  
  
calculate_button = tk.Button(root, text="计算", command=on_calculate)  
calculate_button.pack()  
  
result_label = tk.Label(root, text="结果:")  
result_label.pack()  
result_text = tk.Text(root, height=10, width=50)  
result_text.pack()  
  
root.mainloop()