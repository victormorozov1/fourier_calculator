import pickle

with open('first.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

for o in range(ord('а'), ord('я') + 1):
    print(
        f'"{o - ord("а") + 1}"[label="{chr(o)}",labelSize=12,labelPosition=LabelTop,labelColor="#ffffffff",labelIsVisible=true,position="274.6943526239039 205.5479646793643",velocity="-3.538835890992686e-17 8.196568423990413e-18",manyBodyStrength=-100,gravityCenter="300 200",gravityStrengthX=0.05,gravityStrengthY=0.05,fixed=false,color="#dcdcdcff",radius=8,borderColor="#dcdcdcff",borderWidth=0,opacity=1,inBags="[]"]'
    )

for d in loaded_data:
    letter1, letter2 = d[0], d[1]
    n1, n2 = ord(letter1) - ord('а') + 1, ord(letter2) - ord('а') + 1
    print(
        f'"{n1}" -> "{n2}"[label="",labelSize=12,labelColor="#dcdcdcff",labelIsVisible=true,distance={d[-1] * 100},strength=0.7,thickness=3,color="#dcdcdcff",opacity=1]'
    )


