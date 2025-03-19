async function processImage() {
  const file = document.getElementById('imageInput').files[0];
  const formData = new FormData();
  formData.append('image', file);

  // Replace with your backend URL later
  const response = await fetch('https://your-backend-url/remove-bg', {
    method: 'POST',
    body: formData
  });
  
  const result = await response.blob();
  document.getElementById('resultImage').src = URL.createObjectURL(result);
}