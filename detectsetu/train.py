import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import os

# ======== CONFIG ========
dataset_path = r"C:\Users\khush\detectsetu\processed_dataset"
batch_size = 32
epochs = 15
learning_rate = 0.001
img_size = 128
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# =======================

# Transformations: normalize and convert to tensor
transform = transforms.Compose([
    transforms.Grayscale(),  # already grayscale, but just in case
    transforms.Resize((img_size, img_size)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Load dataset
full_dataset = datasets.ImageFolder(root=dataset_path, transform=transform)

# Split into train and validation (80/20)
train_size = int(0.8 * len(full_dataset))
val_size = len(full_dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(full_dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Get number of classes
num_classes = len(full_dataset.classes)
print("Classes:", full_dataset.classes)

# ======== CNN MODEL ========
class ISL_CNN(nn.Module):
    def __init__(self, num_classes):
        super(ISL_CNN, self).__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),  # input 1 channel
            nn.ReLU(),
            nn.MaxPool2d(2,2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2,2)
        )
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * (img_size//4) * (img_size//4), 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, num_classes)
        )
    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x

model = ISL_CNN(num_classes).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# ======== TRAINING ========
for epoch in range(epochs):
    model.train()
    running_loss = 0
    correct = 0
    total = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    train_acc = 100 * correct / total
    print(f"Epoch [{epoch+1}/{epochs}] Loss: {running_loss/len(train_loader):.4f} Train Accuracy: {train_acc:.2f}%")

print("✅ Training completed!")

# Save model
model_path = os.path.join(os.getcwd(), "isl_model.pth")
torch.save(model.state_dict(), model_path)
print(f"Model saved to {model_path}")
