import cv2
import os

def images_to_video(image_folder, output_file, fps=1):
    """
    Converts a sequence of images into a video file.
    
    :param image_folder: Folder containing images
    :param output_file: Output video file name
    :param fps: Frames per second (default is 1 frame per second)
    """
    # Get list of images sorted by name
    images = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".png"))]
    images.sort()

    # Check if images exist
    if not images:
        print("No images found in the folder!")
        return

    # Read the first image to get dimensions
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Define video codec and create VideoWriter object
    video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Add images to video
    for image in images:
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)
        video.write(frame)
        print(f"Added {image} to video")

    # Release video object
    video.release()
    print(f"Video saved as {output_file}")

if __name__ == "__main__":
    # Set input folder and output file
    input_folder = "./images"
    output_file = "output_video.mp4"
    fps = 1  # 1 frame per second

    # Convert images to video
    images_to_video(input_folder, output_file, fps)
