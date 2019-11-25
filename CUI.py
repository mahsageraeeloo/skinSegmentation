import dill as pickle


def load_model(file_name):
    with open(file_name, 'rb') as f:
        loaded_model = pickle.load(f)
    return loaded_model


print('Hi, welcome to SkinSegmentation Predictor.')
print('Here, you are asked to enter values for Red(R), Green(G), and Blue(B).')
end = 'Y'
while end == 'y' or end == 'Y':
    print('R', end=':')
    red = input()
    print('G', end=':')
    green = input()
    print('B', end=':')
    blue = input()
    filename = 'rfModel_v1.pk'
    model = load_model(filename)
    result = model.predict([[blue, green, red]])
    resultStr = "Skin" if result == 1 else "Non-Skin"
    print('Result is ' + resultStr)
    print('Do you want to continue? (Y/N)')
    end = input()