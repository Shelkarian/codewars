def alphabet_position(text):
    st = ''
    for i in text.lower():
        if i in 'abcdefghijklmnopqrstuvwxyz':
            st += f"{ord(i)-96} "
    return st.strip()