def aneinander(x): 
    def aneinander_x(y): 
        return x + y
    return aneinander_x;

text = aneinander("hallo");
text2 = aneinander("tschüss");

print(aneinander("ich bin"));
print(aneinander("bis später"));