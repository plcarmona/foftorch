import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Cargar los datos del archivo CSV
data = pd.read_csv('datos_accion.csv')

# Seleccionar las columnas relevantes
data = data[['precio']]

# Escalar los datos
scaler = MinMaxScaler()
data = scaler.fit_transform(data)

# Convertir los datos en tensores de PyTorch
data = torch.FloatTensor(data)

# Definir la arquitectura del modelo
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(1, 32)
        self.fc2 = nn.Linear(32, 64)
        self.fc3 = nn.Linear(64, 1)
        
    def forward(self, x):
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Crear una instancia del modelo
model = Model()

# Definir la función de pérdida y el optimizador
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entrenar el modelo
for epoch in range(100):
    optimizer.zero_grad()
    output = model(data[:-1])
    loss = criterion(output, data[1:])
    loss.backward()
    optimizer.step()

# Hacer una predicción
prediction = model(data[-1:])
prediction = scaler.inverse_transform(prediction.detach().numpy())
print(prediction)
