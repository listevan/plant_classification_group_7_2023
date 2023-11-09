import pickle
import torchvision.transforms as transforms
from PIL import Image

model = pickle.load(open('./model.pkl', 'rb'))
transform = transforms.Compose([
    transforms.Resize((224, 224)), # change to what data should be
    transforms.ToTensor(),
    ])

print(model(transform(Image.open('./data/leaf11/data/leaf11/l11nr001.tif'))))