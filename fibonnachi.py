import streamlit as st

st.title('Fibonacchi calculator')
n = st.text_input('What Fibonacchi number do you want?',0) # we want the nth Fibbonachi number
n = int(n)

FNM2 = 0
FNM1 = 1

if n < 0:
    st.write('Program only computes non-negative Fibonacchi numbers')
else:
    if n == 0:
        F = FNM2
    elif n == 1:
        F = FNM1
    else:
        for i in range(n-1):
            F = FNM1+FNM2
            FNM2 = FNM1
            FNM1 = F

    st.write(f'The n={n} fibonacchi number is: {F}')

