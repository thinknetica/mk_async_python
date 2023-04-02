import torch
import asyncio


# Функция для обучения модели на заданном устройстве (GPU)
async def train_on_device(device, x, y):
    # Создаем нейронную сеть
    model = torch.nn.Sequential(
        torch.nn.Linear(1, 10),
        torch.nn.ReLU(),
        torch.nn.Linear(10, 1)
    )
    # Определяем функцию потерь и оптимизатор
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

    # Перемещаем модель и данные на указанное устройство
    model.to(device)
    x = x.to(device)
    y = y.to(device)

    # Обучаем модель
    for _ in range(1000):
        y_pred = model(x)
        loss = loss_fn(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    return model


# Основная функция
async def main():
    # Генерируем случайные данные
    x = torch.randn(1000, 1)
    y = x * 2 + torch.randn(1000, 1) * 0.1

    # Обучаем модель на нескольких GPU
    devices = ['cuda:0', 'cuda:1']
    tasks = [asyncio.create_task(train_on_device(device, x, y)) for device in devices]
    models = await asyncio.gather(*tasks)

    # Объединяем модели, обученные на разных устройствах, в одну модель
    combined_model = torch.nn.Sequential(
        torch.nn.Linear(1, 10),
        torch.nn.ReLU(),
        torch.nn.Linear(10, 1)
    )
    for model in models:
        combined_model.load_state_dict(model.state_dict())
    print(combined_model)


if __name__ == "__main__":
    # Запускаем основную функцию с помощью asyncio.run
    asyncio.run(main())
