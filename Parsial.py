import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Analisis Biaya Produksi Cilok - Turunan Parsial")

# Input dari pengguna
st.subheader("Input Jumlah Bahan")
x0 = st.number_input("Jumlah Tepung (kg)", value=2.0)
y0 = st.number_input("Jumlah Daging (kg)", value=3.0)

# Definisi simbol dan fungsi biaya
x, y = sp.symbols('x y')
f_xy = 5*x**2 + 4*x*y + 6*y**2 + 200

# Turunan parsial
fx = sp.diff(f_xy, x)
fy = sp.diff(f_xy, y)

# Evaluasi turunan dan fungsi pada titik
fx_val = fx.subs({x: x0, y: y0})
fy_val = fy.subs({x: x0, y: y0})
f_val = f_xy.subs({x: x0, y: y0})

# Tampilkan hasil
st.write(f"\( f(x, y) = {sp.latex(f_xy)} \)")
st.latex(f"\frac{{\partial f}}{{\partial x}} = {sp.latex(fx)}")
st.latex(f"\frac{{\partial f}}{{\partial y}} = {sp.latex(fy)}")
st.write(f"Evaluasi di titik ({x0}, {y0}):")
st.latex(f"\frac{{\partial f}}{{\partial x}}({x0},{y0}) = {fx_val}")
st.latex(f"\frac{{\partial f}}{{\partial y}}({x0},{y0}) = {fy_val}")
st.latex(f"f({x0},{y0}) = {f_val}")

# Visualisasi grafik
X = np.linspace(x0 - 2, x0 + 2, 50)
Y = np.linspace(y0 - 2, y0 + 2, 50)
X, Y = np.meshgrid(X, Y)

f_lambd = sp.lambdify((x, y), f_xy, 'numpy')
Z = f_lambd(X, Y)
Zt = float(f_val) + float(fx_val)*(X - x0) + float(fy_val)*(Y - y0)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis')
ax.plot_surface(X, Y, Zt, alpha=0.4, color='red')

ax.set_xlabel("Tepung (kg)")
ax.set_ylabel("Daging (kg)")
ax.set_zlabel("Biaya (Rp)")
ax.set_title("Grafik Biaya dan Bidang Singgung")

st.pyplot(fig)
