import streamlit as st
import utils

st.set_page_config(
    page_title="محاكاة الوسط الحضري",
    page_icon=":computer:",
)

st.markdown("""<style>html{direction:rtl;} .math{direction:ltr;}</style>""", unsafe_allow_html=True)

st.title('محاكاة للسجل الإجتماعي الموحد بالوسط الحضري')

kmu = 9.825
current_sum = 0
options = list()

for m in utils.make_smu_metrics():
    v = 0
    if m.kind == 'checkbox':
        v = st.checkbox(label=m.label, key=m._id)
    elif m.kind == 'text-input':
        v = st.number_input(label=m.label, key=m._id, step=1, min_value=0)
    elif m.kind == 'select-input':
        options.append(m)
    
    #~
    current_sum +=  v * m.score

selected = st.selectbox(
    'الجهة',
    options=options,
    format_func= lambda o: o.label
)

if selected:
    st.latex(
        r'''
        S_{mu} = \sum_{i=1}^{35} C_i * V_i + K_{zg} + K_{mu} =
        ''' + rf''' {current_sum + kmu + selected.score}  '''
    )

    st.latex(r'''K_{zg} =''' + rf'''{selected.score} \; (المقدار \; الثابت \; الخاص \; بكل \;  جهة).''')
    st.latex(r'''K_{mu} =''' + rf'''{kmu} \; (المقدار \;الثابت  \;الخاص  \;بالوسط \; الحضري).''')

