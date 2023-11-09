#making dataset
from PIL import Image
from torch.utils.data import Dataset
import torchvision.transforms as transforms

# defining transform for resnet
resNetTransform = transforms.Compose([
    transforms.Resize((224, 224)), # change to what data should be
    transforms.ToTensor(),
    ])

# makes a custom dataset based on pytorch dataset class
class PlantDataset(Dataset):
    def __init__(self, data_dir, arr, transform = resNetTransform):
        # initialize some valuess
        self.data_dir = data_dir
        self.data = [img for img, _ in arr]
        self.arr = arr

        #transform to normalize/resize all images
        self.transform = transform
    
    def __len__(self):
        return len(self.arr)
    
    def __getitem__(self, idx):
        img, label = self.arr[idx] 
        img = self.transform(Image.open(img))
                
        #returns a tuple of the transformed image and the label (one-hot encoding)
        return (img, label)