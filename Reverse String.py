def play():
    input = raw_input("Select one of the following:\n'1' for reverse_string,\n'2' for reverse_string_with_stack, or\n'3' for reverse_sort\n>> ")
    while True:
        if input == '1':
            reverse_string()
            break
        if input == '2':
            reverse_string_with_stack()
            break
        if input == '3':
            reverse_short()
            break
        else:
            print "invalid entry.  Good bye!"
            break
        
def reverse_string():
    s = raw_input("Type the thing you want to reverse\n>> ")
    st = []
    for i in s:
        st.append(i)
    ts = st[::-1]
    print "".join(ts)
    print "this was reverse_string"
    
#reverse_string()


def reverse_string_with_stack():
    s = raw_input("Type the thing you want to reverse using a stack\n>> ")
    st = []
    ts = []
    for i in s:
        st.append(i)
    while len(st) != 0:
        ts.append(st.pop())
    print "".join(ts)
    print "this was reverse_string_with_stack"
    
#reverse_string_with_stack()


def reverse_short():
    s = raw_input("Type the thing you want to reverse using the short version\n>> ")
    st = []
    for i in s:
        st.append(i)
    st.reverse()
    print ''.join(st)
    print "this was reverse_short"
    
#reverse_short()


play()