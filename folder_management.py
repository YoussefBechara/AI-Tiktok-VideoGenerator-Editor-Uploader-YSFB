import os

folder_name = 'output_videos'

def clear_folder(folder_path):
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"The folder {folder_path} does not exist.")
            return

        # Get a list of all files in the folder
        files = os.listdir(folder_path)

        # Iterate through the files and delete each one
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
           
def count_vids_already_made(folder_path=folder_name):
    try:
        # Construct the absolute path to the folder
        folder_path = os.path.abspath(folder_path)
        
        # Get the list of files in the folder
        files = os.listdir(folder_path)
        
        # Filter only the .mp4 files
        mp4_files = [file for file in files if file.lower().endswith('.mp4')]
        
        # Count the number of .mp4 files
        num_files = len(mp4_files)
        
        return num_files
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Specify the folder name (assuming it's in the same directory as the script)
if __name__ == '__main__':
    num_mp4_files = count_vids_already_made(folder_name)
    print(num_mp4_files)
