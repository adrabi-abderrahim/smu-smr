import streamlit as st
import utils

st.set_page_config(
    page_title="محاكاة الوسط القروي",
    page_icon=":computer:",
)

st.markdown("""<style>html{direction:rtl;} .math{direction:ltr;}</style>""", unsafe_allow_html=True)

st.title('محاكاة للسجل الإجتماعي الموحد بالوسط القروي')
st.markdown('---')

kmu = 8.695
current_sum = 0
options = list()

for m in utils.make_smr_metrics():
    v = 0
    if m.kind == 'checkbox':
        v = st.checkbox(label= f'''{m.label} **(C = {m.score})** ''', key=m._id)
    elif m.kind == 'text-input':
        v = st.number_input(label=f'''{m.label} **(C = {m.score})** ''', key=m._id, min_value=0.00)
    elif m.kind == 'select-input':
        options.append(m)
    #~
    current_sum +=  v * m.score

selected = st.selectbox(
    'الجهة',
    options=options,
    format_func= lambda o: f'''{o.label} (C = {o.score}) '''
)

if selected:
    st.markdown('---')

    st.latex(
        r'''
        S_{mr} = \sum_{i=1}^{28} C_i * V_i + K_{zg} + K_{mr} =
        ''' + rf''' {current_sum + kmu + selected.score:.7f}  '''
    )

    st.latex(r'''K_{zg} =''' + rf'''{selected.score} \; (المقدار \; الثابت \; الخاص \; بكل \;  جهة).''')
    st.latex(r'''K_{mr} =''' + rf'''{kmu} \; (المقدار \;الثابت  \;الخاص  \;بالوسط \; القروي).''')

